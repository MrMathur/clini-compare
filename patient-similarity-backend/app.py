from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
# from services.similarity import calculate_similarity

# Your existing routes...
app = Flask(__name__)
CORS(app)  # This wilsl allow cross-origin requests

# Load your patient dataset (e.g., from a CSV or database)
# patient_data = pd.read_csv('data/patient_data.csv')  # Example CSV file

@app.route('/similarity', methods=['POST'])
def get_similarity():
    input_patient = request.json.get("input_patient")
    # similarity_scores = calculate_similarity(input_patient, patient_data)
    
    # Find the most similar patient
    # most_similar_index = similarity_scores.argmax()
    # most_similar_patient = patient_data.iloc[most_similar_index]
    # similarity_score = similarity_scores[0, most_similar_index]

    # Respond with the most similar patient data and similarity score
    # return jsonify({
    #     "most_similar_patient": most_similar_patient.to_dict(),
    #     "similarity_score": similarity_score
    # })

    return jsonify({
        "input_patient": input_patient
    })

if __name__ == '__main__':
    app.run(debug=True)