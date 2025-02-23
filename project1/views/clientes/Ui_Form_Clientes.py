from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (
    QTableWidgetItem, QVBoxLayout, QPushButton, QWidget, QMessageBox, QLabel
)

from controllers.reservar_controller import ReservarController
from controllers.servicio_controller import ServicioController


class Ui_Form_Clientes(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(242, 242, 242);\n"
"}")
        self.table_historial = QtWidgets.QTableWidget(parent=Form)
        self.table_historial.setGeometry(QtCore.QRect(20, 180, 761, 371))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.table_historial.setFont(font)
        self.table_historial.setStyleSheet("background-color: #F9F9F9; /* Fondo del encabezado */")
        self.table_historial.setRowCount(14)
        self.table_historial.setObjectName("table_historial")
        self.table_historial.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        item.setFont(font)
        self.table_historial.setItem(0, 0, item)
        self.table_historial.horizontalHeader().setCascadingSectionResizes(True)
        self.table_historial.horizontalHeader().setDefaultSectionSize(117)
        self.table_historial.horizontalHeader().setStretchLastSection(True)
        self.btn_regresar = QtWidgets.QPushButton(parent=Form)
        self.btn_regresar.setGeometry(QtCore.QRect(20, 140, 31, 24))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_regresar.setFont(font)
        self.btn_regresar.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"}\n"
"")
        self.btn_regresar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/boton-volver.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_regresar.setIcon(icon)
        self.btn_regresar.setIconSize(QtCore.QSize(24, 24))
        self.btn_regresar.setObjectName("btn_regresar")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("views/ui\\../../resources/images/logo.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 801, 141))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.514, y1:0.0343182, x2:0.500554, y2:0.727, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.btn_consultar = QtWidgets.QPushButton(parent=Form)
        self.btn_consultar.setGeometry(QtCore.QRect(684, 560, 101, 24))
        self.btn_consultar.setObjectName("btn_consultar")
        self.btn_consultar.clicked.connect(self.consultar_registro)
        self.label_3.raise_()
        self.table_historial.raise_()
        self.btn_regresar.raise_()
        self.label_6.raise_()
        self.btn_consultar.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.dynamic_window = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.table_historial.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.table_historial.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre Completo"))
        item = self.table_historial.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Celular"))
        __sortingEnabled = self.table_historial.isSortingEnabled()
        self.table_historial.setSortingEnabled(False)
        self.table_historial.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Form", "Clientes Registrados"))
        self.btn_consultar.setText(_translate("Form", "Consultar Cliente"))
        
    #Método para llenar la tabla con la información que le manda el controlador clientes_controller
    def llenar_tabla(self, data):        
        fila = 0
        self.table_historial.setRowCount(len(data))
        for item in data:
            self.table_historial.setItem(fila, 0, QTableWidgetItem(str(item[0])))
            nombre_completo = item[1] + ' '
            nombre_completo += item[2] + ' '
            nombre_completo += item[3]
            self.table_historial.setItem(fila, 1, QTableWidgetItem(nombre_completo))            
            self.table_historial.setItem(fila, 2, QTableWidgetItem(item[7]))
            fila += 1

    def consultar_registro(self):
        registro_seleccionado = self.table_historial.selectedItems()
        
        if not registro_seleccionado:
            QMessageBox.warning(self.table_historial, "Advertencia", "Por favor, selecciona un registro.")
            return        
        
        fila_seleccionada = self.table_historial.currentRow()
        id_ = self.table_historial.item(fila_seleccionada, 0).text()
        
        #Se consigue el precio de la reserva
        precio_reserva = ReservarController.conseguir_total_reserva(id_)
        
        #Se consigue los servicios
        resumen_servicio = ServicioController.conseguir_total_servicio(id_)
        
        #Se consiguen las ids de los servicios
        id_servicio = []
        for data in resumen_servicio:
            id_servicio.append(data[0])            
        
        nombre = self.table_historial.item(fila_seleccionada, 1).text()
        celular = self.table_historial.item(fila_seleccionada, 2).text()
        self.open_dynamic_window(id_, nombre, celular, precio_reserva, resumen_servicio, id_servicio)
    
    def open_dynamic_window(self, id_, nombre, celular, precio_reserva, resumen_servicio, id_servicio):
        """Abre una nueva ventana dinámica con la información seleccionada."""
        if self.dynamic_window is not None:
            self.dynamic_window.close()  # Cierra cualquier ventana previa

        self.dynamic_window = QWidget()
        self.dynamic_window.setWindowTitle("Información del Registro")
        self.dynamic_window.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout(self.dynamic_window)
        layout.addWidget(QLabel(f"ID: {id_}"))
        layout.addWidget(QLabel(f"Nombre: {nombre}"))
        layout.addWidget(QLabel(f"Celular: {celular}"))        
        layout.addWidget(QLabel("Resumen de los servicios: "))
        
        total_servicio = 0
        for dato_servicio in resumen_servicio:
            layout.addWidget(QLabel('\t' + str(dato_servicio[1]) + ' - ' + str(dato_servicio[2]) + ' - S/.' + str(dato_servicio[3])))
            layout.addWidget(QLabel('\t' + "Detalles: "))
            total_servicio += dato_servicio[3]                        
            
        layout.addWidget(QLabel(f"Total de los servicios solicitados: S/.{total_servicio}"))
        layout.addWidget(QLabel(f"Total de la reserva: S/.{precio_reserva}"))
        
        total_estadia = float(precio_reserva) + float(total_servicio)
        layout.addWidget(QLabel(f"Coste total: S/.{total_estadia}"))
        
        
        from controllers.clientes_controller import ClientesController
        # El botón para generar el PDF
        self.btn_generar_pdf = QPushButton("Generar PDF", self.dynamic_window)
        self.btn_generar_pdf.clicked.connect(lambda: ClientesController.generar_pdf(self, nombre, celular, precio_reserva, resumen_servicio, id_servicio))
        layout.addWidget(self.btn_generar_pdf)

        self.dynamic_window.show()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Clientes()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())