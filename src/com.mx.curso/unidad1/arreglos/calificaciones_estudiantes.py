# Crear arreglo que almacene las calificaciones de estudiantes

# Condición del ciclo while
terminar = 0

# Listas
calificaciones = [5, 7, 9, 8, 9, 7]
alumnos = ["Pepe", "José", "Angel", "Juan", "Alan", "Eric"]

# Ciclo while
while terminar < 1:
    
    # Menú
    print("¿Qué acción desea realizar?\n [1] Consultar calificación.\n [2] Modificar calificación.\n [3] Mostrar promedio.\n [4] Salir.")
    eleccion = input()
    
    # Elecciones del menú
    if eleccion == "1":
        print(f"Selecciona el indice del estudiante a consultar: {alumnos}")
        consultar = int(input())
        print(f"La calificación de {alumnos[consultar]} es: {calificaciones[consultar]}\n")
    elif eleccion == "2":
        print(f"Selecciona el indice del alumno a modificar: {alumnos}")
        consultar = int(input())
        calificaciones[consultar] = int(input("Nueva Calificación: "))
        print("\nCalificación cambiada exitosamente.")
    elif eleccion == "3":
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio es: {promedio}")
    elif eleccion == "4":
        terminar =  terminar + 1
    else: 
        print("Ingresa un numero del 1 al 4\n")