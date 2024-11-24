// https://www.codewars.com/kata/539ee3b6757843632d00026b/train/javascript

const capitals = word => {
	let resultado = [];
  
  word.split('').forEach( (caracter, index) => {
    if(caracter >= 'A' && caracter <= 'Z'){
      resultado.push(index);
    }
  })
 
  return resultado;
};

console.log(capitals('CodEwArS')) // [0,3,5,7]