#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let x = parseInt(process.argv[2]);
  const k = x;
  while (x > 0) {
    let number = '';
    for (let m = 0; m < k; m++) {
      number = number + 'X';
    }
    console.log(number);
    x--;
  }
}
