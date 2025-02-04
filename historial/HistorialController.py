class HistorialController:
    def __init__(self, historial_model):
        self.historial_model = historial_model

    def obtener_datos_historial(self):
        # Obtener datos del modelo
        datos_historial = self.historial_model.obtener_historial_reservas()
        return datos_historial