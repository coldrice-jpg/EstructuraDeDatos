# Simulación de sensores en un robot

# Arreglo de sensores
sensores = [120, 85, 210, 150]

# Declaración del umbral
umbral = 100

# Recorremos cada sensor
for i in range(len(sensores)):
    valor = sensores[i]
    print(f"Sensor {i+1}: {valor} cm")
    if valor < umbral:
        print("Advertencia, distancia demasiado corta")