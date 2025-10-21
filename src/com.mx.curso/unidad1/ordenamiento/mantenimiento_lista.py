# Mantenimiento de datos

# Función de ordenación por inserción
def insert_in_sorted_list(lista_ordenada, nuevo_valor):
    
    i = 0
    
    while i < len(lista_ordenada) and lista_ordenada[i] < nuevo_valor:
        i += 1
    
    lista_ordenada.insert(i, nuevo_valor)
    return lista_ordenada

# Lista de 5 lecturas de sensores ya ordenadas
lecturas = [10.5, 15.2, 22.1, 25.8, 30.3]
nueva_lectura = 23.5

print(f"Lista ordenada original: {lecturas}")
print(f"Nueva lectura recibida: {nueva_lectura}")

lecturas_actualizadas = insert_in_sorted_list(lecturas.copy(), nueva_lectura)

print(f"Lista actualizada y ordenada: {lecturas_actualizadas}")