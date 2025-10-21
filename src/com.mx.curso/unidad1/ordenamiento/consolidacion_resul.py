# Consolidación resultados

# Función de ordenamiento
def merge_sorted_lists(lista1, lista2):
    
    lista_anidada = []
    i, j = 0, 0 

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            lista_anidada.append(lista1[i])
            i += 1
        else:
            lista_anidada.append(lista2[j])
            j += 1
    
    
    lista_anidada.extend(lista1[i:])
    lista_anidada.extend(lista2[j:])
    
    return lista_anidada

# Dos listas de recomendaciones ya ordenadas
modelo_A = [101, 105, 115, 120, 150, 200, 210, 230, 250, 300]
modelo_B = [102, 110, 112, 125, 180, 190, 220, 240, 280, 310]

print(f"Recomendaciones Modelo A: {modelo_A}")
print(f"Recomendaciones Modelo B: {modelo_B}")

recomendacion_final = merge_sorted_lists(modelo_A, modelo_B)

print(f"\nLista anidada y ordenada: {recomendacion_final}")
print(f"Total de recomendaciones: {len(recomendacion_final)}")