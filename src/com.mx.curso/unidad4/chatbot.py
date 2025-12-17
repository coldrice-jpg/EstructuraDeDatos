class MensajeNodo:
    
    def __init__(self, contenido):
        self.texto = contenido
        self.link = None

class HistorialConversacion:
    
    def __init__(self):
        self.inicio = None

    def registrar_al_principio(self, texto):
        
        nuevo_mensaje = MensajeNodo(texto)
        nuevo_mensaje.link = self.inicio
        self.inicio = nuevo_mensaje

    def _añadir_al_final(self, cadena_texto):
        
        nuevo_bloque = MensajeNodo(cadena_texto)
        
        if not self.inicio:
            self.inicio = nuevo_bloque
            return
        
        puntero = self.inicio
        while puntero.link:
            puntero = puntero.link
        puntero.link = nuevo_bloque

    def entrada_usuario(self, comentario):
        
        formato = f"[USUARIO]: {comentario}"
        self._añadir_al_final(formato)
        print(f"Log -> Usuario: {comentario}")

    def respuesta_ia(self, comentario):
        
        formato = f"[BOT]: {comentario}"
        self._añadir_al_final(formato)
        print(f"Log -> Bot: {comentario}")
            
    def desplegar_historial(self):
        
        print("\n--- REPRODUCCIÓN DEL CHAT ---")
        cursor = self.inicio
        while cursor:
            print(f"| {cursor.texto} |", end=" --> ")
            cursor = cursor.link
        print("FINAL DEL REGISTRO\n")

# --- Ejecución del Programa ---
if __name__ == "__main__":
    ai = HistorialConversacion()

    ai.entrada_usuario("Hola.")
    ai.respuesta_ia("¿En qué puedo ayudarte hoy?")
    
    ai.desplegar_historial()