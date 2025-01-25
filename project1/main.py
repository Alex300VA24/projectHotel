import sys
from PyQt6.QtWidgets import QApplication  # type: ignore

from controllers.login_controller import LoginController  # Importa el controlador
from controllers.ventana_principal_controller import VentanaPrincipalController
from controllers.servicio_controller import ServicioController

import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    app = QApplication(sys.argv)
    
    # Crear los controladores
    login_controller = LoginController()
    ventana_principal_controller = VentanaPrincipalController()
    servicio_controller = ServicioController()


    # Configurar referencias cruzadas
    login_controller.ventana_principal_controller = ventana_principal_controller
    ventana_principal_controller.login_controller = login_controller
    ventana_principal_controller.servicio_controller = servicio_controller
    servicio_controller.ventana_principal_controller = ventana_principal_controller
    

    # Mostrar la ventana de login
    login_controller.mostrar_ventana()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
