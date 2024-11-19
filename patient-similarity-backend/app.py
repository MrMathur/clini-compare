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

patients_dataset['embedding'] = patients_dataset['embedding'].apply(lambda x: formatStringToArray(x))

patient_data = {
    "input_note": "",
    "input_embedding": ""
}

model = SentenceTransformer('all-MiniLM-L6-v2')

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