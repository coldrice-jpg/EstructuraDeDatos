# Mapa de las temperaturas de una ciudad

# Matriz del mapa
mapa = [
        [36, 34, 37],
        [33, 34, 35],
        [35, 34, 37]
]

# Condición del ciclo while
terminar = 0

# Ciclo de selección
while terminar < 1:
    print("Selecciona una opción:\n [1] Consultar mapa.\n [2] Modificar una zona.\n [3] Salir.")
    eleccion = input()
    
    if eleccion == "1":
        print("Mapa de la ciudad:")
        for i in range(3):
            print(mapa[i])
    
    elif eleccion == "2":
        print(f"Selecciona la fila a de la celda a modificar:")
        fila = int(input())
        print("Selecciona la columna a modificar:")
        columna = int(input())
        print("Ingresa nueva temperatura:")
        mapa[fila][columna] = int(input())
        print("Temperatura cambiada correctamente")
        
    elif eleccion == "3":
        terminar += 1
    
    else:
        print("Selecciona una opción del 1 al 3")