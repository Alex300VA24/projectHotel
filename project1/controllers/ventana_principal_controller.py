from PyQt6.QtWidgets import QWidget  # type:ignore

from models.model import Habitacion
from views.ventana_principal.Ui_Form_Ventana_Principal import Ui_Form_Ventana_Principal


class VentanaPrincipalController:
    def __init__(self):
        self.ventana_principal = QWidget()  # Guardamos la instancia de la vista (login)
        self.ui = (
            Ui_Form_Ventana_Principal()
        )  # Guardamos la instancia de la vista (login)
        self.ui.setupUi(self.ventana_principal)
        self.ventana_login = None

        self.ui.btn_salir.clicked.connect(
            self.regresar_login
        )  # Conectamos el botón de salir
        self.ui.btn_servicio.clicked.connect(
            self.abrir_ventana_servicio
        )  # Conectamos el botón de servicio
        self.ui.btn_habitaciones.clicked.connect(
            self.abrir_ventana_habitaciones
        )  # Conectamos el botón de habitaciones
        self.ui.btn_clientes.clicked.connect(
            self.abrir_ventana_clientes
        )  # Conectamos el botón de clientes
        self.ui.btn_reservar.clicked.connect(
            self.abrir_ventana_reservar
        )  # Conectamos el botón de reservar
        self.ui.btn_historial.clicked.connect(
            self.abrir_ventana_historial
        )  # Conectamos el botón de historial de reservas

    # Ventana Servicio
    def abrir_ventana_servicio(self):
        self.ventana_principal.hide()
        self.abrir_servicio()

    def abrir_servicio(self):
        if self.servicio_controller:
            self.servicio_controller.mostrar_ventana()

    # Ventana Habitaciones
    def abrir_ventana_habitaciones(self):
        self.ventana_principal.hide()
        self.abrir_habitacion()

    def abrir_habitacion(self):
<<<<<<< HEAD
        if self.habitaciones_controller:
            self.habitaciones_controller.mostrar_ventana()
            #Se llama al método estado_habitacion de la clase Habitación para que jale los registros
            #únicamente cuando se le de el botón, y luego se envía la query al método habitaciones_disponibles
            #del controlador habitaciones_controller
            self.habitaciones_controller.habitaciones_disponibles(Habitacion.estado_habitacion())
=======
        if self.servicio_controller:
            self.servicio_controller.mostrar_ventana()
>>>>>>> 36a23c6 (Algo de cambios en los modelos)

    # Ventana Clientes
    def abrir_ventana_clientes(self):
        self.ventana_principal.hide()
        self.abrir_clientes()

    def abrir_clientes(self):
        if self.clientes_controller:
            self.clientes_controller.mostrar_ventana()

    # Ventana Reservar
    def abrir_ventana_reservar(self):
        self.ventana_principal.hide()
        self.abrir_reservar()

    def abrir_reservar(self):
        if self.reservar_controller:
            self.reservar_controller.mostrar_ventana()

<<<<<<< HEAD
    # Ventana Historial
=======
            # Ventana Historial

>>>>>>> 36a23c6 (Algo de cambios en los modelos)
    def abrir_ventana_historial(self):
        self.ventana_principal.hide()
        self.abrir_historial()

    def abrir_historial(self):
        if self.historial_controller:
            self.historial_controller.mostrar_ventana()

    # Cerrar sesion
    def regresar_login(self):
        self.ventana_principal.hide()
        if self.login_controller:
            self.login_controller.mostrar_ventana()

    # Abrir la ventana
    def mostrar_ventana(self):
        self.ventana_principal.show()
