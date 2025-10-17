# Examen primer parcial

# Creación de la función
def diferencia(arr):
    
    # Declaración variables suma
    suma_diagonal1 = 0
    suma_diagonal2 = 0
    
    # Ciclo de suma
    for i in range(len(arr)):
        
        suma_diagonal1 += arr[i][i]
        
        suma_diagonal2 += arr[i][(len(arr) - 1) - i]
        
    return abs(suma_diagonal1 - suma_diagonal2)
    
# Creación de la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

resultado = diferencia(matriz)

print(resultado)

