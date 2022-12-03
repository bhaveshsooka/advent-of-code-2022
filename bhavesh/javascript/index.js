"use strict";

import { day1 } from "./aoc-2022/day-1-calorie-counting.js";
import { day2 } from "./aoc-2022/day-2-rock-paper-scissors.js";
import { day3 } from "./aoc-2022/day-3-rucksack-reorganization.js";

let answers = [];

await day1().then((answer) => answers.push(answer));
await day2().then((answer) => answers.push(answer));
await day3().then((answer) => answers.push(answer));

console.log(answers);
