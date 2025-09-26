# Practica con DaraSet Iris
import numpy as np 

# Cargar el dataset
datos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_1/iris.data',
                        delimiter=',', dtype='object')

# Visualizar los datos
print(datos)

# Cargar solo las primeras 4 columnas
datos_numericos = np.genfromtxt('src/com.mx.curso/unidad1/matriz/numpy/practica_numpy_1/iris.data',
                                delimiter=',', usecols=(0, 1, 2, 3))

# Visualizar los datos numericos
print(datos_numericos)

# Listado de indicios a eliminar
indices_eliminar = [0, 1, 2, 50]

# Eliminar las filas con los indices detectados con error
datos_limpios = np.delete(datos_numericos, indices_eliminar, axis=0)

print(" ----- Datos Limpios ----- ", datos_limpios)

datos_limpios[0, 0] = np.nan
datos_limpios[4, 0] = np.nan
datos_limpios[12, 1] = np.nan
datos_limpios[10, 2] = np.nan
datos_limpios[10, 0] = np.nan
datos_limpios[3, 1] = np.nan
datos_limpios[10, 2] = np.nan
datos_limpios[4, 1] = np.nan
datos_limpios[5, 0] = np.nan
datos_limpios[25, 1] = np.nan

ultimaFila = datos_limpios.shape[0] - 1
print("Ultima fila", ultimaFila)

# Matriz con datos faltantes
print(" ----- Datos con Faltantes ----- ", datos_limpios)

media_columna = np.nanmean(datos_limpios,axis=0)
print(" ----- Media de cada columna ----- ", media_columna)

for i in range(datos_limpios.shape[0]): # Shape[0] = filas
    for j in range(datos_limpios.shape[1]): # Shape[1] = columnas
        if np.isnan(datos_limpios[i, j]): # La función isnan evalua si es nan
            datos_limpios[i, j] = media_columna[j] # Toma la media de columna y la agrega en la posición del nan

print(" ----- Datos sin errores y con nan reemplazados ----- ", datos_limpios)
