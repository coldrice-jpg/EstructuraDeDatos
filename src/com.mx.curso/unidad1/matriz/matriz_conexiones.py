# Matriz de Conexiones para una Red Neuronal Simple

# Matrices
entrada = [2,5,6]

pesos = [
    [2, 5],
    [1, 2],
    [4, 6]
]

vector = []

# Variables de suma
suma_columna1 = 0
suma_columna2 = 0

# Ciclo de multiplicación y suma
for i in range(len(entrada)):
    multi_columna1 = entrada[i] * pesos[i][0]
    suma_columna1 = suma_columna1+ multi_columna1
    multi_columna2 = entrada[i] * pesos[i][1]
    suma_columna2 = suma_columna2 + multi_columna2

# Agregar las sumas al vector
vector.append(suma_columna1)
vector.append(suma_columna2)

# Imprimir el vector
print(vector)