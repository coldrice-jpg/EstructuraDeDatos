import pandas as pd

# Lista de estudiantes y examenes
estudiantes = ["Diego", "Miguel", "Juan", "Alan"]
examenes = ["Examen 1", "Examen 2", "Examen 3"]

# Creación del dataframe con los estudiantes y examenes
calificaciones = pd.DataFrame(0, index=estudiantes, columns=examenes)

print("--- Tabla Inicial de Calificaciones ---")
print(calificaciones)

# Ingresar calificaciones
for estudiante in calificaciones.index:
    for examen in calificaciones.columns:
        nota = int(input(f"Calificación de {estudiante} en el {examen}: "))
        calificaciones.loc[estudiante, examen] = nota

print(calificaciones)

# Promedio por estudiante
promedios_estudiante = calificaciones.mean(axis=1)
print("\n--- Promedio por Estudiante ---")
print(promedios_estudiante.round(2).to_string())

# Promedio por examen
promedios_examen = calificaciones.mean(axis=0)
print("\n--- Promedio por Examen ---")
print(promedios_examen.round(2).to_string())

# Calificación Más Alta
nota_mas_alta = calificaciones.max().max()
mejor_alumno, examen_destacado = calificaciones.stack().idxmax()

print(f"La calificación más alta fue {nota_mas_alta}, obtenida por {mejor_alumno} en el {examen_destacado}.")