# Ejercicio 01 - Mi Primera Mascota (clase y objetos)
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def presentarse(self):
        return f"Soy {self.nombre}, un {self.especie} de {self.edad} años."
if __name__ == '__main__':
    m = Mascota('Firulais','Perro',3)
    print(m.presentarse())
