#!/usr/bin/node
'use strict';
let x = Number(process.argv[2]);
function factorialize (x) {
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * factorialize(x - 1));
  }
}
console.log(factorialize(x));
