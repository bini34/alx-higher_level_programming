#!/usr/bin/node
// 101-starwars_characters.js
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    const characters = [];
    let count = 0;

    characterUrls.forEach((characterUrl, index) => {
	    request(characterUrl, (charError, charResponse, charBody) => {
		if (charError) {
			console.error(charError);
		} else {
			const character = JSON.parse(charBody);
			characters[index] = character.name;
			count += 1;
		if (count === characterUrls.length) {
			characters.forEach((name) => {
				console.log(name);
            });
          }
        }
      });
    });
  }
});

