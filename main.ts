// One Star, Written in Sap — make.fun entry
// Writes a single one-line 1-star houseplant review to /output/entry.txt.
// Node 22+, stdlib only. Deterministic: the same line every run.

import { mkdirSync, writeFileSync } from "node:fs";

// A pothos, reviewing the human who owns it: watered with leftover iced
// coffee, kept in a pot with no drainage hole, and introduced to guests
// as "thriving" while it drowns. One line, no trailing newline, so the
// file holds exactly the review the gate measures.
const REVIEW =
  "One star. My owner waters me with leftover iced coffee, keeps me in a pot with no drainage hole, and tells guests I'm thriving while I quietly drown in caffeine and denial.";

mkdirSync("/output", { recursive: true });
writeFileSync("/output/entry.txt", REVIEW, "utf8");
