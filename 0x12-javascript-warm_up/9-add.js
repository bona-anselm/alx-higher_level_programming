#!/usr/bin/node

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

function add (a, b) {
  const result = firstInteger + secondInteger;
  console.log(result);
}
add();
