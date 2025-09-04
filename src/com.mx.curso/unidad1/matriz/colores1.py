# Detectar colores en una imagen
imagen = [
    [255, 255, 0],   
    [128, 0, 128],   
    [0, 0, 0],       
    [255, 255, 0],
    [128, 0, 128],
    [255, 255, 0],
    [0, 0, 0],
    [128, 0, 128],
    [255, 255, 0],
    [0, 0, 0],
    [128, 0, 128],
    [255, 255, 0]
]

contadores = {"Amarillos": 0, "Morados": 0, "Negros": 0}

for pixel in imagen:
    if pixel == [255, 255, 0]:   
        contadores["Amarillos"] += 1
    elif pixel == [128, 0, 128]: 
        contadores["Morados"] += 1
    elif pixel == [0, 0, 0]:    
        contadores["Negros"] += 1

for color, cantidad in contadores.items():
    print(f"Pixeles {color}: {cantidad}")