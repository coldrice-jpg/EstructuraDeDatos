# Entrenamiento de una red neuronal

entrada = [1, 2]

# Matris pesos 3x2

pesos = [
    [4, 1, 5, 6],
    [4, 1, 5, 6],
    [2, 3, 1, 7]
]

salida = [0,0,0,0]

for j in range(len(pesos[0])):
    for i in range(len(entrada)):
        salida[j] += entrada[i] * pesos[i][j]

print("Vector entrada:", entrada)
print("Matriz Pesos:", pesos)
print("Vector Salida:", salida)