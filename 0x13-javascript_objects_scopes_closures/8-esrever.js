#!/usr/bin/node
exports.esrever = function (list) {
    const liz = [];
    for (let a = list.length - 1; a >= 0; a--) {
      liz.push(list[a]);
    }
    return liz;
  };
