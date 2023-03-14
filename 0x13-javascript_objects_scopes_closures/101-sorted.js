#!/usr/bin/node

const dict = require('./101-data.js');
const userIdsByOccurrence = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (userIdsByOccurrence.hasOwnProperty(occurrence)) {
    userIdsByOccurrence[occurrence].push(Number(userId));
  } else {
    userIdsByOccurrence[occurrence] = [Number(userId)];
  }
}

console.log(userIdsByOccurrence);
