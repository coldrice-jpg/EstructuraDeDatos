# Profesores enojados
# Arreglo de los estudiantes
a = []

def clase(a):
    # Numero de casos
    t = int(input())
    
    for i in range(t):
        
        # Limite de estudiantes
        k, n = int(input()), int(input())
        
        alumnos_temprano = 0
        alumnos_tarde = 0

        for j in range(k):
            j = j + 1 - n
            
            a.append(j)
            
            if j <= 0:
                alumnos_temprano += 1
            else:
                alumnos_tarde += 1

        print(a)
        
        a = []

        # Determinar si la clase se cancela o no
        if alumnos_tarde > alumnos_temprano:
            return "YES"
        else:
            return "NO"

clase(a)