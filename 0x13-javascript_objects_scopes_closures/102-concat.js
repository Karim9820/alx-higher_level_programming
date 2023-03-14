#!/usr/bin/node

var file1Path = process.argv[2];
var file2Path = process.argv[3];
var destPath = process.argv[4];

var file1 = fs.readFileSync(file1Path, 'utf8');
var file2 = fs.readFileSync(file2Path, 'utf8');

var result = file1 + file2;

fs.writeFileSync(destPath, result);
