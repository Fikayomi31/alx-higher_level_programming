#!/usr/bin/node

const dict = require('./101-data.js').dict;
for (let keg in dict) {
	console.log(key + ': ' + dict[key].join(', '));
}
