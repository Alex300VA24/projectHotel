from PyQt6.QtWidgets import QMessageBox, QWidget  # type:ignore
from models.administrador import Administrador  # type:ignore

from views.login.Ui_Form_Login import Ui_Form_Login


class LoginController:
    def __init__(self):
        self.ventana_login = QWidget()  # Guardamos la instancia de la vista (login)
        self.ui = Ui_Form_Login()
        self.ui.setupUi(self.ventana_login)
        self.ventana_principal_controller = None

        self.ui.btn_ingresar.clicked.connect(self.login)  # Conectamos el botón de login

    def login(self):
        try:
            # Obtenemos los datos de la interfaz
            correo = self.ui.txt_correo.text().strip()
            password = self.ui.txt_contrasena.text().strip()

            if not correo or not password:
                self.mostrar_error("Usuario o contraseña no pueden estar vacíos.")
                return

            if "@" not in correo or "." not in correo:
                self.mostrar_error("El correo electrónico no es válido.")
                return

            if Administrador.validar_usuario(correo, password):
                self.mostrar_mensaje("Iniciaste sesión con éxito")
            else:
                self.mostrar_error("Usuario o contraseña incorrecta")

        except Exception as e:
            self.mostrar_error(f"Ocurrió un error: {e}")

    def mostrar_ventana(self):
        self.ventana_login.show()

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self.ventana_login, "Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(
            self.ventana_login, "Mensaje de Inicio de Sesión", mensaje
        )
        self.ventana_login.hide()  # Cerramos la ventana de login
        self.abrir_ventana_principal()  # Abrimos la ventana principal

    def abrir_ventana_principal(self):
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()
