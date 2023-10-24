#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 'https://swapi-api.alx-tools.com/api/people/18';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
