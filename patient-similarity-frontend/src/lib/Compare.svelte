<script>
  import { onMount } from "svelte";
  import NoteColumn from "../components/NoteColumn.svelte";
  import { loadState, selectedPatient } from "../stores";

  let input_note = "";
  let patientData = null;
  let discharge_note = "";

  let common_words;

  const DUMMY_TEXT =
    `40792  11250484-DS-19    11250484  29769545        DS        19  2170-06-18 00:00:00  2170-06-19 13:27:00   \nName:  ___               Unit No:   ___\n \nAdmission Date:  ___              Discharge Date:   ___\n \nDate of Birth:  ___             Sex:   F\n \nService: MEDICINE\n \nAllergies: \nmetformin / Penicillins / lisinopril / erythromycin base / \nReglan / aspirin / Bactrim / doxycycline / Singulair / Insulins \n/ ___ Receptor Antagonist / nadolol\n \nAttending: ___\n \nChief Complaint:\ntransfer for consideration of TIPS\n \nMajor Surgical or Invasive Procedure:\nEGD on ___ ___\n\n \nHistory of Present Illness:\nMs. ___ is a ___ y/o female is a history of cirrhosis thought \nto be secondary to NASH vs. cryptogenic c/b previous varaceal \nbleeding s/p banding who initially presented to ___ \n___ on ___ with one week of abdominal pain and 4 episodes \nof hematemesis. She denied SOB, CP, or black/tarry stools, \nfever/chills.\n\nIn the ___, the patient had a large volume \nhematemesis with clots. She was given IV fluds, 2 units PRBCs, \noctreotide, and protonix gtt. She was then admitted to the ICU.\n\nOSH ICU course included an urgent EGD that showed grade III \nvaricies and patient had 5 bands placed with hemostasis \nachieved. She briefly required phenylephrine which was quickly \nweaned. She remained hemodynamically throughout the rest of her \ncourse. She was extubated on ___ at 10:30 AM. After extubation \nshe vomitted 15ml of blood  which included one band. She has had \nno further episodes of bleeding. She was also started on \nceftriaxone for SBP ppx. She was then transferred to ___ for \nconsideration of TIPS.\n\nOn arrival, the patient complained of hunger and ongoing diffuse \nabdominal pain. She states that the pain has been chronic for \nthe last year and is diffuse discomfort and bloating. The pain \nis intermittently worse and has been worse for the last 2 weeks. \nShe has no other complaints at that time. The patient also notes \nincreased ___ edema and weight over the last couple of weeks.\n\n \nPast Medical History:\n- ___ Cirrhosis complicated by esophageal/gastric varices with \nvariceal bleeding - ___\n- Diabetes.  She has been on insulin for the past ___ years.  \nHer recent A1c was 6.4.\n- Hypertension in the past, currently not taking \nantihypertensive medications.\n- Obesity with a BMI of 43.  She has not been obese in her \nentire life and has been gaining weight over the past few years.\n- History of fatty liver, prior to diagnosis of cirrhosis.\n- h/o Pneumonia.\n- Asthma.\n- Her last Pap was done in ___.\n- No prior history of cardiac disease or skin cancer or breast \ncancer.\n\n \nSocial History:\n___\nFamily History:\nOne of her brothers died from lymphoma, one from car accident \nand the other one from sudden onset death in infancy.  There is \nno known liver cancer or liver disease in her family.\n\n \nPhysical Exam:\n==================\nAdmission Exam\n==================\nVitals: T: 98.5 BP: 145/61 P: 94 R: 15 O2: 98% on 2L NC  \nGENERAL: Alert, oriented, no acute distress  \nHEENT: Sclera anicteric, MMM, oropharynx clear  \nNECK: supple, JVP not elevated though difficult to assess due to \nbody habitus, acanthosis nigricans  \nLUNGS: Clear to auscultation bilaterally, no wheezes, rales, \nrhonchi  \nCV: Regular rate and rhythm, normal S1 S2, no murmurs, rubs, \ngallops  \nABD: soft, obese, diffuse tenderness to palpation, \nnon-distended, bowel sounds present, no rebound tenderness or \nguarding\nEXT: Warm, well perfused, 2+ pulses, trace edema to ___ up shin \n\n===================\nDISCARGE EXAM:\n===================\nVITALS: 98.4, 109/60, 82, 18, 97RA, 982L when sleeping\nGeneral: obese woman, pleasant, NAD\nHEENT: MMM, oropharynx clear\nCV: rrr, normal s1/s2, no m/r/g\nLungs: CTAB, no wheezes, ronchi, crackles\nAbdomen: obese abdomen, no fluid wave, bs+, mildly tender to \npalpation diffusely, no rebound, no guarding\nExtremities: +1 pitting edema halfway up shins, warm, well \nperfused\nNeuro: AOX3, moving all extremities, no asterixis\n\n \nPertinent Results:\n=================\nAdmission Labs;\n=================\n___ 01:11AM BLOOD WBC-11.3*# RBC-3.54*# Hgb-11.0* \nHct-30.5*# MCV-86 MCH-31.2# MCHC-36.2*# RDW-16.7* Plt ___\n___ 04:08AM BLOOD ___ PTT-25.6 ___\n___ 04:08AM BLOOD Glucose-296* UreaN-19 Creat-0.7 Na-138 \nK-3.9 Cl-106 HCO3-25 AnGap-11\n___ 04:08AM BLOOD ALT-37 AST-38 AlkPhos-118* TotBili-0.8\n___ 04:08AM BLOOD Albumin-2.7* Calcium-7.7* Phos-2.0* \nMg-1.9\n___ 04:08AM BLOOD AFP-3.9\n\n===================\nDischarge labs:\n===================\n___ 06:45AM BLOOD WBC-5.9 RBC-3.38* Hgb-10.5* Hct-30.3* \nMCV-90 MCH-31.1 MCHC-34.7 RDW-17.3* Plt Ct-89*\n___ 06:45AM BLOOD ___ PTT-26.8 ___\n___ 06:45AM BLOOD Glucose-90 UreaN-12 Creat-0.6 Na-141 \nK-3.3 Cl-106 HCO3-26 AnGap-12\n___ 06:45AM BLOOD ALT-36 AST-39 AlkPhos-111* TotBili-0.6\n___ 06:45AM BLOOD Calcium-7.9* Phos-2.6* Mg-1.9\n___ 04:08AM BLOOD AFP-3.9\n\n================\nSTUDIES:\n================\n\nKUB ___\nIMPRESSION:  Normal bowel gas pattern. \n\nECHO ___\nConclusions  \nThe left atrium is mildly dilated. There is mild symmetric left \nventricular hypertrophy with normal cavity size and global \nsystolic function (LVEF>55%). Due to suboptimal technical \nquality, a focal wall motion abnormality cannot be fully \nexcluded. The right ventricular cavity is mildly dilated with \nnormal free wall contractility. The number of aortic valve \nleaflets cannot be determined. There is no aortic valve \nstenosis. The mitral valve leaflets are structurally normal. \nThere is no mitral valve prolapse. Physiologic mitral \nregurgitation is seen (within normal limits). There is mild \npulmonary artery systolic hypertension. There is an anterior \nspace which most likely represents a prominent fat pad.  \n\n \nBrief Hospital Course:\nMs. ___ is a ___ y/o female is a history of cirrhosis thought \nto be secondary to NASH vs. cryptogenic c/b varaceal bleeding \nwho initially presented to ___ with \nhematemesis found to have grade III varacies s/p banding and \ntransferred to ___ for evaluation of TIPS.\n\n# Variceal Bleed: h/o bleeding in ___ and ___ now with \nrecurrence of bleeding. initially presented to ___ \n___ with hematemesis found to have grade III varacies and \nhad 5 bands placed. Transferred to ___ ICU for evaluation of \nTIPS. Hemodynamically stable on arrival, no further episodes of \nbleeding. Pt continued on octreotide gtt and CTX for SBP ppx. Pt \ncalled out to the floor. Decision made to attempt scheduled \nrepeat bandings prior to considering a TIPS. Pt tolerated liquid \nthen solid diet. Octreotide stopped. H/H remained stable. \nCompleted 5 days of ceftriaxone. Discharged home with plan for \nliver follow up and scheduled repeat bandings. \n\n# Abdominal Discomfort: Patient reports chronic abdominal \npain(about a year) with intermitent worsening. Described as \ngeneralized bloating and discomfort. Exam with tenderness but no \nrebound or guarding. Differential includes SBP (bedside US with \nno clear pockets of ascites), constipation (though last BM \nyesterday), gas. KUB unremarkable. Abd US notable for \nsplenomegaly and patent hepatic vasculature thought limited \nstudy.\n\n# NASH vs cryptogenic cirrhosis c/b esophageal varices and \nbleeding ___, ___. At home is on \nfurosemide 40mg daily and aldactone 25mg daily. Initially held \ndiuretics ___ UGIB, but restarted prior to discharge. Not on \nbeta blocker at home as it is not tolerated due to asthma. AFP \n3.9 during hospitalization. Will follow up with Dr. ___ \nrepeat endoscopy and banding monthly until vessels resolve. \n\n# Diabetes: Last A1C 7.3% in ___. Given decreased doses \nwhile here. Transitioned to home insulin dose at time of \ndischarge. NPH 30U breakfast and 40U at night. Humalog 40 Units \nBreakfast, Humalog 40 Units Lunch, Humalog 40 Units Dinner. \n\n# Asthma: Given advair since symbicort is non-formulary. Given \nnebs. Continued on home medications on discharge: \nIpratropium-Albuterol Inhalation Spray 1 INH IH Q4H:PRN SOB, \nIpratropium-Albuterol Neb 1 NEB NEB Q6H:PRN SOB, Symbicort \n(budesonide-formoterol) 160-4.5 mcg/actuation inhalation BID.  \n\n=========================\nTRANSITIONAL ISSUES:\n=========================\n- Pt will need repeat endoscopies scheduled monthly for \nrebanding of varices until they are resolved\n- Should have repeat Chest XRAY PA/lateral at next follow up \napppointment to assess for resolution of LLL opaciy\n- H/H on discharge:10.5/30.3\n- Weight on discharge: 118.5kg\n- Pt unable to tolerate nadolol due to asthma\n- Full code\n\n \nMedications on Admission:\nThe Preadmission Medication list is accurate and complete.\n1. Ascorbic Acid ___ mg PO DAILY \n2. Symbicort (budesonide-formoterol) 160-4.5 mcg/actuation \ninhalation BID \n3. Vitamin D 1000 UNIT PO DAILY \n4. Cyanocobalamin 600 mcg PO DAILY \n5. Ferrous Sulfate 325 mg PO DAILY \n6. Furosemide 40 mg PO DAILY \n7. Humalog 40 Units Breakfast\nHumalog 40 Units Lunch\nHumalog 40 Units Dinner\nNPH 30 Units Breakfast\nNPH 40 Units Bedtime\n8. Ipratropium-Albuterol Inhalation Spray 1 INH IH Q4H:PRN SOB \n9. Ipratropium-Albuterol Neb 1 NEB NEB Q6H:PRN SOB \n10. Omeprazole 20 mg PO BID \n11. Spironolactone 25 mg PO DAILY \n\n \nDischarge Medications:\n1. Furosemide 40 mg PO DAILY \n2. Ipratropium-Albuterol Neb 1 NEB NEB Q6H:PRN SOB \n3. Spironolactone 25 mg PO DAILY \n4. Sucralfate 1 gm PO QID \n5. Ascorbic Acid ___ mg PO DAILY \n6. Cyanocobalamin 600 mcg PO DAILY \n7. Ferrous Sulfate 325 mg PO DAILY \n8. Ipratropium-Albuterol Inhalation Spray 1 INH IH Q4H:PRN SOB \n9. Symbicort (budesonide-formoterol) 160-4.5 mcg/actuation \ninhalation BID \n10. Vitamin D 1000 UNIT PO DAILY \n11. Humalog 40 Units Breakfast\nHumalog 40 Units Lunch\nHumalog 40 Units Dinner\nNPH 30 Units Breakfast\nNPH 40 Units Bedtime\n12. Omeprazole 20 mg PO BID \n13. Ciprofloxacin HCl 500 mg PO Q24H Duration: 2 Days \nRX *ciprofloxacin HCl [Cipro] 500 mg 1 tablet(s) by mouth daily \nDisp #*2 Tablet Refills:*0\n\n \nDischarge Disposition:\nHome\n \nDischarge Diagnosis:\nPRIMARY DIAGNOSIS:\nEsophageal Variceal bleed\n\nSECONDARY DIAGNOSIS:\n___ Cirrhosis\n\n \nDischarge Condition:\nMental Status: Clear and coherent.\nLevel of Consciousness: Alert and interactive.\nActivity Status: Ambulatory - Independent.\n\n \nDischarge Instructions:\nDear Ms. ___, \n\nIt was a pleasure taking care of ___ at ___. \n___ went to ___ after ___ vomited \nblood. ___ were found to have bleeding esophageal varices, which \nare big blood vessels in your esophagus that are caused by your \nliver disease. ___ had the varices banded and ___ improved. ___ \nwere transferred to ___ to be evaluated for a TIPS procedure. \nOnce at ___, we decided to opt for a more conservative \ntreatment and plan for repeat banding every month until the \nvessels went away. \n\n___ will need to follow up with Dr. ___ to make a time to \nhave your repeat endoscopies. ___ were started on new \nmedications to help prevent further episodes of bleeding. \n\nWe wish ___ the best of health, \n\nYour medical team at ___ \n \nFollowup Instructions:\n___\n
    `;

  onMount(() => {
    selectedPatient.subscribe((patient) => {
      patientData = patient;
    });

    get_input_note(patientData.subject_id);
  });

  function findTopCommonWords(str1, str2) {
    // Define a list of stop words
    const stopWords = new Set([
      "a",
      "an",
      "the",
      "and",
      "or",
      "but",
      "so",
      "of",
      "at",
      "by",
      "for",
      "with",
      "about",
      "against",
      "between",
      "into",
      "through",
      "during",
      "before",
      "after",
      "above",
      "below",
      "to",
      "from",
      "up",
      "down",
      "in",
      "out",
      "on",
      "off",
      "over",
      "under",
      "again",
      "further",
      "then",
      "once",
      "here",
      "there",
      "when",
      "where",
      "why",
      "how",
      "all",
      "any",
      "both",
      "each",
      "few",
      "more",
      "most",
      "other",
      "some",
      "such",
      "no",
      "nor",
      "not",
      "only",
      "own",
      "same",
      "than",
      "too",
      "very",
      "s",
      "t",
      "can",
      "will",
      "just",
      "don",
      "should",
      "now",
      "was"
    ]);

    // Helper function to tokenize and filter a string
    function tokenizeAndFilter(str) {
      return str
        .toLowerCase() // Convert to lowercase
        .match(/\b[a-z]+\b/g) // Match words only
        .filter((word) => !stopWords.has(word)); // Remove stop words
    }

    // Tokenize both strings
    const words1 = tokenizeAndFilter(str1);
    const words2 = tokenizeAndFilter(str2);

    // Count word frequencies in each string
    const countWords = (words) => {
      const freqMap = {};
      for (const word of words) {
        freqMap[word] = (freqMap[word] || 0) + 1;
      }
      return freqMap;
    };

    const freq1 = countWords(words1);
    const freq2 = countWords(words2);

    // Find common words and calculate their combined frequencies
    const commonWords = Object.keys(freq1)
      .filter((word) => word in freq2)
      .map((word) => ({ word, frequency: freq1[word] + freq2[word] }));

    // Sort by combined frequency in descending order and return the top 20
    return commonWords.sort((a, b) => b.frequency - a.frequency).slice(0, 20);
  }

  // Function to fetch the variable from Flask
  async function get_input_note(subject_id) {
    loadState.set(true);
    try {
      const response = await fetch("http://localhost:5001/post-discharge-note", {
        method: "POST", 
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({subject_id: subject_id}),
      }); // Adjust the port if different
      const data = await response.json();
      input_note = data.input_note; // Assign the fetched variable to the Svelte variable
      discharge_note = data.discharge_note;
      console.log(discharge_note);
      loadState.set(false);
      common_words = findTopCommonWords(input_note, patientData.text);
    } catch (error) {
      console.error("Error fetching variable:", error);
    }
  }
</script>

{#if patientData != null}
  <div class="three-columns">
    {#if input_note && common_words}
    <NoteColumn
      title="Input Note"
      type="Radiology Note"
      right_border={true}
      note={input_note}
      {common_words}
    />
    {/if}
    {#if patientData && common_words}
    <NoteColumn
      title={"Subject Id: " + patientData.subject_id}
      type="Radiology Note"
      right_border={false}
      note={patientData.text}
      {common_words}
    />
    {/if}
    <NoteColumn
      title="&nbsp"
      type="Discharge Note"
      right_border={false}
      note={discharge_note}
      common_words={null}
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
