#!/usr/bin/node

const request = require('request');

const urlPeople = 'https://swapi-api.hbtn.io/api/people/18/';

request(process.argv[2], function (error, response, body) {
  if (error) {
    throw error;
  } else {
    let count = 0;
    const info = JSON.parse(body).results;
    for (let i = 0; i < info.length; i++) {
      if (info[i].characters.includes(urlPeople)) count++;
    }
    console.log(count);
  }
});
