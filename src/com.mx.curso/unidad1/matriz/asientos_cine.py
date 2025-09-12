# Mapa de asientos del cine (4 filas x 5 asientos)

# Matriz de asientos
asientos = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0]
]

# Imprimir mapa de asientos
print("Mapa de asientos (0=Libre, 1=Ocupado):")
for fila in asientos:
    print(fila)

# Pedir al usuario un asiento
fila = int(input("\nIngrese número de fila (0-3): "))
columna = int(input("Ingrese número de asiento (0-4): "))

# Marcar como ocupado si está libre
if asientos[fila][columna] == 0:
    asientos[fila][columna] = 1
    print("Asiento reservado.")
else:
    print("Asiento ocupado, selecciona otro.")

# Contar asientos libres
libres = 0
for f in asientos:
    for asiento in f:
        if asiento == 0:
            libres += 1

print("\nMapa actualizado:")
for fila in asientos:
    print(fila)

print(f"\nAsientos libres disponibles: {libres}")