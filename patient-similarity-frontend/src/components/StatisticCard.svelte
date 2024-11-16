<script>
  export let stat;
</script>

<div class="stat-card">
  <h3>{stat.title}</h3>
  <p>{stat.value}</p>
</div>

<style>
  .stat-card {
    flex: 1;
    margin: 0 0.5rem;
    padding: 1rem;
    background-color: #f0f0f0;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
  }

  .stat-card h3 {
    margin: 0;
    font-size: 1.2rem;
  }

  .stat-card p {
    font-size: 1.5rem;
    font-weight: bold;
    margin: 0; /* Ensures no additional space */
  }
</style>
