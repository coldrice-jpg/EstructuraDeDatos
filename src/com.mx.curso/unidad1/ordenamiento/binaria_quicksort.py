# Busqueda binaria después de quicksort

import random

# QuickSort del ejercicio anterior
def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(sorted_arr, target):

    low = 0
    high = len(sorted_arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid 
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 

# Creación datos desordenados
customer_ids = random.sample(range(1000, 2000), 500)
customer_to_find = customer_ids[123] 

print(f"Primeros 10 IDs de clientes (desordenados): {customer_ids[:10]}")

# Ordenamiento de los datos con QuickSort
sorted_ids = quick_sort(customer_ids)
print(f"Primeros 10 IDs de clientes (ordenados): {sorted_ids[:10]}")

# Busqueda de un cliente con Búsqueda Binaria
print(f"\nBuscando al cliente con ID: {customer_to_find}")
index = binary_search(sorted_ids, customer_to_find)

if index != -1:
    print(f"Cliente encontrado en el índice: {index}")
else:
    print("El cliente no fue encontrado.")