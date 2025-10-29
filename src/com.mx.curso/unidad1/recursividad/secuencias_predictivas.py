# Generación de Secuencias Predictivas

# Función de las secuencias
def fibonacci_recursivo(n):
    
    if n <= 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Generación de los primeros 10 números
primeros_numeros = 10

print(f"Generando los primeros {primeros_numeros} números de la serie de Fibonacci:")

for i in range(primeros_numeros):
    resultado = fibonacci_recursivo(i)
    print(f"F({i}) = {resultado}")