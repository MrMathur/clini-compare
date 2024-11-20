<script>
  export let patient;
  import { currentPage, selectedPatient } from "../stores";

  function goToCompareView() {
    selectedPatient.set(patient);
    currentPage.set("compare");
  }
</script>

<button on:click={goToCompareView} class="contact-card">
  <h2>{patient.note_id}</h2>
  <h3>Similarity Score: {patient.similarity}</h3>
  <div>
    <p>{patient.text}</p>
  </div>
</button>

<style>
  .contact-card {
    display: flex;
    min-width: 18.75rem;
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
    flex: 1 0 0;
    max-height: 12rem;

    border-radius: 0.5rem;
    border: 1px solid #d9d9d9;
    background: #fff;
  }

  .contact-card h2 {
    margin: 0 0 0.1rem;

    color: #1e1e1e;
    font-size: 1.5rem;
    font-style: normal;
    font-weight: 600;
    line-height: 120%; /* 1.8rem */
    letter-spacing: -0.03rem;
  }

  .contact-card h3 {
    color: #757575;
    font-size: 1rem;
    font-style: normal;
    font-weight: 600;
    line-height: 140%; /* 1.4rem */
  }

  .contact-card p {
    margin: 0.1rem 0;
    text-align: left;
    color: #b3b3b3;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;
    line-height: 140%; /* 1.4rem */
  }

  .contact-card div {
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>
