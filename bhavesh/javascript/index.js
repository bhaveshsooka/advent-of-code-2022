"use strict";

import { day1 } from "./aoc-2022/day-1-calorie-counting.js";
import { day2 } from "./aoc-2022/day-2-rock-paper-scissors.js";
import { day3 } from "./aoc-2022/day-3-rucksack-reorganization.js";
import { day4 } from "./aoc-2022/day-4-camp-cleanup.js";
import { day5 } from "./aoc-2022/day-5-supply-stacks.js";

let answers = [];

await day1().then((answer) => answers.push(answer));
await day2().then((answer) => answers.push(answer));
await day3().then((answer) => answers.push(answer));
await day4().then((answer) => answers.push(answer));
await day5().then((answer) => answers.push(answer));

console.log(answers);
