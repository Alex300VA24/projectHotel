import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_controller import MainController
from controllers.secondary_controller import SecondaryController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear los controladores
    main_controller = MainController()
    secondary_controller = SecondaryController()

    # Configurar referencias cruzadas
    main_controller.secondary_controller = secondary_controller
    secondary_controller.main_controller = main_controller

    # Mostrar la ventana principal
    main_controller.show_window()

    sys.exit(app.exec())
