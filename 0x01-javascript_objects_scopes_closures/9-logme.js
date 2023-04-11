#!/usr/bin/node

let num = 0;
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};
