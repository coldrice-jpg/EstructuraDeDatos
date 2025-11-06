# Priorización de Alertas de un Sistema de Detección de Fraudes

# Función de ordenamiento
def ordenamiento_seleccion(alertas):

    n = len(alertas)
    
    for i in range(n):

        indice_max = i
        for j in range(i + 1, n):
            if alertas[j] > alertas[indice_max]:
                indice_max = j
                
        # Intercambiar el elemento máximo encontrado con el primero
        alertas[i], alertas[indice_max] = alertas[indice_max], alertas[i]
        
    return alertas

# Ejecución del algoritmo
alertas_fraude = [0.32, 0.15, 0.89, 0.55, 0.95, 0.05, 0.76, 0.41, 0.60, 0.23]

print(f"Alertas Sin Ordenar: {alertas_fraude}\n")

alertas_priorizadas = ordenamiento_seleccion(alertas_fraude)

print(f"\nAlertas Priorizadas: {alertas_priorizadas}")