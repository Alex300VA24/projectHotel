from PyQt6.QtWidgets import QMessageBox #type:ignore


class Servicio_Controller:
    def __init__(self, ui_form_ventana_principal):
        self.ui = ui_form_ventana_principal  # Guardamos la instancia de la vista (login)
        # self.ui.btn_ingresar_servicio.clicked.connect(self.abrir_servicio)
    