from PyQt6.QtWidgets import QWidget  # type:ignore
from views.habitaciones.Ui_Form_Habitaciones import Ui_Form_Habitaciones


class HabitacionesController:
    def __init__(self):
        self.ventana_habitaciones = QWidget()
        self.ui = Ui_Form_Habitaciones()
        self.ui.setupUi(self.ventana_habitaciones)
        self.ventana_principal_controller = None

        self.ui.btn_regresar.clicked.connect(self.regresar_ventana_prinicipal)

    def regresar_ventana_prinicipal(self):
        self.ventana_habitaciones.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_ventana(self):
        self.ventana_habitaciones.show()
