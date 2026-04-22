# Crear la clase de personaje
class Personaje:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Crear el objeto
harry_potter = Personaje("Harry Potter", 19)

# Mostrar datos
print("Nombre:", harry_potter.nombre)
print("Edad:", harry_potter.edad)
print ("Hola soy Harry Potter bienvenido a mi programa ")
