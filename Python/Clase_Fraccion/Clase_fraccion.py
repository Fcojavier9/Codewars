from math import gcd

class Fraction:
    
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator can't be zero.")
        self.top = numerator
        self.bottom = denominator
        self.simplify()
    
    # Método para simplificar la fracción
    def simplify(self):
        common_divisor = gcd(self.top, self.bottom)
        #! //= sirve para dividir y redondear al entero más cercano
        self.top //= common_divisor
        self.bottom //= common_divisor

    # Prueba de igualdad
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    # Suma de fracciones, reedito el metodo +
    def __add__(self, other):
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    # Resta de fracciones, reedito el metodo -
    def __sub__(self, other):
        new_top = self.top * other.bottom - other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)
    
    # Multiplicación de fracciones, reedito el metodo *
    def __mul__(self, other):
        new_top = self.top * other.top
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)
    
    # Representación de la fracción toString
    def __str__(self):
        return f"{self.top}/{self.bottom}"