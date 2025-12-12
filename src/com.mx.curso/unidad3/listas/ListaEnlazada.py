# Lista  enlazada en python

# Clase del nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Clase de la lista
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
    
    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza == None:
            self.cabeza = nuevo
            print("Insertar al final (lista vacia): ", dato)
            return

        actual = self.cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo
        print("Insertado al final ", dato)

    def imprimir_lista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, " -> ", end = " ")
            actual = actual.siguiente
        print("None")
    
lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(5)
lista.insertar_al_inicio(8)
lista.insertar_al_final(13)
lista.imprimir_lista()
