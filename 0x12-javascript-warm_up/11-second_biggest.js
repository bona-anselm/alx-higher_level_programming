#!/usr/bin/node

const args = process.argv.splice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const numArgs = args.map(num => parseInt(num));

  let maxNumber = -Infinity;
  let secondMaxNumber = -Infinity;

  for (let i = 0; i < numArgs.length; i++) {
    if (numArgs[i] > maxNumber) {
      secondMaxNumber = maxNumber;
      maxNumber = numArgs[i];
    } else if (numArgs[i] > secondMaxNumber && numArgs[i] !== maxNumber) {
      secondMaxNumber = numArgs[i];
    }
  }
  if (secondMaxNumber === -Infinity) {
    console.log(0);
  } else {
    console.log(secondMaxNumber);
  }
}
