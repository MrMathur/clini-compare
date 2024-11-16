<script>
  export let contact;
  import { currentPage } from "../stores";

  function goToCompareView() {
    currentPage.set("compare");
  }
</script>

<button on:click={goToCompareView} class="contact-card">
  <h3>{contact.name}</h3>
  <p>Disease: {contact.phone}</p>
  <p>Note: {contact.email}</p>
</button>

<style>
  .contact-card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    margin-bottom: 1rem;
    background-color: #f9f9f9;
    text-align: left;
    width: 100%;
  }

  .contact-card h3 {
    margin: 0 0 0.5rem;
  }

  .contact-card p {
    margin: 0.2rem 0;
  }
</style>
