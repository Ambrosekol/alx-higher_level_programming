#!/usr/bin/node

function factorial (val) {
  if (val === 1) {
    return (1);
  }
  return (val * factorial(val - 1));
}

let k = 0;
if (isNaN(parseInt(process.argv[2]))) {
  k = 1;
} else {
  k = parseInt(process.argv[2]);
}

console.log(factorial(k));
