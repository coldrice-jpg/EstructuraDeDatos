# Reversión de la Pila de Llamadas de un Árbol 

# Función de recursividad
def revertir_secuencia(cadena):

    if len(cadena) <= 1:

        return cadena
        
    primer_caracter = cadena[0]
    resto_cadena = cadena[1:]
    
    print(f"Llamada '{resto_cadena}'. Se guarda '{primer_caracter}' para el final")
    
    resultado_recursivo = revertir_secuencia(resto_cadena)
    resultado_final = resultado_recursivo + primer_caracter
    
    print(f"Resultado: '{resultado_final}'")
    return resultado_final

# Secuencia original
secuencia_ia = "IA_es_genial"

print(f"Secuencia original: {secuencia_ia}\n")

# Ejecutar la función 
secuencia_invertida = revertir_secuencia(secuencia_ia)

print(f"\nLa secuencia invertida es: '{secuencia_invertida}'")