# Clasificación de Datos con QuickSort (Ordenamiento)

# Función de partición
def particion(lista, inicio, fin):

    # El pivote es el último elemento
    pivote = lista[fin]
    
    i = inicio - 1

    for j in range(inicio, fin):
        
        if lista[j] <= pivote:
            
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
            
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    
    return i + 1

# Función de ordenamiento quicksort
def quicksort(lista, inicio, fin):
    
    if inicio < fin:
        
        posicion_pivote = particion(lista, inicio, fin)
        
        quicksort(lista, inicio, posicion_pivote - 1)
        
        quicksort(lista, posicion_pivote + 1, fin)

# Ejecución del algoritmo
comentarios = [0.5, -0.8, 0.2, -0.3, 0.9, -0.1]
n = len(comentarios)

print(f"Comentarios Sin Ordenar: {comentarios}")

# Llamada inicial a QuickSort
quicksort(comentarios, 0, n - 1)

print(f"Comentarios Ordenados: {comentarios}")