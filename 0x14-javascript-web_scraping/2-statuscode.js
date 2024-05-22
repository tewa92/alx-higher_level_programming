#!/usr/bin/node
// Prints the status code of a GET request to the first command line argument

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
