# Historial de entrenamiento del modelo

# Precisiones
precisiones = [0.75, 0.81, 0.83, 0.85, 0.86, 0.87, 0.89, 0.97, 0.95]

print("Lista de precisiones:", precisiones)

# Entrada de cuantas precisiones se quieren agregar
num_epocas = int(input("\nNúmero de precisiones a agregar: "))

# Ciclo para agregar más precisiones
for i in range(num_epocas):
    valor = float(input(f"Precisión a agregar:"))
    if 0 <= valor <= 1:
        precisiones.append(valor)
    else:
        print("Valor no valido.")

precision_maxima = max(precisiones)
ultima_precision = precisiones[-1]

# Impresión de precisiones
print(f"Precisión final: {ultima_precision}")
print(f"Precisión más alta: {precision_maxima}")