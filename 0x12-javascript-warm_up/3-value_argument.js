#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0]) {
  args.forEach((arg, index) => {
    console.log(arg);
  });
} else {
  console.log('No argument');
}
