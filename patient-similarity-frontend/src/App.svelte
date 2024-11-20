<script>
  import { currentPage } from "./stores";

  import Navbar from "./components/Navbar.svelte";
  import Input from "./lib/Input.svelte";
  import Dashboard from "./lib/Dashboard.svelte";
  import Compare from "./lib/Compare.svelte";
  import Loading from "./lib/Loading.svelte";
</script>

<main>
  <Navbar />

  <Loading />

  {#if $currentPage === "input"}
    <Input />
  {:else if $currentPage === "dashboard"}
    <Dashboard />
  {:else if $currentPage === "compare"}
    <Compare />
  {/if}
</main>

<style>
  main {
    padding: none;
    margin: none;
    display: flex;
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
</style>
