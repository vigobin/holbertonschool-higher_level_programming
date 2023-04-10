#!/usr/bin/node

function factorial (n) {
  if (n < 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log(1);
} else {
  console.log(factorial(x));
}
