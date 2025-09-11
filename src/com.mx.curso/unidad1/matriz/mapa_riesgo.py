# Mapa de riesgo

# Crear matriz 8x8
matriz = [
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1]
    ]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()

area_riesgo = 0
area_precaucion = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 2:
            area_riesgo += 1
        if matriz[i][j] == 1:
            area_precaucion += 1
    
    
print(f"Area de Riesgo (2): {area_riesgo}")
print(f"Area de Precaución (1): {area_precaucion}\n")

# Actualizar la matriz de navegación
# Cambiar todos los 2 por 1

print("Actualización de matriz de navegación")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 2:
            matriz[i][j] = 1
        if matriz[i][j] == 1:
            area_precaucion += 1

area_riesgo_actualizada = 0
area_precaucion_actualizada = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
        if matriz[i][j] == 2:
            area_riesgo_actualizada += 1
        if matriz[i][j] == 1:
            area_precaucion_actualizada += 1
    print()

print(f"Area de Riesgo (2): {area_riesgo_actualizada}")
print(f"Area de Precaución (1): {area_precaucion_actualizada}")
