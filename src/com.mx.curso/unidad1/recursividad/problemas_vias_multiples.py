# Solución de Problemas con Vías Múltiples

# Función de la recursión
def torres_hanoi(n, origen, destino, auxiliar):

    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    torres_hanoi(n - 1, origen, auxiliar, destino)
    
    print(f"Mover disco {n} de {origen} a {destino}")
    
    torres_hanoi(n - 1, auxiliar, destino, origen)

# Prueba de la simulación
numero_discos = 4
print(f"Solución para {numero_discos} discos:\n")
torres_hanoi(numero_discos, 'A', 'C', 'B')