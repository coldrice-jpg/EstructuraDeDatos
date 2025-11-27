# Sorting: bubble sort

# Función del ordenamiento
def ordenar_burbuja(a):
    n = len(a)

    veces_recorrida = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                veces_recorrida += 1
    
    print(f"Veces recorrida: {veces_recorrida}")

    print(f"Primer elemento: {a[0]}")

    print(f"Ultimo elemento: {a[-1]}")
    
    return a

a = [3, 2, 1]

resultado = ordenar_burbuja(a)

