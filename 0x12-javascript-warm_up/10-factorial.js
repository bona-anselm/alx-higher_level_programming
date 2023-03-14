#!/usr/bin/node

const numArg = parseInt(process.argv[2]);

function factorial (numArg) {
  if (isNaN(numArg) || numArg === 0) {
    return 1;
  } else {
    return numArg * factorial(numArg - 1);
  }
}
console.log(factorial(numArg));
