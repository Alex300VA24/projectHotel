from PyQt6.QtWidgets import QWidget  #type:ignore
from .servicio_habitacion import Ui_Form_Servicio  # Importa la clase generada automáticamente

class FormServicio(QWidget, Ui_Form_Servicio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz de usuario generada por Qt Designer