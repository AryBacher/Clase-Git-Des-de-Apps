import math
import json

nombre = input("Ingrese tu nombre: ")
presupuestos = []

filename = 'presupuestos.json'

corriendo = True

with open('presupuestos.json') as file:
    presupuestos = json.load(file)

while corriendo:
    eleccion = int(input("Usted desea calcular un nuevo presupuesto, ver los presupuestos calculados o no hacer nada. Presione 1 para la primera opción, 2 para la segunda y 3 para la tercera: "))

    if eleccion == 1:
        viajeros = int(input("Ingrese la cantidad de viajeros: "))
        precioTotal = 5000 * (viajeros + (math.ceil(viajeros / 30)))
        presupuestos.append(precioTotal)
        print("$" + str(precioTotal))

    elif eleccion == 2:
        count = 0
        for i in presupuestos:
            count += 1  
            print("Presupuesto " + str(count) + ": $" + str(i))

    elif eleccion == 3:
        corriendo = False

    else:
        print("Incorrecto. Ingrese nuevamente")

with open('presupuestos.json', "w") as file:
    json.dump(presupuestos, file)