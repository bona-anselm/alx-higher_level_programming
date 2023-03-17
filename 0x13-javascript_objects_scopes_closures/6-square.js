#!/usr/bin/node

const formerSquare = require('./5-square');

class Square extends formerSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        const squareSymbol = c;
        console.log(squareSymbol.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
