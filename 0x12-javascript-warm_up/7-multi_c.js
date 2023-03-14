#!/usr/bin/node

const argCount = Number(process.argv[2]);
const myString = 'C is fun';

if (isNaN(argCount)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argCount; i++) {
    console.log(myString);
  }
}
