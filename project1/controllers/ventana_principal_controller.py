from PyQt6.QtWidgets import QMessageBox
from views.servicio_habitacion import Form_Servicio as VentanaServicio


class Ventana_Principal_Controller:
    def __init__(self, ui_form_ventana_principal):
        self.ui = ui_form_ventana_principal  # Guardamos la instancia de la vista (login)
        self.ui.setupUi(self.ui)
        self.ui.btn_salir.clicked.connect(self.regresar_login)
        self.ui.btn_servicio.clicked.connect(self.abrir_ventana_servicio) # Conectamos el botón de servicio
    

    def abrir_ventana_servicio(self):
        self.ui.close()
        self.abrir_servicio()

    def abrir_servicio(self):
        ventana_servicio = VentanaServicio()
        self.ui_ventana_servicio = ventana_servicio
        self.ui_ventana_servicio.setupUi(self.ui_ventana_servicio)
        #cerramos ventana principal
        #self.ui_ventana_principal.btn_salir.clicked.connect(self.regresar_login)
        self.ui_ventana_servicio.show()
    
    def regresar_login(self):
        self.ui.close()
    


