

# Función para partir el chocolate
def birthday(s, d, m):

    # Conteo
    n = len(s)  
    count = 0   
    
    if m > n:
        return 0
    

    for i in range(n - m + 1):
        
        window = s[i : i + m]
        
        current_sum = sum(window)
        
        if current_sum == d:
            count += 1
            
    return count

# Ejemplo

datos_barra= [2, 2, 1, 3, 2]
dia = 4
mes = 2
# Impresión de los datos
print(f"Barra: {datos_barra}, Día: {dia}, Mes: {mes}")
print(f"Formas encontradas: {birthday(datos_barra, dia, mes)}")