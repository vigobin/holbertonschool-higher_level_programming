#!/usr/bin/node

const file = require('fs');
file.readFile(process.argv[2], 'utf-8', (err, inputF) => {
  if (err) throw err;
  console.log(inputF);
});
