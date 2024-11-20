from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer

from scipy.spatial.distance import cosine
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)  # This will allow all origins by default

patients_dataset = pd.read_csv('./data/radiology_embeddings.csv')

def formatStringToArray(string_array):
    cleaned_string = string_array.replace('[', '').replace(']', '').replace('\n', ' ').strip()
    array = np.array([float(x) for x in cleaned_string.split()])
    return array

# patients_dataset['embedding'] = patients_dataset['embedding'].apply(lambda x: np.fromstring(x[1:-1], sep=' '))
patients_dataset['embedding'] = patients_dataset['embedding'].apply(formatStringToArray)

patient_data = {
    "input_note": "",
    "input_embedding": ""
}

model = SentenceTransformer('all-MiniLM-L6-v2')

def test_embeddings(dataset):    
    # Check for rows with string embeddings
    string_check = dataset[dataset['embedding'].apply(lambda x: isinstance(x, str))]
    print("Rows with string embeddings:")
    print(string_check)
    
    # Check for rows with empty list embeddings
    empty_list_check = dataset[dataset['embedding'].apply(lambda x: isinstance(x, list) and len(x) == 0)]
    print("Rows with empty embeddings:")
    print(empty_list_check)
    
    # Check for rows with NaN values in embeddings
    nan_check = dataset[dataset['embedding'].apply(lambda x: any(np.isnan(i) for i in x))]
    print("Rows with NaN values in embeddings:")
    print(nan_check)
    
    # Check for rows with hidden characters or whitespace in embeddings
    hidden_char_check = dataset[dataset['embedding'].apply(lambda x: any(isinstance(i, str) and i.strip() == '' for i in x))]
    print("Rows with hidden characters or whitespace in embeddings:")
    print(hidden_char_check)
    
    # Check for rows with non-numeric types in embeddings
    type_check = dataset[dataset['embedding'].apply(lambda x: not all(isinstance(i, (int, float, np.float64)) for i in x))]
    print("Rows with non-numeric types in embeddings:")
    print(type_check)

    problematic_rows = patients_dataset[patients_dataset['embedding'].apply(
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
    
    print("Done")

def findSimilarPatients(input_embedding):
    df = patients_dataset.copy()
    df['similarity'] = df['embedding'].apply(lambda x: cosine_similarity([input_embedding], [x])[0][0])
    similar_patients = df.sort_values(by='similarity', ascending=False).head(5)
    return similar_patients

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
    similarPatients = findSimilarPatients(input_embedding)
    similarPatientsResponse = similarPatients.to_json(orient="records")
    response = {"input_note": input_note, "similarPatients": similarPatientsResponse}
    return jsonify(response)

@app.route('/get-input_note', methods=['GET'])
def get_ipnut_note():
    response = {"input_note": patient_data['input_note']}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)