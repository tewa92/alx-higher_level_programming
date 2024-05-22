#!/usr/bin/node

// Writes the contents of process.argv[3] to the file specified
// in process.argv[2]

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (err) {
    if (err) {
      console.log(err);
    }
  });
