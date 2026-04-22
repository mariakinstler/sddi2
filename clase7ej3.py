# Crear la clase
class PlataformaStreaming:
    def __init__(self, nombre, usuarios):
        self.nombre = nombre
        self.usuarios = usuarios

# Crear objetos (instancias)
netflix = PlataformaStreaming("Netflix", 20)
hbo_max = PlataformaStreaming("HBO Max", 100)
amazon_prime_video = PlataformaStreaming("Amazon Prime Video", 130)

# Mostrar datos
print(netflix.nombre, netflix.usuarios)
print(hbo_max.nombre, hbo_max.usuarios)
print(amazon_prime_video.nombre, amazon_prime_video.usuarios)
print("Los numeros son la cantidad de usuarios que hay en las plataformas")
print("Sumate a nuestras Plataformas para disfrutar de peliculas y series")
