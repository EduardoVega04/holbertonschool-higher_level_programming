#!/usr/bin/node
/* Display status code of a GET request */
const https = require('https');
https.get(process.argv[2], (res) => {
  console.log('code:', res.statusCode);
});
