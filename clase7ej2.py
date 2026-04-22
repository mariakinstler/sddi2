# Crear la clase
class Dinosaurio:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear los objetos
velociraptor = Dinosaurio("Velociraptor")
tiranosaurio_rex = Dinosaurio("Tiranosaurio Rex")
braquiosaurio = Dinosaurio("Braquiosaurio")

# Mostrar los nombres
print(velociraptor.nombre)
print(tiranosaurio_rex.nombre)
print(braquiosaurio.nombre)
