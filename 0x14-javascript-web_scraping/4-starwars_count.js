#!/usr/bin/node
// const request = require('request');
// const url = process.argv[2];

// request(url, function (err, data, body) {
// if (err) {
// console.log(err);
//  } else {
//  let counter = 0;
// const films = JSON.parse(body).results;
// for (let result = 0; result < films.length; result++) {
// const characters = films[result].characters;
// for (let j = 0; j < characters.length; j++) {
// if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/' || characters[j] === 'http://swapi-api.hbtn.io/api/people/18/') {
// counter += 1;
// }
// }
// }
// console.log(counter);
// }
// });
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
