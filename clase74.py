# Crear la clase Casa
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


# Crear un objeto de la clase
mi_casa = Casa("Beige", 2)

# Mostrar los atributos
print("Color:", mi_casa.color)
print("Cantidad de pisos:", mi_casa.cantidad_pisos)
print("Mi casa es color Beige y tiene 2 pisos")
