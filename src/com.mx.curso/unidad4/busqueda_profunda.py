# Busqueda profundas

class RegistroEstado:
    def __init__(self, datos):
        self.valor = datos
        self.debajo = None

class AlmacenLIFO:
    def __init__(self):
        self.superior = None

    def apilar(self, nuevo_dato):
        nuevo_registro = RegistroEstado(nuevo_dato)
        nuevo_registro.debajo = self.superior
        self.superior = nuevo_registro

    def desapilar(self):
        if self.superior is None:
            return None
        
        extraido = self.superior.valor
        self.superior = self.superior.debajo
        return extraido

    def visualizar_pila(self):
        cursor = self.superior
        secuencia = []

        while cursor:
            secuencia.append(str(cursor.valor))
            cursor = cursor.debajo

        if secuencia:
            print("Estado actual de la Pila:", " | ".join(secuencia))
        else:
            print("Memoria LIFO vacía.")

# Ejemplo de uso con contexto de IA 
if __name__ == "__main__":
    memoria_busqueda = AlmacenLIFO()
    
    print("--- Registrando Nodos de Ruta ---")
    memoria_busqueda.apilar("Nodo_A")
    memoria_busqueda.apilar("Nodo_B")
    memoria_busqueda.visualizar_pila()
    
    print(f"Retrocediendo de: {memoria_busqueda.desapilar()}")
    memoria_busqueda.visualizar_pila()