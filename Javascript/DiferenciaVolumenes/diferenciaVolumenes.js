// https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/javascript

function findDifference(a, b) {
  
    let sumA = a[0];
    let sumB = b[0];
    
    for(let i = 1; i < 3; i++){
      sumA *= a[i];
      sumB *= b[i];
    }
    
    return Math.abs(sumA-sumB);
}

console.log(findDifference([3, 2, 5], [1, 4, 4])); // 14