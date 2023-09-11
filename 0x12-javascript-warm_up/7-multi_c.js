#!/usr/bin/node

const args = Math.floor(Number(process.argv[2]))
if (!isNaN(args)) {
	for (let i = 0; i < args; i++)	{
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
