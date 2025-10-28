# Sistema de arbol de decisión 

def es_manzana(fruta, nivel_pregunta=1):

    # Comparación de los valores de las  en la pregunta uno
    if nivel_pregunta == 1:
        print(f"Nivel {nivel_pregunta} (Raíz): ¿La fruta es roja?")
        
        if fruta['color'] == 'rojo':
            print("  Respuesta: SÍ. Bajando al siguiente nivel...")
            return es_manzana(fruta, nivel_pregunta + 1)
        else:
            print("  Respuesta: NO.")
            return False
        
    # Comparación de la pregunta dos
    elif nivel_pregunta == 2:
        print(f"Nivel {nivel_pregunta}: ¿La fruta es redonda?")
        
        if fruta['forma'] == 'redonda':
            print("  Respuesta: SÍ.")
            return True
        else:
            print("  Respuesta: NO.")
            return False

# Caraterísticas de las frutas 
manzana = {'color': 'rojo', 'forma': 'redonda'}
platano = {'color': 'amarillo', 'forma': 'alargada'}
fresa = {'color': 'rojo', 'forma': 'corazon'}

# Respuestas de sí es manzana
print("Manzana 1")
resultado_1 = es_manzana(manzana)
print(f"¿Es manzana? {resultado_1}\n")

print("Manzana 2")
resultado_2 = es_manzana(platano)
print(f"¿Es manzana? {resultado_2}\n")

print("Manzana 3")
resultado_3 = es_manzana(fresa)
print(f"¿Es manzana? {resultado_3}\n")
