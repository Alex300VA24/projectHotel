from views.login import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox  # type: ignore
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_ingresar.clicked.connect(self.login)

    def login(self):
        try:

            usuario = self.ui.txt_usuario.text()
            password = self.ui.txt_password.text()

            # Realizar la operación seleccionada
            if usuario == 'alex300va24' and password == 'alex061123':
                self.mostrar_mensaje('Iniciaste sesion con éxito')
            else:
                self.mostrar_error('Usuario o contraseña incorrecta')

        except Exception as e:
            self.mostrar_error(f"Ocurrio un error: {e}")

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self, 'Mensaje de Inicio de Sesion', mensaje)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
