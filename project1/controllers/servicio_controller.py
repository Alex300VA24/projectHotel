from PyQt6.QtWidgets import QWidget #type:ignore
from views.Ui_Form_Servicio import Ui_Form_Servicio

class ServicioController:
    def __init__(self):
        self.ventana_servicio = QWidget()
        self.ui = Ui_Form_Servicio()
        self.ui.setupUi(self.ventana_servicio)
        self.ventana_principal_controller = None

        self.ui.btn_guardar.clicked.connect(self.regresar_ventana_prinicipal)
    
    def regresar_ventana_prinicipal(self):
        self.ventana_servicio.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()
    
    def mostrar_ventana(self):
        self.ventana_servicio.show()
    