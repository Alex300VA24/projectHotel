from PyQt6.QtWidgets import QWidget  # Clase base para la vista
from .Ui_Form_Login import Ui_Form_Login  # Importa la clase generada automáticamente

class FormLogin(QWidget, Ui_Form_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz de usuario generada por Qt Designer
