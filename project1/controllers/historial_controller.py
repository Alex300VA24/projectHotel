from PyQt6.QtWidgets import QWidget  # type:ignore
from views.historial.Ui_Form_Historial import Ui_Form_Historial

class HistorialController:
    def __init__(self):
        self.ventana_historial = QWidget()
        self.ui = Ui_Form_Historial()
        self.ui.setupUi(self.ventana_historial)
        self.ventana_principal_controller = None

        self.ui.btn_regresar.clicked.connect(self.regresar_ventana_prinicipal)

    def regresar_ventana_prinicipal(self):
        self.ventana_historial.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_ventana(self):
        self.ventana_historial.show()
