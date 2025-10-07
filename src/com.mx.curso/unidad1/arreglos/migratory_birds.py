# Arreglo de aves migratorias
arr = [1, 2, 4, 4, 4, 2, 2, 3, 4, 2, 3, 5, 6]
aves = set(arr)

# Conteo de las veces que se ha visto un ave
print(len(arr))
print(arr)

print("Tipos de aves y sus frecuencias:")

# Conteo de las veces que se ven las aves
ave_mas_vista = max(aves, key=arr.count)
frecuencia = arr.count(ave_mas_vista)
print(f"\nEL tipo de ave que más se repite es: {ave_mas_vista}, se repite {frecuencia} veces")

