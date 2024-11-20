<script>
    import { loadState } from "../stores";
</script>

{#if $loadState}
  <div class="overlay">
    <div class="spinner"></div>
  </div>
{/if}

<style>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(
      255,
      255,
      255,
      0.8
    ); /* Adjust opacity and color as needed */
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000; /* High z-index to cover other elements */
  }

  .spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #000; /* Change color as needed */
    border-radius: 50%;
    width: 40px; /* Adjust size as needed */
    height: 40px; /* Adjust size as needed */
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>
