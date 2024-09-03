# ejemplo de uso de listas
misnovios = ["Martín", "Villamil", "Isaza"]
misnumeros = ["55", "100", "45"]

# Mostrando mis novios
print(misnovios)

# Mostrando mis números raros
print(misnumeros)

print("---Accediendo a los elementos de la lista---")
print(misnovios[-2])

if "xpersona" in misnovios:
  print("Si, 'xpersona' está en la lista de mis novios")
else:
  print("Chale, no eres mi novio")

print("Numero de novios")
Nnovios = len(misnovios)
print(f"Numero de novios: {Nnovios}")

print("Ciclo for en listas")
posicion = 0
for medianaranja in misnovios:
  print(posicion," ",medianaranja)
  posicion = posicion + 1