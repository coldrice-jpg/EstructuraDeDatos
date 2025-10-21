# Analisis de rendimiento MergeSort vs QuickSort

import time
import random
import sys

# Aumentar el límite de recursividad para arreglos grandes
sys.setrecursionlimit(20000)

# Función de MergeSort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

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
    return arr

# Función de QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]
        izquierda = [x for x in arr if x < pivote]
        centro = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return quick_sort(izquierda) + centro + quick_sort(derecha)

# Tamaños de los arreglos para la prueba
tamaño_datos = [1000, 10000]

for tamaño in tamaño_datos:
    print(f"\n--- Analizando con {tamaño} elementos ---")
    datos_aleatorios = [random.randint(1, 100000) for _ in range(tamaño)]
    
    # Medición de MergeSort
    copia_datos_merge = datos_aleatorios.copy()
    start_time = time.perf_counter()
    merge_sort(copia_datos_merge)
    end_time = time.perf_counter()
    print(f"MergeSort tardó: {end_time - start_time:.6f} segundos.")
    
    # Medición de QuickSort
    copia_datos_quick = datos_aleatorios.copy()
    start_time = time.perf_counter()
    quick_sort(copia_datos_quick)
    end_time = time.perf_counter()
    print(f"QuickSort tardó: {end_time - start_time:.6f} segundos.")