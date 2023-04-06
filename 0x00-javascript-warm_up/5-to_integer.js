#!/usr/bin/node

const integer = parseInt(process.argv[2]);
if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
