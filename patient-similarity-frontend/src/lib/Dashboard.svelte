<script>
  import PatientCard from "../components/PatientCard.svelte";
  import StatisticCard from "../components/StatisticCard.svelte";
  import ScatterPlot from "../components/ScatterPlot.svelte";
  let showLeftCol = false;
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
    try {
      const response = await fetch(
        "http://localhost:5001/get-similar-patients"
      ); // Adjust the port if different
      const data = await response.json();
      parsedPatients = JSON.parse(data.similarPatients);
    } catch (error) {
      console.error("Error fetching variable:", error);
    }
  }

  // Call the function when the component loads
  get_similar_patients();
</script>

<div class="dashboard">
  <!-- Left Column for D3 Visualization -->
  {#if showLeftCol}
    <div class="left-column">
      <!-- Add your D3 visualization setup here later -->
      <div class="d3-container">
        <!-- Top Section: Aggregate Statistics -->
        <div class="stats-section">
          {#each stats as stat}
            <StatisticCard {stat} />
          {/each}
        </div>
        <ScatterPlot />
      </div>
    </div>
  {/if}

  <!-- Right Column for Contact Cards -->
  <div class="right-column">
    <h2>Most Similar Patients</h2>
    {#each parsedPatients as patient (patient.subject_id)}
      <PatientCard {patient} />
    {/each}
  </div>
</div>

<style>
  .dashboard {
    display: flex;
    height: 100vh;
  }

  .left-column,
  .right-column {
    padding: 1rem;
  }

  .left-column {
    flex: 2; /* Adjusts the width of the columns */
    border-right: 1px solid #ccc;
  }

  .right-column {
    flex: 1;
    overflow-y: auto; /* Allows scrolling if the list is long */
  }
  .d3-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    padding: 1rem;
  }

  .stats-section {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
  }
</style>
