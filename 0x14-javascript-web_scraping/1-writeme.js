#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(fileName, fileContent, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
