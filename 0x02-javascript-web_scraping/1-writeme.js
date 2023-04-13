#!/usr/bin/node

const file = require('fs');
const input = process.argv[3];
file.writeFile(process.argv[2], input, 'utf-8', (err) => {
  if (err) throw err;
});
