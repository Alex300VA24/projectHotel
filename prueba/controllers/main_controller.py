from PyQt6.QtWidgets import QMainWindow
from view.main_window_ui import Ui_MainWindow

class MainController:
    def __init__(self):
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.secondary_controller = None  # Referencia al controlador secundario

        # Conectar el botón para cambiar de ventana
        self.ui.btn_ingresar.clicked.connect(self.open_secondary_window)

    def open_secondary_window(self):
        self.main_window.hide()  # Ocultar la ventana principal
        if self.secondary_controller:
            self.secondary_controller.show_window()  # Mostrar la secundaria

    def show_window(self):
        self.main_window.show()
