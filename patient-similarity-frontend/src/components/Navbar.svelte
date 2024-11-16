<script>
  import { currentPage } from "../stores";

  function goToDatabase() {
    currentPage.set("dashboard");
  }

  function createNewPatient() {
    currentPage.set("input");
  }
</script>

<nav class="navbar">
  <div class="logo">CliniCompare</div>
  <div class="nav-buttons">
    {#if $currentPage != "input" && $currentPage != "dashboard"}
      <button on:click={goToDatabase}>Database</button>
    {/if}
    {#if $currentPage != "input"}
      <button on:click={createNewPatient}>New Patient Note</button>
    {/if}
  </div>
</nav>

<style>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: #f8f9fa; /* Adjust as needed */
    top: 0;
    width: 100%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    z-index: 1000;
  }

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
  }

  .nav-buttons {
    display: flex;
    gap: 1rem;
  }

  button {
    padding: 0.5rem 1rem;
    border: none;
    cursor: pointer;
    background-color: #007bff; /* Adjust button color */
    color: #fff;
    border-radius: 5px;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>
