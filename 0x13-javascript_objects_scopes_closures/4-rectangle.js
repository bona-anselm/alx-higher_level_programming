#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let squareSymbol = '';
      for (let j = 0; j < this.width; j++) {
        squareSymbol += 'X';
      }
      console.log(squareSymbol);
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const brief = this.height;
    this.height = this.width;
    this.width = brief;
  }
};
