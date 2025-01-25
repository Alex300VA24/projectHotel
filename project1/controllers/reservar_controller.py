from PyQt6.QtWidgets import QWidget  # type:ignore
from views.reservar.Ui_Form_Reservar_Habitacion import Ui_Form_Reservar_Habitacion


class ReservarController:
    def __init__(self):
        self.ventana_reservar = QWidget()
        self.ui = Ui_Form_Reservar_Habitacion()
        self.ui.setupUi(self.ventana_reservar)
        self.ventana_principal_controller = None

        self.ui.btn_cancelar.clicked.connect(self.regresar_ventana_prinicipal)

    def regresar_ventana_prinicipal(self):
        self.ventana_reservar.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_ventana(self):
        self.ventana_reservar.show()
