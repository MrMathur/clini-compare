<script>
  import { onMount, onDestroy } from "svelte"; // Import onMount lifecycle function
  import { highlightedPatients } from "../stores";
  import * as d3 from "d3"; // Import D3.js
  export let similarity_histogram;

  const DEFAULT_COLOR = "#003f5c";
  const MATCHING_COLOR = "#ffa600";
  const SELECTION_COLOR = "#bc5090";

  function createHistogram(data) {
    // Select parent container size
    const container = d3.select("#chart-container");
    const width = container.node().clientWidth;
    const height = container.node().clientHeight;
    const margin = { top: 20, right: 30, bottom: 40, left: 50 };
    const svgWidth = width - margin.left - margin.right;
    const svgHeight = height - margin.top - margin.bottom;

    // Remove any existing SVG (if rerendered)
    container.selectAll("*").remove();

    // Create SVG
    const svg = d3
      .select("#chart-container")
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    // X Scale
    const xScale = d3
      .scaleLinear()
      .domain([d3.min(data, (d) => d.bin.mid), d3.max(data, (d) => d.bin.mid)])
      .range([0, svgWidth]);

    // Y Scale (Logarithmic)
    const yScale = d3
      .scaleLog()
      .domain([1, d3.max(data, (d) => Math.max(1, d.similarity_count))]) // Avoid zero values
      .nice()
      .range([svgHeight, 0]);

    // // X Axis
    // svg
    //   .append("g")
    //   .attr("transform", `translate(0,${svgHeight})`)
    //   .call(d3.axisBottom(xScale).ticks(5))
    //   .style("opacity", 0.5)
    //   .selectAll(".tick text")
    //   .remove();

    // Add x-axis labels
    svg
      .append("text")
      .attr("x", 0) // Align left
      .attr("y", svgHeight + 30) // Position below axis
      .attr("text-anchor", "start")
      .style("font-size", "14px")
      .style("fill", "black")
      .text("Less Similar");

    svg
      .append("text")
      .attr("x", svgWidth) // Align right
      .attr("y", svgHeight + 30) // Position below axis
      .attr("text-anchor", "end")
      .style("font-size", "14px")
      .style("fill", "black")
      .text("More Similar");

    // // Y Axis
    // svg
    //   .append("g")
    //   .call(d3.axisLeft(yScale).ticks(5))
    //   .style("opacity", 0.5)
    //   .selectAll(".tick text")
    //   .remove();

    // Create a tooltip
    const tooltip = container
      .append("div")
      .style("position", "absolute")
      .style("background", "white")
      .style("border", "1px solid #ccc")
      .style("padding", "5px 10px")
      .style("border-radius", "5px")
      .style("font-size", "12px")
      .style("visibility", "hidden")
      .style("pointer-events", "none")
      .style("box-shadow", "0px 0px 5px rgba(0,0,0,0.3)");

    // Draw bars
    svg
      .selectAll(".bar")
      .data(data)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", (d) => xScale(d.bin.mid) - svgWidth / data.length / 2)
      .attr("y", (d) => yScale(d.similarity_count))
      .attr("width", svgWidth / data.length) // Adjust bar width
      .attr("height", (d) => svgHeight - yScale(d.similarity_count))
      .attr("fill", (d, i) =>
        i === data.length - 1 ? MATCHING_COLOR : DEFAULT_COLOR
      )
      .on("mouseover", function (event, d) {
        d3.select(this).attr("fill", MATCHING_COLOR); // Highlight color on hover
        tooltip
          .style("visibility", "visible")
          .html(`Count: ${d.similarity_count}`)
          .style("top", `${event.pageY - 30}px`)
          .style("left", `${event.pageX + 10}px`);

        highlightedPatients.set(d.note_ids);
      })
      .on("mousemove", function (event) {
        tooltip
          .style("top", `${event.pageY - 30}px`)
          .style("left", `${event.pageX + 10}px`);
      })
      .on("mouseout", function () {
        d3.select(this).attr("fill", (d, i) =>
          i === data.length - 1 ? MATCHING_COLOR : DEFAULT_COLOR
        ); // Revert color on hover out
        tooltip.style("visibility", "hidden");

        highlightedPatients.set([]);
      });
  }

  onMount(() => {
    createHistogram(similarity_histogram);
    window.addEventListener("resize", () =>
      createHistogram(similarity_histogram)
    ); // Re-render on window resize
  });

  // Cleanup the resize listener on unmount
  onDestroy(() => {
    window.removeEventListener("resize", () =>
      createHistogram(similarity_histogram)
    );
  });
</script>

<div></div>

<style>
</style>
