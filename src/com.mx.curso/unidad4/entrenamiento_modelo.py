# Importamos la versión renovada de la pila
from BusquedaProfunda import AlmacenLIFO 

class AuditoriaEntrenamiento:
    
    print("\nINICIO: Ajuste de Hiperparámetros del Modelo")

    # Inicializamos la bitácora de cambios
    historial_cambios = AlmacenLIFO()

    # Registramos una serie de configuraciones (Push)
    configuraciones = [
        "tasa_aprendizaje = 0.01",
        "epocas = 50",
        "tamaño_lote = 32",
        "optimizador = Adam_Optim",
        "capa_dropout = 0.3"
    ]

    for ajuste in configuraciones:
        print(f"REGISTRANDO -> {ajuste}")
        historial_cambios.apilar(ajuste)
        historial_cambios.visualizar_pila()

    print("\nFASE: Reversión de Cambios (Undo)")
    
    # Simulamos deshacer las últimas dos acciones (Pop)
    for _ in range(2):
        eliminado = historial_cambios.desapilar()
        print(f"REVERTIDO: Se ha descartado el ajuste -> {eliminado}")
        historial_cambios.visualizar_pila()

print("\nAuditoría finalizada con éxito.")