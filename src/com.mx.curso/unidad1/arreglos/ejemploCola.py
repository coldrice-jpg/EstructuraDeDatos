# Ejemplo de cola (FIFO - First In First Out)
class Cola:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")
    
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía")
    
    def tamano(self):
        return len(self.items)

# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola()
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    print("Frente de la cola:", cola.ver_frente())
    print("Tamaño de la cola:", cola.tamano())
    print("Desencolando:", cola.desencolar())
    print("Tamaño de la cola despues de desencolar:", cola.tamano())