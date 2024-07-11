#!/usr/bin/node

const request = require('request');

// Check if Movie ID is provided as a positional argument
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to get data from API. Status code: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Failed to get character data from API. Status code: ${charResponse.statusCode}`);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
