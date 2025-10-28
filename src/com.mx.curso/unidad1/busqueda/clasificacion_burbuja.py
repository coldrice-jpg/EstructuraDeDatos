# Clasificación de Datos con Burbuja

# Función de ordenamiento burbuja
def ordenar_confianzas(puntajes):
    
    n = len(puntajes)
    print(f"Lista original: {puntajes}")
    
    for i in range(n):
        
        intercambio_realizado = False
        
        for j in range(0, n - i - 1):
            
            if puntajes[j] > puntajes[j + 1]:

                puntajes[j], puntajes[j+1] = puntajes[j+1], puntajes[j]
                intercambio_realizado = True
        
        if not intercambio_realizado:
            break
        
    return puntajes

# Lista de predicciones
predicciones = [0.85, 0.92, 0.56, 0.71, 0.23, 0.99, 0.64]

# Ejecutar el ordenamiento
puntajes_ordenados = ordenar_confianzas(predicciones)

print(f"\nLos puntajes de confianza ordenados son: {puntajes_ordenados}")