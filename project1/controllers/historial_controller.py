from PyQt6.QtWidgets import QWidget  # type:ignore
from views.historial.Ui_Form_Historial import Ui_Form_Historial

class HistorialController:
    def __init__(self):
        self.ventana_historial = QWidget()
        self.ui = Ui_Form_Historial()
        self.ui.setupUi(self.ventana_historial)
        self.ventana_principal_controller = None

        self.ui.btn_regresar.clicked.connect(self.regresar_ventana_prinicipal)

    def obtener_datos_historial(self):
        # Obtener datos del modelo
        return self.historial_model.obtener_historial_reservas()

    def actualizar_estado_reserva(self, id_reserva, nuevo_estado):
        # Llamar al modelo para actualizar la base de datos
        self.historial_model.actualizar_estado_reserva(id_reserva, nuevo_estado)

    def regresar_ventana_prinicipal(self):
        self.ventana_historial.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_ventana(self):
        self.ventana_historial.show()