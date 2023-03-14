#!/usr/bin/node

const argPassed = process.argv;
const argConverted = parseInt(argPassed[2]);

if (isNaN(Math.floor(argConverted))) {
  console.log('Not a Number');
} else {
  console.log('My number:', argConverted);
}
