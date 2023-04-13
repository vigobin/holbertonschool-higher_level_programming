#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const url_character = 'https://swapi-api.hbtn.io/api/people/18/';
let movies = [];

request(url_character, function (error, response, body) {
  if (error) throw error;
  else {
    movies = JSON.parse(body).films;
  }
  console.log(movies.length);
});
