<script>
  export let patient;
  import { currentPage, selectedPatient } from "../stores";
  import * as d3 from "d3"; // Import D3.js

  const DEFAULT_COLOR = "#003f5c";
  const MATCHING_COLOR = "#ffa600";
  const SELECTION_COLOR = "#bc5090";

  function goToCompareView() {
    selectedPatient.set(patient);
    currentPage.set("compare");
  }

  function formatSimilarityScore(num) {
    return (num).toFixed(2);
  }

  function addHighlight(event) {
    event.currentTarget.classList.add("highlight");
    d3.select(`#circle-${CSS.escape(patient.note_id)}`)
      .attr("r", "6")
      .style("fill", SELECTION_COLOR);
  }

  function removeHighlight(event) {
    event.currentTarget.classList.remove("highlight");
    d3.select(`#circle-${CSS.escape(patient.note_id)}`)
      .attr("r", "3")
      .style("fill", MATCHING_COLOR);
  }
</script>

<button
  on:click={goToCompareView}
  on:mouseenter={addHighlight}
  on:mouseleave={removeHighlight}
  class="contact-card"
  id={`button-${patient.note_id}`}
>
  <h2>{patient.note_id}</h2>
  <h3>Similarity Score: {formatSimilarityScore(patient.similarity)}</h3>
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
    transition: all 0.3s ease; /* Smooth transition for highlight */
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

  .contact-card.highlight {
    background: #f0f0f0; /* Example highlight background */
    border-color: #1e90ff; /* Example highlight border color */
    transform: scale(1.02); /* Slight scale effect */
  }
</style>
