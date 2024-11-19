<script>
  import { onMount } from "svelte";
  import NoteColumn from "../components/NoteColumn.svelte";
  import { selectedPatient } from "../stores";

  let input_note = "";
  let patientData = null;

  const DUMMY_TEXT = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sequi quo ab necessitatibus repellat expedita eaque ad cumque quibusdam, impedit voluptatem sed mollitia recusandae nisi facere ipsum quasi distinctio veritatis qui?";

  onMount(() => {
    selectedPatient.subscribe((patient) => {
      patientData = patient;
    });
  });

  // Function to fetch the variable from Flask
  async function get_input_note() {
    try {
      const response = await fetch("http://localhost:5001/get-input_note"); // Adjust the port if different
      const data = await response.json();
      input_note = data.input_note; // Assign the fetched variable to the Svelte variable
    } catch (error) {
      console.error("Error fetching variable:", error);
    }
  }

  // Call the function when the component loads
  get_input_note();
</script>

{#if patientData != null}
  <div class="three-columns">
    <NoteColumn
      title="Input Note"
      type="Radiology Note"
      right_border={true}
      note={input_note}
    />
    <NoteColumn
      title={"Note Id: " + patientData.note_id}
      type="Radiology Note"
      right_border={false}
      note={patientData.text}
    />
    <NoteColumn
      title="&nbsp"
      type="Discharge Note"
      right_border={false}
      note={DUMMY_TEXT}
    />
  </div>
{/if}

<style>
  .three-columns {
    display: flex;
    justify-content: space-between;
    align-items: center;
    align-self: stretch;
  }
</style>
