function coinCombo(cents) {
  const valores = [25, 10, 5, 1];
  const array = [0, 0, 0, 0];

  while (cents > 0) {
    valores.forEach((valor, index) => {
      if (cents % valor === 0) {
        array[array.length - 1 - index] = cents / valor;
        cents = 0;
      } else {
        array[array.length - 1 - index] = Math.floor(cents / valor);
        cents %= valor;
      }
    });
  }

  return array;
}

console.log(coinCombo(6));
