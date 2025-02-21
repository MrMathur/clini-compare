from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer

from scipy.spatial.distance import cosine
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import umap

import faiss

app = Flask(__name__)
CORS(app)  # This will allow all origins by default
    
EMBEDDING_TYPE = 'model_1_embedding'
NUM_BINS = 15

patients_dataset = pd.read_csv('./data/training_radiology_embedding.csv')

umap_embedding = pd.read_csv('./data/umap_data.csv')

discharge_notes = pd.read_csv('./data/filtered_discharge_highest.csv')
# Convert umap_embedding DataFrame to a list of dictionaries
umap_embedding_dict = umap_embedding.to_dict(orient="records")

def formatStringToArray(string_array):
    """
    Converts a string representation of a list into a numpy array, or returns the input if it's already an array.
    Args:
        string_array: A string representation of a list or a numpy array.
    Returns:
        np.ndarray: Numpy array of floats.
    """
    if isinstance(string_array, np.ndarray):
        # Already an array, return as is
        return string_array
    elif isinstance(string_array, str):
        # Convert string to numpy array
        try:
            cleaned_string = string_array.replace('[', '').replace(']', '').replace('\n', ' ').strip()
            array = np.array([float(x.strip()) for x in cleaned_string.split(',') if x.strip()])
            return array
        except ValueError as e:
            print(f"Error converting string to array: {string_array}")
            raise e
    else:
        raise TypeError(f"Unsupported type: {type(string_array)}. Expected str or np.ndarray.")


# Create an index for fast similarity search
def build_faiss_index():
    patients_dataset[EMBEDDING_TYPE] = patients_dataset[EMBEDDING_TYPE].apply(formatStringToArray)
    embeddings = np.vstack(patients_dataset[EMBEDDING_TYPE].values).astype("float32")
    index = faiss.IndexFlatIP(embeddings.shape[1])  # Inner product (cosine similarity equivalent)
    index.add(embeddings)
    return index

# Use the index to find similar patients
def findSimilarPatients_faiss(input_embedding, index):
    input_embedding = np.array([input_embedding]).astype("float32")
    similarity_scores, indices = index.search(input_embedding, len(patients_dataset))
    similar_patients = patients_dataset.iloc[indices[0]]
    similar_patients['similarity'] = similarity_scores[0]
    return similar_patients

# Build the index once
faiss_index = build_faiss_index()

patients_dataset[EMBEDDING_TYPE] = patients_dataset[EMBEDDING_TYPE].apply(formatStringToArray)

patient_data = {
    "input_note": "",
    "input_embedding": ""
}

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_statistics(data):
    # Sort by similarity in descending order
    sorted_data = data.sort_values(by="similarity", ascending=False)
    
    # 1) Average similarity across the top 20 similarity scores
    top_20 = sorted_data.head(20)
    avg_similarity_top_20 = top_20['similarity'].mean().item()

    # 2) Number of patients with similarity greater than 0.8
    num_greater_than_0_9 = (sorted_data['similarity'] > 0.8).sum().item()

    # 3) Calculate h-index
    total_entries = len(sorted_data)
    h_index = 0
    for h in range(1, total_entries + 1):
        # Percentage of entries with similarity >= h/100
        percentage_gte_h = (sorted_data['similarity'] >= h / 100).mean()
        if percentage_gte_h >= h / 100:
            h_index = h
        else:
            break

    return {
        "average_similarity_top_20": float(avg_similarity_top_20),
        "num_greater_than_0_9": int(num_greater_than_0_9),
        "h_index": int(h_index),
    }

def calculate_umap_embedding(data, num_of_sim_patients):
    # Ensure 'note_id' exists in the data
    if 'note_id' not in data.columns:
        raise ValueError("The 'note_id' column is missing in the input data.")

    # Convert Series to a 2D NumPy array
    try:
        embedding_array = np.stack(data[EMBEDDING_TYPE].to_numpy())
    except ValueError as e:
        print("Error stacking arrays:", e)
        raise ValueError("Ensure all elements in 'embedding' have the same length and are numeric.")

    # Validate dimensions
    if len(embedding_array.shape) != 2:
        raise ValueError("Input data must be a 2D array where each row is a vector.")

    # Apply UMAP
    reducer = umap.UMAP(n_neighbors=num_of_sim_patients, min_dist=0.1, n_components=2, random_state=42, metric='cosine')
    embedding = reducer.fit_transform(embedding_array)

    # Combine note_id with UMAP embedding
    umap_data = [
        {"note_id": (note_id), "x": float(emb[0]), "y": float(emb[1])}
        for note_id, emb in zip(data["note_id"], embedding)
    ]

    return umap_data

def test_embeddings(dataset):    
    # Check for rows with string embeddings
    string_check = dataset[dataset[EMBEDDING_TYPE].apply(lambda x: isinstance(x, str))]
    print("Rows with string embeddings:")
    print(string_check)
    
    # Check for rows with empty list embeddings
    empty_list_check = dataset[dataset[EMBEDDING_TYPE].apply(lambda x: isinstance(x, list) and len(x) == 0)]
    print("Rows with empty embeddings:")
    print(empty_list_check)
    
    # Check for rows with NaN values in embeddings
    nan_check = dataset[dataset[EMBEDDING_TYPE].apply(lambda x: any(np.isnan(i) for i in x))]
    print("Rows with NaN values in embeddings:")
    print(nan_check)
    
    # Check for rows with hidden characters or whitespace in embeddings
    hidden_char_check = dataset[dataset[EMBEDDING_TYPE].apply(lambda x: any(isinstance(i, str) and i.strip() == '' for i in x))]
    print("Rows with hidden characters or whitespace in embeddings:")
    print(hidden_char_check)
    
    # Check for rows with non-numeric types in embeddings
    type_check = dataset[dataset[EMBEDDING_TYPE].apply(lambda x: not all(isinstance(i, (int, float, np.float64)) for i in x))]
    print("Rows with non-numeric types in embeddings:")
    print(type_check)

    problematic_rows = patients_dataset[patients_dataset[EMBEDDING_TYPE].apply(
    lambda x: isinstance(x, list) and not all(isinstance(i, (int, float, np.float64)) for i in x))]
    print("Problematic rows:")
    print(problematic_rows)
    
    # Attempt to convert each row's embedding to a float array and print any conversion errors
    try:
        for index, row in dataset.iterrows():
            try:
                float_array = np.array(row['embedding'], dtype=float)
            except ValueError as e:
                print(f"Error at row {index}: {e}")
                print("Problematic row data:", row['embedding'])
                break  # Stop after finding the first problematic row
    except Exception as e:
        print(f"Unexpected error: {e}")

def findSimilarPatients(input_embedding):
    df = patients_dataset.copy()
    df['similarity'] = df[EMBEDDING_TYPE].apply(lambda x: cosine_similarity([input_embedding], [x])[0][0])
    similar_patients = df.sort_values(by='similarity', ascending=False)
    return similar_patients

def get_discharge_note_by_subject(subject_id, discharge_notes):
    """
    Retrieves all rows from the discharge_notes DataFrame that match the given subject_id.

    Args:
        subject_id (int or str): The subject_id to search for.
        discharge_notes (pd.DataFrame): The DataFrame containing discharge notes.

    Returns:
        pd.DataFrame: A DataFrame with rows matching the given subject_id.
    """
    # Filter rows based on the subject_id
    filtered_rows = discharge_notes[discharge_notes['subject_id'] == subject_id]
    
    # Return the filtered rows
    return filtered_rows

def create_similarity_histogram(df, NUM_BINS):
    # Define bins based on similarity scores
    bins = np.linspace(df['similarity'].min(), df['similarity'].max(), NUM_BINS + 1)
    
    # Assign bin labels
    df['bin'] = pd.cut(df['similarity'], bins, include_lowest=True)
    
    # Group by bins and collect note_ids as lists
    histogram_df = df.groupby('bin').agg(
        similarity_count=('similarity', 'count'),
        note_ids=('note_id', list)
    ).reset_index()

    num_of_sim_patients = histogram_df.iloc[NUM_BINS - 1]["similarity_count"]

    return histogram_df, num_of_sim_patients

# Basic text cleaning function
def preprocess_text(text):
    text = text.lower().replace('\n', ' ').replace('\r', '')
    return text.strip()

@app.route('/post-input-note', methods=['POST'])
def post_input_note():
    data = request.json
    input_note = data.get('input_note')  # Use dictionary syntax
    input_embedding = model.encode(preprocess_text(input_note))
    patient_data['input_note'] = input_note
    patient_data['input_embedding'] = input_embedding
    response = {"message": "Data received", "received_value": input_note}
    return jsonify(response)

@app.route('/get-similar-patients', methods=['GET'])
def get_similar_patients():
    input_note = patient_data['input_note']
    input_embedding = patient_data['input_embedding']
    # similarPatients = findSimilarPatients(input_embedding)
    similarPatients = findSimilarPatients_faiss(input_embedding, faiss_index)

    similarity_histogram, num_of_sim_patients = create_similarity_histogram(similarPatients, NUM_BINS)
    histogram_response = similarity_histogram.to_json(orient="records")

    similarPatientsToSend = similarPatients.head(num_of_sim_patients)
    print("Debugging")
    print(similarPatientsToSend)
    similarPatientsResponse = similarPatientsToSend.to_json(orient="records")
    statistics = calculate_statistics(similarPatients)
    # Calculate UMAP embedding and convert to list
    # umap_embedding = calculate_umap_embedding(patients_dataset, num_of_sim_patients)
    
    response = {
        "input_note": input_note,
        "similarPatients": similarPatientsResponse,
        "umap_embedding": umap_embedding_dict,
        "statistics": statistics,
        "similarity_histogram" : histogram_response
    }
    return jsonify(response)

@app.route('/post-discharge-note', methods=['POST'])
def post_discharge_note():
    data = request.json
    subject_id = data.get('subject_id')
    discharge_note = get_discharge_note_by_subject(subject_id, discharge_notes)['text'].iloc[0]
    response = {"input_note": patient_data['input_note'], "discharge_note": discharge_note}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)