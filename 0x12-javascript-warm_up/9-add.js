#!/usr/bin/node
/* Prints the addition of 2 integers */

function add (a, b) {
  console.log(a + b);
}

add(process.argv[2], process.argv[3]);
