#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
	constructor (size) {
		super(size, size);
	}
	charPrint(c) {
		const value = c === undefined ? 'X': c;
		for (let i = 0; i < this.height; i++) {
			let row = '';
			for (let i = 0; i < this.width; i++) {
				row += value
			}
			console.log(row);
		}
	}
}

module.exports = Square;
