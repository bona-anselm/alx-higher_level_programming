#!/usr/bin/node

const argPassed = Math.floor(Number(parseInt(process.argv[2])));
// const argConverted = parseInt(argPassed[2]);

if (isNaN(argPassed)) {
  console.log('Not a Number');
} else {
  console.log(`My number: ${argPassed}`);
}
