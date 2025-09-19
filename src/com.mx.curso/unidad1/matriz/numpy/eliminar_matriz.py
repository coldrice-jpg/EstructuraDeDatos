import numpy as np 

# 1. Crear un conjunto de datos (matriz de 3x4)
# La segunda columna (indice 1) es la que se eliminará

datos = np.array([
    [10, 20, 30, 40],
    [15, 20, 35, 45],
    [25, 20, 45, 55]
])

print("--- Conjunto de datos original ---")
print(datos)

# 2. Eliminar la columna de datos irrelevantes
# np.delete() se utiliza para eliminar elementos o filas/columnas
# axis=1 indica que se debe eliminar una columna
# El segundo argumento es el indice de la columna a eliminar (en este caso, 1)
datos_limpios = np.delete(datos, 2, axis=0)

print("\n--- Conjunto de datos limpio ---")
print(datos_limpios)

# Valores para axis
# axis=1 -> columnas
# axis=0 -> filas
# axis = None -> todo el array

datos_limpios2 = np.delete(datos_limpios, 0, axis=1)

print("\n--- Conjunto de datos limpios procesados ---")
print(datos_limpios2)