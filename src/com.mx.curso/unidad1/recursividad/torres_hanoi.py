# Algoritmo de las torres de hanoi

# Función del algoritmo
def resolver_torres(n, origen, destino, auxiliar):
    
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    
    resolver_torres(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")

    resolver_torres(n - 1, auxiliar, destino, origen)

if __name__ == "__main__":
    numero_de_discos = 5  
    poste_origen = 'A'   
    poste_auxiliar = 'B' 
    poste_destino = 'C'   

    print(f"Secuencia de movimientos para {numero_de_discos} discos:")

    # Iniciar la solución
    resolver_torres(numero_de_discos, poste_origen, poste_destino, poste_auxiliar)

