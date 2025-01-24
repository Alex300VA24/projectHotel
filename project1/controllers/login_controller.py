from PyQt6.QtWidgets import QMessageBox
from views.ventana_principal import Form_Ventana_Principal as VentanaPrincipal
from models.db import DBConnection

class Login_Controller:
    def __init__(self, ui_form_login):
        self.ui = ui_form_login  # Guardamos la instancia de la vista (login)
        self.ui.btn_ingresar.clicked.connect(self.login)  # Conectamos el botón de login

    def login(self):
        try:
            # Obtenemos los datos de la interfaz
            correo = self.ui.txt_correo.text()
            password = self.ui.txt_contrasena.text()

            # Validación de los datos
            if correo == '' or password == '':
                self.mostrar_error('Usuario o contraseña no pueden estar vacíos.')
            else:
                # Crear una instancia de DBConnection
                db = DBConnection()

                # Conectar a la base de datos
                db.connect()

                # Consulta para verificar si el usuario y la contraseña coinciden
                query = "SELECT * FROM administrador WHERE correo = %s AND contrasenia = %s"
                result = db.query(query, (correo, password))

                # Si se encuentra el usuario
                if result:
                    self.mostrar_mensaje('Iniciaste sesión con éxito')
                else:
                    self.mostrar_error('Usuario o contraseña incorrecta')

                # Desconectar después de la consulta
                db.disconnect()

        except Exception as e:
            self.mostrar_error(f"Ocurrió un error: {e}")

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self.ui, "Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self.ui, 'Mensaje de Inicio de Sesión', mensaje)
        self.ui.close()  # Cerramos la ventana de login
        self.abrir_ventana_principal()  # Abrimos la ventana principal

    def abrir_ventana_principal(self):
        ventana_principal = VentanaPrincipal()
        self.ui_ventana_principal = ventana_principal
        self.ui_ventana_principal.setupUi(self.ui_ventana_principal)
        self.ui_ventana_principal.btn_salir.clicked.connect(self.regresar_login)
        self.ui_ventana_principal.show()

    def regresar_login(self):
        # Aquí deberías manejar la lógica para regresar al login
        # Esto puede implicar simplemente cerrar la ventana principal y abrir de nuevo la ventana de login
        self.ui_ventana_principal.close()
        self.ui.show()
