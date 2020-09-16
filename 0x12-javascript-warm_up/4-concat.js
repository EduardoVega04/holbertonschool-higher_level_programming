#!/usr/bin/node
/* Prints two arguments passed to it, in the following format: “ is ” */

let myArg1 = 'undefined';
let myArg2 = 'undefined';

if (process.argv[2]) {
  myArg1 = process.argv[2];
}
if (process.argv[3]) {
  myArg2 = process.argv[3];
}
console.log(myArg1, 'is', myArg2);
