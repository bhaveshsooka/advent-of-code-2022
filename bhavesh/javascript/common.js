"use strict";

import axios from "axios";
import { config } from 'dotenv';

config()
let cookie = process.env.COOKIE;

export function getQuestionData(url) {
  return axios.get(url, {
    headers: {
      Accept: "application/json",
      Cookie: cookie,
    },
  });
}

export function sumAndMax(array, delimiter) {
  let sum = 0;
  let max = -1;
  array.forEach((item) => {
    if (item === delimiter) {
      if (sum > max) {
        max = sum;
      }
      sum = 0;
    } else {
      let calories = Number.parseInt(item);
      sum += calories;
    }
  });

  return max;
}

export function sumTopThree(array, delimiter) {
  let sum = 0;
  let maxes = [];
  array.forEach((item) => {
    if (item === delimiter) {
      maxes.push(sum);
      sum = 0;
    } else {
      let calories = Number.parseInt(item);
      sum += calories;
    }
  });

  let sorted = maxes.sort((a, b) => b - a);

  return sorted[0] + sorted[1] + sorted[2];
}
