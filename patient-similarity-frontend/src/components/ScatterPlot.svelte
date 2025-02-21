<script>
  import { onMount, onDestroy } from "svelte"; // Import onMount lifecycle function
  import * as d3 from "d3"; // Import D3.js
  import { highlightedPatients } from "../stores";

  export let umapData;
  export let parsedPatients;

  const DEFAULT_COLOR = "#003f5c";
  const MATCHING_COLOR = "#ffa600";
  const SELECTION_COLOR = "#bc5090";

  function createUMAPScatterplot(data) {
    // Select the parent container's dimensions
    const container = d3.select("#scatterplot-container");
    const containerWidth = container.node().clientWidth || 800; // Default width
    const containerHeight = container.node().clientHeight || 600; // Default height

    const margin = { top: 20, right: 20, bottom: 30, left: 40 };
    const width = containerWidth - margin.left - margin.right;
    const height = containerHeight - margin.top - margin.bottom;

    // Remove any existing SVG (if rerendered)
    container.selectAll("*").remove();

    // Create responsive SVG
    const svg = container
      .append("svg")
      .attr("viewBox", `0 0 ${containerWidth} ${containerHeight}`) // Responsive scaling
      .attr("preserveAspectRatio", "xMinYMin meet") // Maintain aspect ratio
      .classed("responsive-svg", true);

    const plotGroup = svg
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    const xScale = d3
      .scaleLinear()
      .domain(d3.extent(data, (d) => d.x))
      .range([0, width]);

    const yScale = d3
      .scaleLinear()
      .domain(d3.extent(data, (d) => d.y))
      .range([height, 0]);

    const xAxis = d3.axisBottom(xScale);
    const yAxis = d3.axisLeft(yScale);

    plotGroup
      .append("g")
      .attr("transform", `translate(0,${height})`)
      .call(xAxis)
      .style("opacity", 0.5)
      .selectAll(".tick text")
      .remove();

    plotGroup
      .append("g")
      .call(yAxis)
      .style("opacity", 0.5)
      .selectAll(".tick text")
      .remove();

    // Extract the set of note_ids from parsedPatients
    const parsedNoteIds = new Set(parsedPatients.map((d) => d.note_id));

    // Separate data into matching and non-matching
    const matchingData = data.filter((d) => parsedNoteIds.has(d.note_id));
    const nonMatchingData = data.filter((d) => !parsedNoteIds.has(d.note_id));

    // Render non-matching circles first
    plotGroup
      .selectAll(".non-matching-circle")
      .data(nonMatchingData)
      .enter()
      .append("circle")
      .attr("class", "non-matching-circle")
      .attr("cx", (d) => xScale(d.x))
      .attr("cy", (d) => yScale(d.y))
      .attr("r", 1)
      .style("fill", d => DEFAULT_COLOR)
      .style("opacity", 0.075);

    // Render matching circles on top
    plotGroup
      .selectAll(".matching-circle")
      .data(matchingData)
      .enter()
      .append("circle")
      .attr("class", "matching-circle")
      .attr("cx", (d) => xScale(d.x))
      .attr("cy", (d) => yScale(d.y))
      .attr("r", 3) // Slightly larger for emphasis
      .style("fill", MATCHING_COLOR)
      .style("opacity", 0.75)
      .attr("id", (d) => `circle-${d.note_id}`) // Add unique id to each circle
      .on("mouseover", function (event, d) {
        // Increase the circle radius
        d3.select(this)
          .transition()
          .duration(200) // Smooth transition
          .attr("r", 6) // Set the radius to 6
          .style("fill", SELECTION_COLOR);

        // Highlight the corresponding button
        const button = document.getElementById(`button-${d.note_id}`);
        if (button) {
          button.classList.add("highlight"); // Add a highlight class to the button
        }
      })
      .on("mouseout", function (event, d) {
        // Reset the circle radius
        d3.select(this)
          .transition()
          .duration(200) // Smooth transition
          .attr("r", 3) // Reset the radius to its original size
          .style("fill", MATCHING_COLOR);

        // Remove the highlight from the button
        const button = document.getElementById(`button-${d.note_id}`);
        if (button) {
          button.classList.remove("highlight");
        }
      });
  }

  onMount(() => {
    createUMAPScatterplot(umapData);
    window.addEventListener("resize", () => createUMAPScatterplot(umapData)); // Re-render on window resize
  });

  // Cleanup the resize listener on unmount
  onDestroy(() => {
    window.removeEventListener("resize", () => createUMAPScatterplot(umapData));
  });
</script>

<div id="scatterplot-container"></div>

<style>
  #scatterplot-container {
    border: 1px;
    padding: 1 rem;
    width: 100%;
    height: 100%;
  }

  .responsive-svg {
    width: 100%;
    height: 100%;
  }

  .tick {
    opacity: 0.5;
  }
</style>
