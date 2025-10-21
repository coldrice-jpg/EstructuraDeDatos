# Combinación de Algoritmos: Clasificación y Recomendación

import random

# Función que ordena tuplas por su primer elemento
def merge_sort_recommendations(productos):
    if len(productos) > 1:
        mid = len(productos) // 2
        L = productos[:mid]
        R = productos[mid:]
        merge_sort_recommendations(L)
        merge_sort_recommendations(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            
            if L[i][0] > R[j][0]:
                productos[k] = L[i]
                i += 1
            else:
                productos[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            productos[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            productos[k] = R[j]
            j += 1
            k += 1
    return productos

# Creación de un conjunto de 100 productos
lista_producto = [(random.uniform(0.5, 1.0), f"Producto-{i:03d}") for i in range(100)]

print("--- Primeros 5 productos (sin ordenar) ---")
for score, name in lista_producto[:5]:
    print(f"Relevancia: {score:.2f}, Nombre: {name}")

# Ordenar toda la lista con MergeSort
sorted_products = merge_sort_recommendations(lista_producto.copy())

# Mostrar solo los 5 productos con mayor puntuación
print("\n--- TOP 5 PRODUCTOS RECOMENDADOS ---")
top_5 = sorted_products[:5]
for score, name in top_5:
    print(f"Relevancia: {score:.2f}, Nombre: {name}")