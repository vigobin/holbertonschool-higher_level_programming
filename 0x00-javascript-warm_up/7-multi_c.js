#!/usr/bin/node

const str = 'C is fun';
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(str);
  }
}
