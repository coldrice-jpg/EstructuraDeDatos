# Limpieza de datos con NumPy
import numpy as np

# Simular una matriz de 12 * 5
np.random.seed(42)
datos = np.random.rand(12, 5)* 100

# Simular datos erroneos
datos[0, 0] = -99 # Valor negativo
datos[2, 3] = 1000 # Valor fuera de rango

print("Datos originales:")
print(datos)

indices_erroneos = [0, 2]

datos_limpios = np.delete(datos, indices_erroneos, axis=0)
print("\nDatos limpios:")
print(datos_limpios)