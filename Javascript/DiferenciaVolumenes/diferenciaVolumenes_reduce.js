// https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/javascript

const findDifference = (a, b) => {
  return Math.abs(
    a.reduce((acc, val) => acc * val) - b.reduce((acc, val) => acc * val)
  );
}

console.log(findDifference([3, 2, 5], [1, 4, 4])); // 14
