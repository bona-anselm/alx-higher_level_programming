#!/usr/bin/node

const argPassed = Number(parseInt(process.argv[2]));
//const argConverted = parseInt(argPassed[2]);

if (isNaN(Math.floor(argPassed))) {
  console.log('Not a Number');
} else {
  console.log('My number:', argPassed);
}
