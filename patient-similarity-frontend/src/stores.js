// src/stores.js
import { writable } from "svelte/store";

// Create a writable store with an initial value
export const currentPage = writable("input"); // 'home' can be your initial page
