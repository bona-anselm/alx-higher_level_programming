#!/usr/bin/node

const formerSquare = require('./5-square');

class Square extends formerSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const squareSymbol = 'C'.repeat(this.width);

      for (let i = 0; i < this.height; i++) {
        console.log(squareSymbol);
      }
    }
  }
}
module.exports = Square;
