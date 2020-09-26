#!/usr/bin/node
/* Class Rectangle that defines a rectangle */
class Rectangle {
  constructor (w, h) {
    if (w > 0) {
      this.width = w;
    }
    if (h > 0) {
      this.height = h;
    }
  }
}
module.exports = Rectangle;
