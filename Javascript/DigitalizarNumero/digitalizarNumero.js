// https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/javascript

const digitize = (n) =>
  n
    .toString()
    .split("")
    .map((elemento) => Number(elemento));


console.log(digitize(35231)); // [ 3, 5, 2, 3, 1 ]