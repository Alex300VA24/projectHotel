from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QComboBox, QMessageBox
from models.historial import Historial
class Ui_Form_Historial(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("QWidget{background-color: rgb(242, 242, 242);}")

        self.table_historial = QtWidgets.QTableWidget(parent=Form)
        self.table_historial.setGeometry(QtCore.QRect(20, 180, 761, 401))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.table_historial.setFont(font)
        self.table_historial.setStyleSheet(""
            "QTableWidget {"
            "background-color: #F9F9F9;"
            "border: 1px solid #B0BEC5;"
            "gridline-color: #B0BEC5;"
            "}" 
            "QHeaderView::section {"
            "background-color: #546E7A;"
            "color: white;"
            "padding: 5px;"
            "border: 1px solid #37474F;"
            "}" 
            "QTableWidget::item:selected {"
            "background-color: #B0BEC5;"
            "color: black;"
            "}" 
        "")
        self.table_historial.setRowCount(0)
        self.table_historial.setColumnCount(7)
        headers = ["ID Cliente", "Nombre Completo", "Fecha Salida", "Estado", "N° de Habitación", "Tipo de Habitación", "Monto"]
        self.table_historial.setHorizontalHeaderLabels(headers)
        self.table_historial.horizontalHeader().setStretchLastSection(True)

    def llenar_tabla(self, data, controller):
        self.table_historial.setRowCount(len(data))
        self.controller = controller
        
        for fila, item in enumerate(data):
            print(f"Fila {fila} - Datos obtenidos: {item}")

            self.table_historial.setItem(fila, 0, QTableWidgetItem(str(item["idCliente"])))
            self.table_historial.setItem(fila, 1, QTableWidgetItem(item["nombre_completo"]))
            self.table_historial.setItem(fila, 2, QTableWidgetItem(str(item["fecha_salida"])))
            self.table_historial.setItem(fila, 4, QTableWidgetItem(item["numero_habitacion"]))
            self.table_historial.setItem(fila, 5, QTableWidgetItem(item["tipo_habitacion"]))
            self.table_historial.setItem(fila, 6, QTableWidgetItem(str(item["monto"])))
            
            combo = QComboBox()
            opciones = ["Pagada", "Pendiente", "Cancelada"]
            combo.addItems(opciones)
            estado_actual = item.get("estado_reserva", "Pendiente").capitalize()
            
            print(f"Fila {fila} - Estado corregido: {estado_actual}")
            
            if estado_actual in opciones:
                combo.setCurrentIndex(opciones.index(estado_actual))
            else:
                print(f"Advertencia: Estado '{estado_actual}' no válido en fila {fila}")
            
            combo.setStyleSheet(""
                "QComboBox {"
                "background-color: white;"
                "border: 1px solid #B0BEC5;"
                "padding: 5px;"
                "}" 
                "QComboBox QAbstractItemView {"
                "border: 1px solid #37474F;"
                "selection-background-color: #B0BEC5;"
                "}"
            "")
            
            combo.currentIndexChanged.connect(lambda _, row=fila, cbox=combo: self.confirmar_cambio_estado(row, cbox))
            self.table_historial.setCellWidget(fila, 3, combo)

    def confirmar_cambio_estado(self, fila, combo):
        nuevo_estado = combo.currentText()
        id_cliente = self.table_historial.item(fila, 0).text()
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Confirmar Cambio")
        mensaje.setText(f"¿Seguro que deseas cambiar el estado a '{nuevo_estado}'?")
        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        mensaje.setStyleSheet(""
            "QMessageBox {"
            "background-color: #ECEFF1;"
            "border: 1px solid #B0BEC5;"
            "}" 
            "QPushButton {"
            "background-color: #546E7A;"
            "color: white;"
            "border-radius: 5px;"
            "padding: 5px;"
            "}" 
            "QPushButton:hover {"
            "background-color: #78909C;"
            "}" 
        "")
        
        respuesta = mensaje.exec()
        
        if respuesta == QMessageBox.StandardButton.Yes:
            self.controller.actualizar_estado_reserva(id_cliente, nuevo_estado)
        else:
            combo.blockSignals(True)
            combo.setCurrentIndex(combo.findText(self.table_historial.item(fila, 3).text()))
            combo.blockSignals(False)

if __name__ == "__main__":
    import sys
    from controllers.historial_controller import HistorialController
    from historial import Historial

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'Hotel'
    }
    historial_model = Historial(db_config)
    historial_controller = HistorialController(historial_model)
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Historial()
    ui.setupUi(Form)
    
    data = historial_controller.obtener_datos_historial()
    ui.llenar_tabla(data, historial_controller)
    
    Form.show()
    sys.exit(app.exec())
