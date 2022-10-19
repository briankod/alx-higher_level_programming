#!/usr/bin/node
const request = require('request');
let fs = require('fs');
request(`${process.argv[2]}`, 'utf-8').pipe(fs.createWriteStream(process.argv[3]));
