#!/usr/bin/node

function incrementAndCall (number, theFunction) {
  number++;
  theFunction(number);
}
console.log(incrementAndCall);
