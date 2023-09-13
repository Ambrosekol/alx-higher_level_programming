#!/usr/bin/node

const superSquare_ = require('./5-square');

const Square = class Square extends superSquare_ {
  charPrint (c) {
    if (c) {
      let prints = '';
      for (let cont = 0; cont < this.height; cont++) {
        for (let cont = 0; cont < this.height; cont++) {
          prints = prints + c;
        }
        console.log(prints);
        prints = '';
      }
    } else {
      super.print();
    }
  }
};

module.exports = Square;
