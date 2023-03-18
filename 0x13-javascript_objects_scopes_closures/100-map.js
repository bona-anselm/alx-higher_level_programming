#!/usr/bin/node

const list = require('./100-data').list;

const computedArray = list.map((arrItem, index) => arrItem * index);
console.log(list);
console.log(computedArray);
