<script>
  export let title;
  export let type;
  export let note;
  export let right_border;
  export let common_words; // List of words to highlight

  const HIGHLIGHT_COLOR = "rgba(255, 166, 0, 0.5)";

  // Function to highlight words in the note
  function highlightWords(text, wordsToHighlight) {
    if (!text || wordsToHighlight.length === 0) {
      return text; // Return original text if no words to highlight
    }

    // Extract just the words from the objects
    const words = wordsToHighlight.map((obj) => obj.word);

    // Create a regex to match the words to highlight (case-insensitive)
    const regex = new RegExp(`\\b(${words.join("|")})\\b`, "gi");

    // Replace matching words with highlighted HTML
    return text.replace(
      regex,
      (match) =>
        `<span style="background-color: ${HIGHLIGHT_COLOR}; padding: 0.1rem;">${match}</span>`
    );
  }
</script>

<div class={right_border ? "column right-border" : "column"}>
  <div>
    <h1>{title}</h1>
    <h2>{type}</h2>
    <!-- <br /> -->
    <!-- Use @html to render the highlighted HTML safely -->
    {#if type != "Discharge Note"}
      <p>{@html highlightWords(note, common_words)}</p>
    {:else}
      <p>{note}</p>
    {/if}
  </div>
</div>

<style>
  .column {
    padding: 1rem;
    border-radius: 8px;
    overflow-y: hidden;
    margin: 0;

    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    align-self: stretch;
    flex: 1;
  }

  .right-border {
    border-right: 1px solid #e1e1e1;
  }

  .column h1 {
    color: #1e1e1e;
    font-size: 1.5rem;
    font-style: normal;
    font-weight: 600;
    line-height: 120%; /* 1.8rem */
    letter-spacing: -0.03rem;
  }

  .column h2 {
    color: #757575;
    font-size: 1.25rem;
    font-style: normal;
    font-weight: 400;
    line-height: 120%; /* 1.5rem */
  }

  .column p {
    white-space: pre-wrap; /* This preserves newlines and white spaces */
    color: #1e1e1e;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;
    line-height: 140%; /* 1.4rem */
  }

  /* Highlighted word style */
  .highlight {
    background-color: yellow;
    font-weight: bold;
  }
</style>
