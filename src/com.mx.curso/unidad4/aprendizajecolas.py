# Cola de tareas

class SolicitudNodo:
    def __init__(self, tarea):
        self.contenido = tarea
        self.proximo = None

class GestorTraficoIA:
    def __init__(self):
        self.frente = None
        self.final = None
        self.contador = 0

    def encolar_peticion(self, descripcion):
        nueva_peticion = SolicitudNodo(descripcion)
        if self.final is None:
            self.frente = self.final = nueva_peticion
        else:
            self.final.proximo = nueva_peticion
            self.final = nueva_peticion
        self.contador += 1

    def atender_peticion(self):
        if self.frente is None:
            return None
        
        atendida = self.frente.contenido
        self.frente = self.frente.proximo
        
        if self.frente is None:
            self.final = None
            
        self.contador -= 1
        return atendida

    def obtener_pendientes(self):
        tareas = []
        actual = self.frente
        while actual:
            tareas.append(actual.contenido)
            actual = actual.proximo
        return tareas

# Lógica de Procesamiento
buffer_ia = GestorTraficoIA()

# Carga de trabajo inicial
tareas_iniciales = [
    "Analizar sentimientos en Tweet",
    "Consulta filosófica: ¿Qué es la vida?",
    "Resumen de artículo científico",
    "Generación de imagen: Noche estrellada",
    "Corrección gramatical de documento",
    "Plan de estudios: Inglés"
]

for t in tareas_iniciales:
    buffer_ia.encolar_peticion(t)

print(f"\nEstado del Buffer: {buffer_ia.obtener_pendientes()}")
print(f"Total de peticiones en espera: {buffer_ia.contador}")
print("\n---- Despachando solicitudes (Orden FIFO) ----")

while buffer_ia.frente:
    total_antes = buffer_ia.contador
    tarea_actual = buffer_ia.atender_peticion()
    print(f">> Ejecutando: {tarea_actual}")
    print(f"   [Pendientes: {buffer_ia.contador}]")

print("\nEstatus final: Todas las solicitudes han sido procesadas.")