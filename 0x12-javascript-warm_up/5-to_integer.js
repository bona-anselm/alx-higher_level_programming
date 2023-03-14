#!/usr/bin/node

const argPassed = Math.floor(Number(process.argv[2]));

if (isNaN(argPassed)) {
  console.log('Not a number');
} else {
  console.log('My number:', argPassed);
}
