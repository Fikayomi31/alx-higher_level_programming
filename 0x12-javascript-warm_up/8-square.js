#!/usr/bin/node

const args = Math.floor(Number(process.argv[2]));
if (!isNaN(args)) {
	for (let i = 0; i < args; i++) {
		let string = 'X';
		
		console.log(`${string.repeat(args)}`);
	}
} else {
	console.log('Missing size');
}
