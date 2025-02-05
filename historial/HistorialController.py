class HistorialController:
    def __init__(self, historial_model):
        self.historial_model = historial_model

    def obtener_datos_historial(self):
        # Obtener datos del modelo
        return self.historial_model.obtener_historial_reservas()

    def actualizar_estado_reserva(self, id_reserva, nuevo_estado):
        # Llamar al modelo para actualizar la base de datos
        self.historial_model.actualizar_estado_reserva(id_reserva, nuevo_estado)
