#!/usr/bin/node
const fs = require('fs');

const farg = fs.readFileSync(process.argv[2]).toString();
const sarg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], farg + sarg);
