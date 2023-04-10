#!/usr/bin/node

const str = 'X';
const integer = parseInt(process.argv[2]);
if (integer === undefined || isNaN(integer)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(str.repeat(process.argv[2]));
  }
}
