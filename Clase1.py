import math

nombre = input("Hola, por favor ingrese su nombre: ")
viajeros = int(input("Por favor ingrese la cantidad de personas que viajan: "))

precio = 50000 * (viajeros + (math.ceil(viajeros / 30)))

print("El precio total del viaje es de $" + str(precio))