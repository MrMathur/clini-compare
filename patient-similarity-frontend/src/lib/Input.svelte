<script>
  import { currentPage } from "../stores";
  let clinicalNote = ""; // Bind this variable to the textarea to capture input
  let defaultNote =
    "EXAMINATION: Thoracentesis\nINDICATION: ___ year old patient with pleural effusion, persistent despite diuretic therapy. // Please perform thoracentesis and follow post-procedure protocol with albumin administration as needed.\nTECHNIQUE: Ultrasound-guided therapeutic thoracentesis\nCOMPARISON: Thoracentesis performed on ___.\nFINDINGS:\nLimited grayscale ultrasound imaging of the chest revealed a significant pleural effusion. The deepest accessible pocket in the right lower hemithorax was identified and selected for fluid aspiration.\nPROCEDURE:\nThe procedure, along with its risks, benefits, and potential alternatives, was explained to the patient, and written informed consent was obtained.\nA pre-procedure time-out was conducted to confirm the planned procedure, verify the patient’s identity with three identifiers, and review a checklist according to ___ protocol.\nWith ultrasound guidance, the skin entry point was determined and the area was prepped and draped in a standard sterile manner. Local anesthesia was achieved with 1% lidocaine.\nA ___ gauge catheter was inserted into the largest pocket in the right hemithorax, and approximately 1.5 L of clear, straw-colored fluid was aspirated, consistent with prior imaging findings.\nThe patient tolerated the procedure well without any immediate complications. Estimated blood loss was negligible.\nDr. ___ directly supervised the trainee during the critical aspects of the procedure and confirmed agreement with the trainee’s assessment and findings.\nIMPRESSION:\nApproximately 1.5 L of clear, straw-colored pleural fluid was removed from the right hemithorax without any complications.";
  function loadDemoData() {
    clinicalNote = defaultNote; // Add any default demo text you want
  }

  function findSimilarPatients() {
    currentPage.set("dashboard");
  }
</script>

<div class="form-container">
  <label for="clinical-note">Clinical Note</label>
  <textarea
    id="clinical-note"
    bind:value={clinicalNote}
    placeholder="Enter clinical note here..."
  ></textarea>

  <div class="button-container">
    <button on:click={loadDemoData}>Load Demo Data</button>
    <button on:click={findSimilarPatients}>Find Similar Patients</button>
  </div>
</div>

<style>
  .form-container {
    display: flex;
    flex-direction: column;
    height: 90vh;
    padding: 2rem;
  }

  label {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
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
    gap: 1rem;
    margin-top: 1rem;
  }

  button {
    padding: 0.5rem 1.5rem;
    border: none;
    cursor: pointer;
    background-color: #007bff; /* Primary button color */
    color: #fff;
    border-radius: 5px;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>
