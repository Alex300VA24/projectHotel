from PyQt6.QtWidgets import QWidget  # Clase base para la vista
from .Ui_Form_Ventana_Principal import Ui_Form_Ventana_Principal  # Importa la clase generada automáticamente

class FormVentanaPrincipal(QWidget, Ui_Form_Ventana_Principal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz de usuario generada por Qt Designer