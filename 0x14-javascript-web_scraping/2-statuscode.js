#!/usr/bin/node
/* Display status code of a GET request */
const https = require('https');
https.get(process.argv[2], (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
