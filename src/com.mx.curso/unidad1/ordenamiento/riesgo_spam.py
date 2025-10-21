# Riesgo spam

# Función
def bubble_sort_spam(emails):
    
    n = len(emails)
    
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            
            if emails[j][0] > emails[j + 1][0]:
                emails[j], emails[j + 1] = emails[j + 1], emails[j]
    return emails

# Arreglo de 10 correos
puntaje_spam = [
    (85, "¡Gana un millón ahora!"),
    (20, "Re: Reporte semanal"),
    (95, "URGENTE: Tu cuenta ha sido comprometida"),
    (50, "Promoción especial para ti"),
    (10, "Confirmación de tu pedido"),
    (75, "Viagra a precios bajos"),
    (30, "Acta de la reunión del lunes"),
    (99, "Felicidades, has sido seleccionado"),
    (5, "Hola, ¿cómo estás?"),
    (60, "Descuentos exclusivos de nuestra tienda")
]

print("--- Lista de correos antes de ordenar ---")
for puntaje, asunto in puntaje_spam:
    print(f"Riesgo: {puntaje}, Asunto: {asunto}")

emails_ordenados = bubble_sort_spam(puntaje_spam.copy()) 

print("\n--- Lista de correos ordenada por riesgo ---")
for puntaje, asunto in emails_ordenados:
    print(f"Riesgo: {puntaje}, Asunto: {asunto}")