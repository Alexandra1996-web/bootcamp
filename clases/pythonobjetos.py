#propiedadesdelosobjetos,clasessedefine
class Persona:
    edad = 0
    def __init__(self, un_nombre):
        self.mi_nombre = un_nombre
        print("Hola naci, me llamo", self.mi_nombre)

    def cumple(self):
        self.edad = self.edad + 1

pepe = Persona("Pepito")
pepa = Persona("Pepita")
print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)

class Blogger:
    lineas = 5
    def __init__(self, apuntes, hule):
        self.mynote = apuntes
        self.basurero = hule
        print("Hola escribi", self.mynote, self.basurero)

cuaderno = Blogger("Alex", "Hola") #mayusculalasclases
print(cuaderno.lineas)
print(cuaderno.mynote)
print(cuaderno.basurero)