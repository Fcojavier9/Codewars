def God():
    adan = Man("Adan")
    eva = Woman("Eva")
    return [adan, eva]

# Clase padre
class Human:
    def __init__(self, nombre : str):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

# Herederos
class Man(Human):
    def __init__(self, nombre : str):
        super().__init__(nombre)

class Woman(Human):
    def __init__(self, nombre : str):
        super().__init__(nombre)

# Ejecucion
creacion = God()
print(f"Hombre creado: {creacion[0]}")
print(f"Mujer creada: {creacion[1]}")