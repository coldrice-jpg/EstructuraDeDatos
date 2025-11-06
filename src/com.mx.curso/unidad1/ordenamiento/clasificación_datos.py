# Clasificación de Datos con Selección (Ordenamiento)

def ordenamiento_seleccion(productos):
    
    n = len(productos)
    
    for i in range(n):

        indice_min = i
        for j in range(i + 1, n):
            
            if productos[j] < productos[indice_min]:
                indice_min = j
                
        # Intercambiar el elemento mínimo encontrado con el primer
        productos[i], productos[indice_min] = productos[indice_min], productos[i]
        
    return productos

# Ejecución del algoritmo
puntuaciones_productos = [75, 50, 95, 20, 10, 80, 60, 35]

print(f"Productos Sin Ordenar: {puntuaciones_productos}\n")

productos_ordenados = ordenamiento_seleccion(puntuaciones_productos)

print(f"\nProductos Ordenados: {productos_ordenados}")