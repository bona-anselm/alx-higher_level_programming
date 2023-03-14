#!/usr/bin/node

const argCount = process.argv;

if (argCount[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argCount[2]);
}
  

