# Valores de la matriz
filas = 5
columnas = 5
sesion_activa = True

# Se crea la rejilla o matriz con un valor inicial
rejilla = [['0'] * columnas for _ in range(filas)]

borde = "------" * columnas
print("      ", end="")
print(f"\n{borde}")
for indice_fila, fila_actual in enumerate(rejilla):
    for celda in fila_actual:
        print(f"  {celda}  |", end="")
    print()
print(borde)

# Bucle para modificar la matriz
while sesion_activa:
    
    fila_ingresada = int(input("\nElige el número de Fila para modificar: "))
    col_ingresada = int(input("Elige el número de Columna para modificar: "))
    simbolo_ingresado = input("Escribe '1' para obstáculo o '0' para limpiar: ").strip().upper()

    rejilla[fila_ingresada][col_ingresada] = simbolo_ingresado
        
    borde = "------" * columnas
    print("    ", end="")
    print(f"\n{borde}")
    for indice_fila, fila_actual in enumerate(rejilla):
        for celda in fila_actual:
            print(f"  {celda}  |", end="")
        print()
    print(borde)

    respuesta = input("\n¿Continuar modificando?: ")
    if respuesta.lower() == 'no':
        sesion_activa = False


# Contar los obstaculos
conteo_total_obstaculos = sum(fila.count('1') for fila in rejilla)
print(f"Obstáculos totales en la rejilla: {conteo_total_obstaculos}")

# Se cuentan los obstáculos en una fila específica
fila_a_contar = int(input("\nElige una Fila para contar sus obstáculos: "))
if 0 <= fila_a_contar < filas:
    conteo_en_fila = rejilla[fila_a_contar].count('1')
    print(f"En la Fila {fila_a_contar} hay {conteo_en_fila} obstáculos.")
else:
    print("El número de fila no es válido.")