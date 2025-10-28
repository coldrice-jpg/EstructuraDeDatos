# Búsqueda de un Hipo-parámetro Óptimo

# Función de búsqueda binaria
def busqueda_hiperparametro(tasas_aprendizaje, tasa_objetivo):
    
    izquierda = 0
    derecha = len(tasas_aprendizaje) - 1

    while izquierda <= derecha:
        
        medio = (izquierda + derecha) // 2
        valor_medio = tasas_aprendizaje[medio]
        
        if valor_medio == tasa_objetivo:
            return medio
            
        elif valor_medio < tasa_objetivo:

            izquierda = medio + 1
            
        else:

            derecha = medio - 1
            
    return -1

# Tasas de aprendizaje
tasas_posibles = [0.0001, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]
tasa_encontrar = 0.05

# Ejecutar la búsqueda
resultado = busqueda_hiperparametro(tasas_posibles, tasa_encontrar)

if resultado != -1:
    print(f"\nLa tasa de aprendizaje {tasa_encontrar} se encontró en la posición {resultado}.")
else:
    print(f"\nLa tasa de aprendizaje {tasa_encontrar} no es una de las opciones válidas.")