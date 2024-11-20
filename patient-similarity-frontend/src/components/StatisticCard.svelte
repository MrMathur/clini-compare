<script>
  export let stat;
</script>

<div class="stat-card">
  <h3>{stat.value}</h3>
  <p>{stat.title}</p>
</div>

<style>
  .stat-card {
    flex: 1;
    margin: 0 0.5rem;
    padding: 1rem;
    background-color: #f0f0f0;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;

    min-width: 15rem;
    padding: 1rem;
    align-items: center;
    gap: 1rem;

    border-radius: 0.5rem;
    border: 1px solid #d9d9d9;
    background: #fff;
  }

  .stat-card h3 {
    margin: 0;
    color: #1e1e1e;
    text-align: center;
    font-family: Inter;
    font-size: 1.5rem;
    font-style: normal;
    font-weight: 600;
    line-height: 120%; /* 1.8rem */
    letter-spacing: -0.03rem;
  }

  .stat-card p {
    color: #1e1e1e;
    text-align: center;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;
    line-height: 140%; /* 1.4rem */
    margin: 0; /* Ensures no additional space */
  }
</style>
