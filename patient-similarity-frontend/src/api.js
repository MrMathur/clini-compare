// src/api.js
export async function fetchSimilarity(inputPatient) {
    try {
        const response = await fetch("http://127.0.0.1:5000/similarity", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ input_patient: inputPatient }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch similarity data");
        }

        const data = await response.json();
        
        return data;
    } catch (error) {
        console.error("Error fetching similarity data:", error);
        return null;
    }
}