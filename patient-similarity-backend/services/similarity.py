from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity(input_patient, patient_data):
    # Assuming patient_data is a DataFrame where each row is a patient
    # Convert to numpy array for similarity calculation
    input_vector = np.array(input_patient).reshape(1, -1)
    data_vectors = np.array(patient_data)
    
    # Calculate cosine similarity between input patient and all patients in the dataset
    similarity_scores = cosine_similarity(input_vector, data_vectors)
    return similarity_scores