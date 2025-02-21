<script>
  import { currentPage, selectedPatient, loadState } from "../stores";
  let clinicalNote = ""; 
  let defaultNote =
    "EXAMINATION: Thoracentesis\n\nINDICATION: ___ year old patient with pleural effusion, persistent despite diuretic therapy. // Please perform thoracentesis and follow post-procedure protocol with albumin administration as needed.\n\nTECHNIQUE: Ultrasound-guided therapeutic thoracentesis\n\nCOMPARISON: Thoracentesis performed on ___.\n\nFINDINGS:\nLimited grayscale ultrasound imaging of the chest revealed a significant pleural effusion. The deepest accessible pocket in the right lower hemithorax was identified and selected for fluid aspiration.\n\nPROCEDURE:\nThe procedure, along with its risks, benefits, and potential alternatives, was explained to the patient, and written informed consent was obtained.\nA pre-procedure time-out was conducted to confirm the planned procedure, verify the patient’s identity with three identifiers, and review a checklist according to ___ protocol.\nWith ultrasound guidance, the skin entry point was determined and the area was prepped and draped in a standard sterile manner. Local anesthesia was achieved with 1% lidocaine.\nA ___ gauge catheter was inserted into the largest pocket in the right hemithorax, and approximately 1.5 L of clear, straw-colored fluid was aspirated, consistent with prior imaging findings.\nThe patient tolerated the procedure well without any immediate complications. Estimated blood loss was negligible.\nDr. ___ directly supervised the trainee during the critical aspects of the procedure and confirmed agreement with the trainee’s assessment and findings.\n\nIMPRESSION:\n\nApproximately 1.5 L of clear, straw-colored pleural fluid was removed from the right hemithorax without any complications.";

  selectedPatient.set(null);

  let selectedModel = 'all-MiniLM-L6-v2';

  function loadDemoData() {
    clinicalNote = defaultNote;
  }

  async function sendPatientData(variableToSend) {
    loadState.set(true);
    try {
      const response = await fetch("http://localhost:5001/post-input-note", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input_note: variableToSend }),
      });

      const result = await response.json();
      loadState.set(false);
      currentPage.set("dashboard");
    } catch (error) {
      console.error("Error sending data:", error);
    }
  }

  function findSimilarPatients() {
    if (clinicalNote == "") {
      alert("Clinical Note cannot be empty!");
    } else {
      sendPatientData(clinicalNote);
    }
  }
</script>

<div class="form-container">
  <div class="text-area-field">
    <label for="clinical-note">Clinical Note</label>
    <textarea
      id="clinical-note"
      bind:value={clinicalNote}
      placeholder="Enter clinical note here..."
    ></textarea>
  </div>

  <div class="button-container">
    <button class="tertiary" on:click={loadDemoData}>Load Demo Data</button>

    <select bind:value={selectedModel} class="model-dropdown">
      <option value="all-MiniLM-L6-v2">all-MiniLM-L6-v2</option>
      <option value="ClinicalBERT">ClinicalBERT</option>
      <option value="BioSentVec">BioSentVec</option>
    </select>

    <button class="primary" on:click={findSimilarPatients}
      >Find Similar Patients</button
    >
  </div>
</div>

<style>
  .form-container {
    display: flex;
    min-width: 20rem;
    padding: 1rem;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    flex: 1 0 0;
    align-self: stretch;
  }

  .text-area-field {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
    flex: 1 0 0;
    align-self: stretch;
  }

  label {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
    align-self: stretch;

    color: #1e1e1e;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;
    line-height: 140%; /* 1.4rem */
  }

  textarea {
    flex-grow: 1;
    width: 100%;
    resize: none;
    padding: 1rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .button-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 1rem;
    align-self: stretch;
  }

  button {
    display: flex;
    padding: 0.5rem 2rem;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    border-radius: 0.5rem;
  }
</style>
