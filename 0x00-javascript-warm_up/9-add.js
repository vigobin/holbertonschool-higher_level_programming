#!/usr/bin/node

function add (num1, num2) {
  const result = num1 + num2;
  return result;
}

const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);
const addNum = add(n1, n2);
console.log(addNum);
