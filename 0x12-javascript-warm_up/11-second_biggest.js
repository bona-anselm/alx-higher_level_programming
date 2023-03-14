#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(num => parseInt(num)); // convert all arguments to integers
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      secondMax = max;
      max = numbers[i];
    } else if (numbers[i] > secondMax && numbers[i] !== max) {
      secondMax = numbers[i];
    }
  }

  if (secondMax === -Infinity) {
    console.log(0);
  } else {
    console.log(secondMax);
  }
}
