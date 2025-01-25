from PyQt6.QtWidgets import QMainWindow
from view.second_window_ui import Ui_SecondWindow

class SecondaryController:
    def __init__(self):
        self.secondary_window = QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.secondary_window)
        self.main_controller = None  # Referencia al controlador principal

        # Conectar el botón para volver a la ventana principal
        self.ui.btn_regresar.clicked.connect(self.open_main_window)

    def open_main_window(self):
        self.secondary_window.hide()  # Ocultar la ventana secundaria
        if self.main_controller:
            self.main_controller.show_window()  # Mostrar la principal

    def show_window(self):
        self.secondary_window.show()
