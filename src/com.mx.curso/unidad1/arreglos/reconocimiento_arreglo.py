# El programa debe normalizar el vector de características, dividiendo cada valor por la suma total del vector.

# Declaración del vector
flor = [4.3, 2.7, 0.6]

# Operación
suma_total = sum(flor)

suma_normalizada = 0

# Ciclo
for car in flor:
    division = car / suma_total
    suma_normalizada = suma_normalizada + division
    
    print("Division:", division)

print("Flor:", flor)
print("Suma normalizada:", suma_normalizada)
