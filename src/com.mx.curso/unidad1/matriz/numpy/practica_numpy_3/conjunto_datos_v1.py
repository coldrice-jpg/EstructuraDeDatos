# limpieza de conjuntos de datos para la IA
import numpy as np 

datos = np.array([
    [10.9, 1.1, 20.1, 30.1],
    [5.9, 2.1, 20.1, 3.1],
    [10.9, 3.1, 20.1, 30.1],
    [10.9, 4.1, 20.1, 30.1],
    [10.9, 5.1, 20.1, 30.1],
    [10.9, 7.1, 20.1, 30.1],
    [10.9, 8.1, 20.1, 30.1],
    [7.9, 100.1, 20.1, 30.1],
    [10.9, 10.1, 20.1, 30.1],
    [10.9, 11.1, 20.1, 30.1]]
)

print("Datos originales")
print(datos)

datos[6] = [99.99, 99.99, 99.99, 99.99]

datos[1, 1] = np.nan
datos[5, 2] = np.nan
datos[9, 3] = np.nan

print(" ----- Datos con errores ----- ", datos)

datos_sin_errores = np.delete(datos, 5, axis=0)

print(" ----- Datos sin errores -----", datos_sin_errores)

media_columna = np.nanmean(datos_sin_errores,axis=0)
print(" ----- Media de cada columna ----- ", media_columna)

# LLenar los valores donde se encuentra nan por el promedio de cada columna
for i in range(datos.shape[0]): # Shape[0] = filas
    for j in range(datos.shape[1]): # Shape[1] = columnas
        if np.isnan(datos[i, j]): # La función isnan evalua si es nan
            datos[i, j] = media_columna[j] # Toma la media de columna y la agrega en la posición del nan

print(" ----- Datos sin errores y con nan reemplazados ----- ", datos)
