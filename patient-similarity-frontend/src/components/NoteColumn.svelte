<script>
  export let title;
  export let type;
  export let note;
  export let right_border;
</script>

<div class={right_border ? "column right-border" : "column"}>
  <div>
    <h1>{title}</h1>
    <h2>{type}</h2>
    <br />
    <p>{note}</p>
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
</style>
