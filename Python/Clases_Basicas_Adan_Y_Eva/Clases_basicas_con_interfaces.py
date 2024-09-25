from abc import ABC, abstractmethod

def God():
    adan = Man("Adan")
    eva = Woman("Eva")
    return [adan, eva]

# Clase padre
class Human(ABC):
    def __init__(self, nombre : str):
        self.nombre = nombre

    def __str__(self):
        return f"{self.__class__.__name__}"
    
    #metodo abstracto
    @abstractmethod
    def mear(self):
        ...

# Herederos
class Man(Human):
    def mear(self):
        return "Meo de pie"

class Woman(Human):
    def mear(self):
        return "Meo sentada"

creacion = God()
print(creacion[0], creacion[1], creacion[0].mear())