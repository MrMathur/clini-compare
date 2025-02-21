import { writable } from "svelte/store";

export const currentPage = writable("input");
export const selectedPatient = writable(null);
export const loadState = writable(false);
export const highlightedPatients = writable([]);
