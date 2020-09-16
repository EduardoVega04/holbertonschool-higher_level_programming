#!/usr/bin/node
/* Handling argv, argc */
const args = process.argv;

if (args[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
