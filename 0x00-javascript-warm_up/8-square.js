#!/usr/bin/node

const str = 'X';
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(str.repeat(process.argv[2]));
  }
}
