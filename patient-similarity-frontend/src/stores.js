import { writable } from "svelte/store";

export const currentPage = writable("input");
export const selectedPatient = writable(null);
