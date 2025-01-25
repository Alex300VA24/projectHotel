from PyQt6.QtWidgets import QMessageBox, QWidget #type:ignore

from views.ventana_principal.Ui_Form_Ventana_Principal import Ui_Form_Ventana_Principal


class VentanaPrincipalController:
    def __init__(self):
        self.ventana_principal = QWidget()  # Guardamos la instancia de la vista (login)
        self.ui = Ui_Form_Ventana_Principal()  # Guardamos la instancia de la vista (login)
        self.ui.setupUi(self.ventana_principal)
        self.ventana_login = None



        self.ui.btn_salir.clicked.connect(self.regresar_login)  # Conectamos el botón de salir
        self.ui.btn_servicio.clicked.connect(self.abrir_ventana_servicio) # Conectamos el botón de servicio

    

    def abrir_ventana_servicio(self):
        self.ventana_principal.hide()
        self.abrir_servicio()
    
    def abrir_servicio(self):
        if self.servicio_controller:
            self.servicio_controller.mostrar_ventana()
    
    def regresar_login(self):
        self.ventana_principal.hide()
        if self.login_controller:
            self.login_controller.mostrar_ventana()
    
    def mostrar_ventana(self):
        self.ventana_principal.show()
    


