#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let k = '';
      for (let l = 0; l < this.width; l++) {
        k = k + 'X';
      }
      console.log(k);
    }
  }
}

module.exports = Rectangle;
