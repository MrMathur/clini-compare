<script>
  import PatientCard from "../components/PatientCard.svelte";
  import StatisticCard from "../components/StatisticCard.svelte";
  import ScatterPlot from "../components/ScatterPlot.svelte";
  import { currentPage, loadState } from "../stores";
  let showLeftCol = true;
  // Sample data for contact cards
  let parsedPatients = [];

  // Sample data for aggregate statistics
  let stats = [
    { title: "h-index", value: "79" },
    { title: ">90% similarity", value: "4" },
    { title: "Cluster Average", value: "82%" },
  ];

  // Function to fetch the variable from Flask
  async function get_similar_patients() {
    loadState.set(true);
    try {
      const response = await fetch(
        "http://localhost:5001/get-similar-patients"
      ); // Adjust the port if different
      const data = await response.json();
      parsedPatients = JSON.parse(data.similarPatients);
      loadState.set(false);
      console.timeEnd('debug');
    } catch (error) {
      console.error("Error fetching variable:", error);
    }
  }

  console.time('debug');
  get_similar_patients();
</script>

<div class="dashboard">
  <!-- Left Column for D3 Visualization -->
  {#if showLeftCol}
    <div class="left-column">
      <!-- Add your D3 visualization setup here later -->
      <div class="d3-container">
        <!-- Top Section: Aggregate Statistics -->
        <!-- <div class="stats-section">
          {#each stats as stat}
            <StatisticCard {stat} />
          {/each}
        </div> -->
        <ScatterPlot />
      </div>
    </div>
  {/if}

  <!-- Right Column for Contact Cards -->
  <div class="right-column">
    <h1>Most Similar Patients</h1>
    <h2>Top 5 cosine similarity</h2>
    {#each parsedPatients as patient (patient.subject_id)}
      <PatientCard {patient} />
    {/each}
  </div>
</div>

<style>
  .dashboard {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex: 1 0 0;
    align-self: stretch;
    height: 90%;
  }

  .left-column {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.4375rem;
    flex: 1 0 0;
    align-self: stretch;
  }

  .right-column {
    display: flex;
    width: 30.375rem;
    padding: var(--sds-size-space-0) var(--sds-size-space-1600);
    flex-direction: column;
    align-items: flex-start;
    gap: var(--sds-size-space-1200);
    align-self: stretch;
    border-left: 1px solid #d9d9d9;
    padding: 1rem;
    height: 100%;
    overflow: scroll;
  }
  .d3-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
  }

  .stats-section {
    display: flex;
    justify-content: space-between;
    padding: 1rem;
    border-bottom: 1px solid #e1e1e1;
  }

  .right-column h1 {
    color: #1e1e1e;
    font-size: 1.5rem;
    font-style: normal;
    font-weight: 600;
    letter-spacing: -0.03rem;
  }

  .right-column h2 {
    color: #757575;
    font-size: 1.25rem;
    font-style: normal;
    font-weight: 400;
    line-height: 120%; /* 1.5rem */
  }
</style>
