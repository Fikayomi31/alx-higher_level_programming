#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length <= 3) {
	console.log(0);
} else {
	const number = args.map(Number);
	const num = [...new Set(number)];
	num.sort((a, b) => b - a);
	console.log(num[1]);
}
