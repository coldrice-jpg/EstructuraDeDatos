import pandas as pd

# Creación de la matriz inicial
examenes = [
    ["Estudiante", "Examen 1", "Examen 2", "Examen 3"],
    ["Diego", 0, 0, 0], 
    ["Miguel", 0, 0, 0],
    ["Juan", 0, 0, 0],
    ["Alan", 0, 0, 0]
]

columnas = examenes[0]
datos = examenes[1:]

df = pd.DataFrame(datos, columns=columnas)
print("    Tabla Inicial ")
print(df.to_string(index=False))
print("\n")

# Ingresar calificaciones
print("    Ingresa las Calificaciones")
for i in range(len(datos)):
    nombre_estudiante = datos[i][0]
    for j in range(1, len(columnas)):
        nombre_examen = columnas[j]
        calificacion = int(input(f"Calificación de {nombre_estudiante} en el {nombre_examen}: "))
        datos[i][j] = calificacion

# Mostrar calificaciones
df = pd.DataFrame(datos, columns=columnas)
print(df.to_string(index=False))

# Calcular promedio por estudiante
print("\nPromedio por Estudiante:")

for fila in datos:
    nombre = fila[0]
    promedio = sum(fila[1:]) / (len(fila) - 1)
    print(f"{nombre}: {promedio:.2f}")

# Calcular promedio por examen
print("\nPromedio por Examen: ")

for j in range(1, len(columnas)):
    suma_examen = 0
    
    for i in range(len(datos)):
        suma_examen += datos[i][j]
    promedio_examen = suma_examen / len(datos)
    print(f"{columnas[j]}: {promedio_examen:.2f}")

# Encontrar la calificación más alta
maxima_nota = -1  
mejor_estudiante = ""
examen_max_nota = ""

for fila in datos:
    nombre_actual = fila[0]
    for i, nota in enumerate(fila[1:]): 
        if nota > maxima_nota:
            maxima_nota = nota
            mejor_estudiante = nombre_actual
            examen_max_nota = columnas[i + 1] 
            
print(f"La calificación más alta es {maxima_nota}, obtenida por {mejor_estudiante} en el {examen_max_nota}.")