# Analisis de rendimiento

import time
import random

# Función de Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Función de Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Tamaños de los arreglos para la prueba
tamaño_datos = [100, 1000, 5000]

for size in tamaño_datos:
    print(f"\n--- Analizando con {size} elementos ---")
    
    # Generar datos aleatorios
    datos_aleatorios = [random.randint(1, 100000) for _ in range(size)]
    
    # Medición de bubble sort
    copia_datos_burbuja = datos_aleatorios.copy()
    start_time = time.perf_counter()
    bubble_sort(copia_datos_burbuja)
    end_time = time.perf_counter()
    print(f"Bubble Sort tardó: {end_time - start_time:.6f} segundos.")
    
    # Medición de Insertion Sort
    copia_datos_insercion = datos_aleatorios.copy()
    start_time = time.perf_counter()
    insertion_sort(copia_datos_insercion)
    end_time = time.perf_counter()
    print(f"Insertion Sort tardó: {end_time - start_time:.6f} segundos.")