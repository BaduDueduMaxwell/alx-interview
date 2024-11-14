#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error("Error fetching movie:", error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error("Movie not found or network issue");
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const printCharacterNames = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error("Error fetching character:", error);
        return;
      }

      if (response.statusCode === 200) {
        const character = JSON.parse(body);
        console.log(character.name);
        printCharacterNames(index + 1);
      }
    });
  };

  printCharacterNames(0);
});
