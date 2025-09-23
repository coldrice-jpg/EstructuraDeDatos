# Limpieza de datos para Machine Learning
import numpy as np 

matriz = np.array([
    [12, 14, 53, 12],
    [19, 21, 35, 32],
    [12, 5, 4, 23]
])

print("Datos de la matriz:\n", matriz)

# Eliminar la tercer columna
matriz_renovada = np.delete(matriz, 2, axis=1)
print("Matriz con datos eliminados:\n", matriz_renovada)
