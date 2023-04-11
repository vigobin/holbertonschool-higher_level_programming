#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    const str = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(str.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
