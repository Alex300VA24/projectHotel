from principal import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox  # type: ignore
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_procesar.clicked.connect(self.realizar_operacion)

    def realizar_operacion(self):
        try:

            num1 = float(self.ui.numero1.toPlainText())
            num2 = float(self.ui.numero2.toPlainText())

            operacion = self.ui.operaciones_cb.currentText()

            # Realizar la operación seleccionada
            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero.")
                resultado = num1 / num2
            else:
                raise ValueError("Operación no válida.")

            self.ui.resultado.setText(str(resultado))

        except ValueError:
            self.mostrar_error("Por favor, ingresa números válidos.")
        except ZeroDivisionError as e:
            self.mostrar_error(str(e))

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
