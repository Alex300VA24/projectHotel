from views.login import Ui_Form
from views.ventana_principal import Ui_Form_Ventana_Principal as VentanaPrincipal
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox  # type: ignore
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btn_ingresar.clicked.connect(self.login)
        
        

    def login(self):
        try:

            usuario = self.ui.txt_correo.text()
            password = self.ui.txt_contrasena.text()

            # Realizar la operación seleccionada
            if usuario == '' and password == '':
                self.mostrar_mensaje('Iniciaste sesion con éxito')
            else:
                self.mostrar_error('Usuario o contraseña incorrecta')

        except Exception as e:
            self.mostrar_error(f"Ocurrio un error: {e}")

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self, 'Mensaje de Inicio de Sesion', mensaje)
        # Quiero que la ventana donde estamos se cierre y se vizualice ventana_principal
        self.close()
        self.abrir_ventana_principal()

    def abrir_ventana_principal(self):
        self.ventana_principal = QMainWindow()
        self.ui_ventana_principal = VentanaPrincipal()
        self.ui_ventana_principal.setupUi(self.ventana_principal)
        self.ui_ventana_principal.btn_salir.clicked.connect(self.regresar_login)
        self.ventana_principal.show()
    

    # Quiero ahora que el boton de ventana principal me regrese al login
    def regresar_login(self):
        self.ventana_principal.close()
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
