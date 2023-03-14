#!/usr/bin/node

const executeXTimes = (x, theFunction) => {
  let iteration = 0;

  while (iteration < x) {
    theFunction();
    iteration++;
  }
};
console.log(executeXTimes);
