#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    let square = '';
    for (let j = 0; j < squareSize; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
