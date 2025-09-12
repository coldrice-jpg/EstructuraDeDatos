# Inventario de productos de un almacén

# Declaración de la matriz
inventario = [
    [101, 50, 20],   
    [102, 30, 15],   
    [103, 80, 5]     
]

# Imprimir inventario
print("Inventario:")
for producto in inventario:
    print(f"ID: {producto[0]}, Stock: {producto[1]}, Precio: ${producto[2]}")

# Calcular valor total de un producto (ejemplo: producto 2)
indice = 1 
cantidad = inventario[indice][1]
precio = inventario[indice][2]
valor_total = cantidad * precio
print(f"\nValor total del producto {inventario[indice][0]}: ${valor_total}")

# Actualizar stock después de vender 10 unidades
inventario[indice][1] -= 10
print(f"Nuevo stock del producto {inventario[indice][0]}: {inventario[indice][1]}")
