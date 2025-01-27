from PyQt6.QtWidgets import QWidget  # type:ignore
from views.clientes.Ui_Form_Clientes import Ui_Form_Clientes


class ClientesController:
    def __init__(self):
        self.ventana_clientes = QWidget()
        self.ui = Ui_Form_Clientes()
        self.ui.setupUi(self.ventana_clientes)
        self.ventana_principal_controller = None

        self.ui.btn_regresar.clicked.connect(self.regresar_ventana_prinicipal)

    def regresar_ventana_prinicipal(self):
        self.ventana_clientes.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_ventana(self):
        self.ventana_clientes.show()
        
    #La informacion lo reenvia al Form
    def clientes_registrados(self, data):
        self.ui.llenar_tabla(data)
