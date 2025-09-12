#Operación de producto punto (base de las redes neuronales)

import numpy as np
import time

# Vector de entrada (una sola característica de 3 neuronas)
entrada = np.array([1,4])

# Matriz de pesos (3 neuronas de entrada, 2 de salida)
pesos = np.array([
    [0.5, 0.2,0.10,0.9],
    [0.1, 0.9,0.10,1.1]
])

start_time = time.time()
# Realizar el producto punto
salida = np.dot(entrada, pesos)
end_time = time.time()

print("Inicio:", start_time)
print("Tiempos:", end_time-start_time)
print("Vector de entrada:", entrada)
print("Matriz de pesos:\n", pesos)
print("\nSalida de la capa de neuronas (producto punto):", salida)