#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a Number');
} else {
  console.log(parseInt('My number: ' `${process.argv[2]}`));
}
