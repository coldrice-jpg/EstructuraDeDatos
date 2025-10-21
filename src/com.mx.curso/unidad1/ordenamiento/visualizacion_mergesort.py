# Taller de Recursividad: Visualización de MergeSort

# Función visual de MergeSort
def visual_merge_sort(arr, indent=""):

    print(f"{indent}Dividiendo: {arr}")
    
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        visual_merge_sort(L, indent + "  ")
        visual_merge_sort(R, indent + "  ")
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        print(f"{indent}Mezclado:  {arr}")
    else:
        print(f"{indent}Caso base (lista de 1), no se hace nada.")

# Un arreglo de 8 elementos para visualizar
array_to_visualize = [38, 27, 43, 3, 9, 82, 10, 50]

print(f"Arreglo Original: {array_to_visualize}\n")
visual_merge_sort(array_to_visualize)
print(f"\nArreglo Final Ordenado: {array_to_visualize}")