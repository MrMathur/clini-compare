<script>
  export let patient;
  import { currentPage, selectedPatient } from "../stores";

  function goToCompareView() {
    selectedPatient.set(patient);
    currentPage.set("compare");
  }
</script>

<button on:click={goToCompareView} class="contact-card">
  <h3>{patient.note_id}</h3>
  <p>Similarity Score: {patient.similarity}</p>
  <p>Note: {patient.text}</p>
</button>

<style>
  .contact-card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    margin-bottom: 1rem;
    background-color: #f9f9f9;
    text-align: left;
    width: 100%;
  }

  .contact-card h3 {
    margin: 0 0 0.5rem;
  }

  .contact-card p {
    margin: 0.2rem 0;
  }
</style>
