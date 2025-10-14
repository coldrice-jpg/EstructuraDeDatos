# Registro de intensidades de luz

# Creación de la matriz
matriz = [
    [450, 450, 1100, 800],
    [1600, 1100, 800, 1100],
    [1100, 1600, 450, 450],
    [1100, 800, 1600, 800]
]

terminar = 0

while terminar < 1:
    print("Selecciona una opción:\n [1] Imprimir matriz.\n [2] Consultar celda específica.\n [3] Modificar una celda.\n [4] Calcular promedio de luz.\n [5] Salir.")
    eleccion = input()
    
    if eleccion == "1":
        print("Mapa de la luz:")
        for i in range(3):
            print(matriz[i])
        print("\n")
            
    elif eleccion == "2":
        print("Selecciona la fila de la posición que deseas consultar")
        fila = int(input())
        print("Selecciona la columna de la posición que deseas consultar")
        columna = int(input())
        print(f"La temperatura la posición seleccionada es: {matriz[fila][columna]}")
    
    elif eleccion == "3":
        print(f"Selecciona la fila a de la celda a modificar:")
        fila = int(input())
        print("Selecciona la columna a modificar:")
        columna = int(input())
        print("Ingresa nueva intensidad:")
        matriz[fila][columna] = int(input())
        print("Temperatura cambiada correctamente")
    
    elif eleccion == "4":
        promedio = sum(matriz) / len(matriz)
        print(f"El promedio de la intensidad de luz es: {promedio}")
        
    elif eleccion == "5":
        terminar += 1
    
    else:
        print("Selecciona una opción del 1 al 5")