# Ordenamiento por selección

# Función de ordenamiento
def selection_sort_features(caracteristicas):
    
    n = len(caracteristicas)
    
    for i in range(n):
        
        max_idx = i
        for j in range(i + 1, n):
            
            if caracteristicas[j][0] > caracteristicas[max_idx][0]:
                max_idx = j
        
        caracteristicas[i], caracteristicas[max_idx] = caracteristicas[max_idx], caracteristicas[i]
    return caracteristicas

# Lista de 8 características
lista_caracteristicas = [
    (0.78, "Edad del cliente"),
    (0.45, "Frecuencia de compra"),
    (0.91, "Último monto gastado"),
    (0.23, "País de origen"),
    (0.65, "Productos vistos"),
    (0.88, "Antigüedad de la cuenta"),
    (0.15, "Dispositivo de acceso"),
    (0.55, "Items en el carrito")
]

print("--- Características antes de ordenar ---")
for puntaje, nombre in lista_caracteristicas:
    print(f"Importancia: {puntaje:.2f}, Característica: {nombre}")

caracteristicas_ordenadas = selection_sort_features(lista_caracteristicas.copy())

print("\n--- Características ordenadas por importancia (mayor a menor) ---")
for puntaje, nombre in caracteristicas_ordenadas:
    print(f"Importancia: {puntaje:.2f}, Característica: {nombre}")