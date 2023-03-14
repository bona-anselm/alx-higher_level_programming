#!/usr/bin/node

const argsPassedLength = process.argv.length - 2;
const argsPassed = process.argv;

if (argsPassedLength === 2) {
  console.log(`${argsPassed[2]} is ${argsPassed[3]}`);
} else if (argsPassedLength === 1) {
  console.log(`${argsPassed[2]} is ${argsPassed[3]}`);
} else {
  console.log(`${argsPassed[2]} is ${argsPassed[3]}`);
}
