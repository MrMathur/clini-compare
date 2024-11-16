<script>
  import PatientCard from "../components/PatientCard.svelte";
  import StatisticCard from "../components/StatisticCard.svelte";
  import ScatterPlot from "../components/ScatterPlot.svelte";
  // Sample data for contact cards
  let contacts = [
    { name: "John Doe", phone: "123-456-7890", email: "john.doe@example.com" },
    {
      name: "Jane Smith",
      phone: "987-654-3210",
      email: "jane.smith@example.com",
    },
    {
      name: "Alice Johnson",
      phone: "555-123-4567",
      email: "alice.johnson@example.com",
    },
  ];

  // Sample data for aggregate statistics
  let stats = [
    { title: "h-index", value: "79" },
    { title: ">90% similarity", value: "4" },
    { title: "Cluster Average", value: "82%" },
  ];
</script>

<div class="dashboard">
  <!-- Left Column for D3 Visualization -->
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

  <!-- Right Column for Contact Cards -->
  <div class="right-column">
    <h2>Most Similar Patients</h2>
    {#each contacts as contact (contact.name)}
      <PatientCard {contact} />
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
