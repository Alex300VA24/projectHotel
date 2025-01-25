import sys
from PyQt6.QtWidgets import QApplication  # type: ignore

from controllers.login_controller import LoginController  # Importa el controlador
from controllers.ventana_principal_controller import VentanaPrincipalController
from controllers.servicio_controller import ServicioController
from controllers.habitaciones_controller import HabitacionesController
from controllers.clientes_controller import ClientesController
from controllers.reservar_controller import ReservarController

import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)


def main():
    app = QApplication(sys.argv)

    # Crear los controladores
    login_controller = LoginController()
    ventana_principal_controller = VentanaPrincipalController()
    servicio_controller = ServicioController()
    habitaciones_controller = HabitacionesController()
    clientes_controller = ClientesController()
    reservar_controller = ReservarController()

    # Configurar referencias cruzadas
    login_controller.ventana_principal_controller = ventana_principal_controller

    ventana_principal_controller.login_controller = login_controller
    ventana_principal_controller.servicio_controller = servicio_controller
    ventana_principal_controller.habitaciones_controller = habitaciones_controller
    ventana_principal_controller.clientes_controller = clientes_controller
    ventana_principal_controller.reservar_controller = reservar_controller

    servicio_controller.ventana_principal_controller = ventana_principal_controller
    habitaciones_controller.ventana_principal_controller = ventana_principal_controller
    clientes_controller.ventana_principal_controller = ventana_principal_controller
    reservar_controller.ventana_principal_controller = ventana_principal_controller

    # Mostrar la ventana de login
    login_controller.mostrar_ventana()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
