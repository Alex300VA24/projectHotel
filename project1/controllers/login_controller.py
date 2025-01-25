from PyQt6.QtWidgets import QMessageBox
from models.administrador import Administrador #type:ignore
from controllers.ventana_principal_controller import VentanaPrincipalController
from views.ventana_principal.FormVentanaPrincipal import FormVentanaPrincipal
from models.db import DBConnection

class LoginController:
    def __init__(self, login_view):
        self.ui = login_view  # Guardamos la instancia de la vista (login)
        self.ui.setupUi(self.ui)
        self.ui.btn_ingresar.clicked.connect(self.login)  # Conectamos el botón de login
        

    def login(self):
        try:
            # Obtenemos los datos de la interfaz
            correo = self.ui.txt_correo.text().strip()
            password = self.ui.txt_contrasena.text().strip()

            if not correo or not password:
                self.mostrar_error('Usuario o contraseña no pueden estar vacíos.')
                return

            if '@' not in correo or '.' not in correo:
                self.mostrar_error('El correo electrónico no es válido.')
                return

            if Administrador.validar_usuario(correo, password):
                self.mostrar_mensaje('Iniciaste sesión con éxito')
            else:
                self.mostrar_error('Usuario o contraseña incorrecta')

        except Exception as e:
            self.mostrar_error(f"Ocurrió un error: {e}")

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self.ui, "Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self.ui, 'Mensaje de Inicio de Sesión', mensaje)
        self.ui.close()  # Cerramos la ventana de login
        self.abrir_ventana_principal()  # Abrimos la ventana principal

    def abrir_ventana_principal(self):
        ventana_principal = FormVentanaPrincipal()
        self.ventana_principal_view = ventana_principal
        #self.ventana_principal_view.setupUi(self.ventana_principal_view)
        ventana_principal_controller = VentanaPrincipalController(self.ventana_principal_view, self.ui)
        self.ventana_principal_view.show()

    '''def regresar_login(self):
        # Aquí deberías manejar la lógica para regresar al login
        # Esto puede implicar simplemente cerrar la ventana principal y abrir de nuevo la ventana de login
        self.ui_ventana_principal.close()
        self.ui.show()'''
    

