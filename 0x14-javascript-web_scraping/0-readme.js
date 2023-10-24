#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
