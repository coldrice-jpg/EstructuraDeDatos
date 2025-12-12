# Lista doble

# Clase del nodo
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# Clase de la lista doble
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_inicio(self, dato):
        nuevo = NodoDoble(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            return

        nuevo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo
        self.cabeza = nuevo


    def insertar_al_final(self, dato):
        nuevo = NodoDoble(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            return
        
        self.cola.siguiente = nuevo
        nuevo.anterior = self.cola
        self.cola = nuevo

    def imprimir_inicio_final(self):
        actual = self.cabeza
        print("Inicio al fin: ")

        while actual is not None:
            print(actual.dato, " <-> ", end= " ")
            actual = actual.siguiente

        print("None")

    def imprimir_final_inicio(self):
        actual = self.cola
        print("Fin al inicio: ")

        while actual is not None:
            print(actual.dato, " <-> ", end= " ")
            actual = actual.anterior
        
        print("None")


lista = ListaDoble()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(5)
lista.insertar_al_inicio(8)
lista.insertar_al_inicio(13)
lista.insertar_al_final(21)
lista.insertar_al_final(34)
lista.imprimir_inicio_final()
lista.imprimir_final_inicio()





