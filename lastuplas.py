arcoiris = ("Azul","Verde","Rojo","Amarillo")
print(arcoiris)

print("-Longitud arcoiris")
print(len(arcoiris))

animales = ("Pantera", 20, "Estatura", 1.7)
print(animales)

print("Elementos de la tupla")
print(animales[2])

print("Modificando elementos")
rateros = ("Juan","Ana","Pedro")
y = list(rateros)
y[1] = "Polainas"
rateros = tuple(y)
print(rateros)

print("Agregando elementos")
Nanimal = ("body","chetos")
y = list(Nanimal)
print(y)
y.append("tontolino")
Nanimal = tuple(y)
print(Nanimal)

print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)