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
  <!-- <div class="nav-pill-list"></div> -->
  <div class="nav-buttons">
    {#if $currentPage != "input" && $currentPage != "dashboard"}
      <button class="secondary" on:click={goToDatabase}>Database</button>
    {/if}
    {#if $currentPage != "input"}
      <button class="primary" on:click={createNewPatient}>New Patient Note</button>
    {/if}
  </div>
</nav>

<style>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center; /* Vertically centers items */
    padding: 1rem;
    top: 0;
    width: 100%;
    border-bottom: 1px solid #d9d9d9;
    background: #ffffff;
    flex-shrink: 0;
  }

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    margin-left: 20px; /* Adds 20px space to the left */
  }

  .nav-buttons {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-right: 20px; /* Adds 20px space to the right */
  }

  button {
    display: flex;
    padding: 0.5rem;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    border-radius: 0.5rem;
    cursor: pointer;
  }
</style>
