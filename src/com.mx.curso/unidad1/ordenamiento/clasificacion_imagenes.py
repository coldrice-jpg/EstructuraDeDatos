# Clasificación de imagenes por similaridad

import random

def quick_sort_similarity(puntos):

    if len(puntos) <= 1:
        return puntos
    else:
        pivote = puntos[len(puntos) // 2]
        
        izquierda = [x for x in puntos if x > pivote]

        centro = [x for x in puntos if x == pivote]

        derecha = [x for x in puntos if x < pivote]
        return quick_sort_similarity(izquierda) + centro + quick_sort_similarity(derecha)

# Generamos 200 puntuaciones de similaridad 
puntos_similares = [random.uniform(0.0, 1.0) for _ in range(200)]

print(f"--- Primeras 10 puntuaciones sin ordenar ---")
print([f"{punto:.2f}" for punto in puntos_similares[:10]])

puntos_ordenados = quick_sort_similarity(puntos_similares)

print(f"\n--- Las 10 imágenes más similares ---")
print([f"{punto:.2f}" for punto in puntos_ordenados[:10]])

print(f"\n--- Las 10 imágenes menos similares ---")
print([f"{punto:.2f}" for punto in puntos_ordenados[-10:]])