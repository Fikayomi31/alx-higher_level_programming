#!/usr/bin/node

const args = Math.floor(Number(process.argv[2]));
console.log(isNaN(args) ? 'Not a number' : `My number: ${args}`);
