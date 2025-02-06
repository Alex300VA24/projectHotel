from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QComboBox, QMessageBox
from views.historial.Ui_Form_Historial import Ui_Form_Historial
from models.reserva import Reserva

class HistorialController:
    def __init__(self):
        self.ventana_historial = QWidget()
        self.ui = Ui_Form_Historial()
        self.ui.setupUi(self.ventana_historial)
        self.ventana_principal_controller = None

        self.ui.btn_regresar.clicked.connect(self.regresar_ventana_prinicipal)

        self.cargar_datos_historial()

    def cargar_datos_historial(self):
        """Carga los datos del historial en la tabla"""
        datos = Reserva.obtener_historial_reservas()
        self.ui.table_historial_2.setRowCount(len(datos))

        for fila, reserva in enumerate(datos):
            for columna, valor in enumerate(reserva):
                if columna == 4:  # Columna del estado de la reserva
                    combo = QComboBox()
                    combo.addItems(["pagada", "cancelada", "pendiente"])
                    combo.setCurrentText(str(valor))  # Establecer estado actual
                    combo.currentIndexChanged.connect(lambda _, f=fila, c=columna: self.confirmar_cambio_estado(f, c))
                    self.ui.table_historial_2.setCellWidget(fila, columna, combo)
                else:
                    self.ui.table_historial_2.setItem(fila, columna, QTableWidgetItem(str(valor)))

    def confirmar_cambio_estado(self, fila, columna):
        """Muestra una ventana de confirmación antes de actualizar el estado"""
        combo = self.ui.table_historial_2.cellWidget(fila, columna)
        nuevo_estado = combo.currentText()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle("Confirmar cambio de estado")
        msg.setText(f"¿Estás seguro de actualizar el estado a '{nuevo_estado}'?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        respuesta = msg.exec()

        if respuesta == QMessageBox.StandardButton.Yes:
            id_reserva = self.ui.table_historial_2.item(fila, 0).text()  # Suponiendo que la columna 0 es el ID
            self.actualizar_estado_reserva(id_reserva, nuevo_estado)
        else:
            # Restaurar el estado anterior si cancela
            datos = Reserva.obtener_historial_reservas()
            combo.setCurrentText(datos[fila][4])

    def actualizar_estado_reserva(self, id_reserva, nuevo_estado):
        """Actualiza el estado en la base de datos"""
        try:
            Reserva.actualizar_estado_reserva(id_reserva, nuevo_estado)
            QMessageBox.information(self.ventana_historial, "Éxito", "Estado actualizado correctamente.")
        except Exception as e:
            QMessageBox.critical(self.ventana_historial, "Error", f"No se pudo actualizar: {e}")

    def regresar_ventana_prinicipal(self):
        self.ventana_historial.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_ventana(self):
        self.ventana_historial.show()
        self.cargar_datos_historial()  # Recargar datos al mostrar la ventana
