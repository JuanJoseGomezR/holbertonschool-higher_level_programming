#!/usr/bin/node
exports.logMe = function (item) {
    if (this.counter === undefined) {
      this.counter = 0;
    } else {
      this.counter++;
    }
    const count = this.counter;
    console.log(count + ': ' + item);
  };
