#!/usr/bin/node
const request = require('request');
let characters;
const dictionary = {};
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  characters = JSON.parse(body).characters;
  for (const url of characters) {
    request(url, (error, response, body) =>
      !error && addData(url, JSON.parse(body).name));
  }
});

function addData (url, name) {
  dictionary[url] = name;
  if (Object.entries(dictionary).length === characters.length) {
    for (const url of characters) {
      console.log(dictionary[url]);
    }
  }
}
