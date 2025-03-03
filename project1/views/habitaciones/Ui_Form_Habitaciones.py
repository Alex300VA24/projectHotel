from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem


class Ui_Form_Habitaciones(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("QWidget{\n    background-color: rgb(242, 242, 242);\n}")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 801, 141))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.514, y1:0.0343182, x2:0.500554, y2:0.727, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(
            QtGui.QPixmap("views/ui\\../../resources/images/logo.jpg")
        )
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.btn_regresar = QtWidgets.QPushButton(parent=Form)
        self.btn_regresar.setGeometry(QtCore.QRect(20, 140, 31, 24))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_regresar.setFont(font)
        self.btn_regresar.setStyleSheet(
            "QPushButton {\n"
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
            ""
        )
        self.btn_regresar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("views/ui\\../../resources/images/icons/boton-volver.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_regresar.setIcon(icon)
        self.btn_regresar.setIconSize(QtCore.QSize(24, 24))
        self.btn_regresar.setObjectName("btn_regresar")
        self.table_historial_2 = QtWidgets.QTableWidget(parent=Form)
        self.table_historial_2.setGeometry(QtCore.QRect(20, 180, 761, 391))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.table_historial_2.setFont(font)
        self.table_historial_2.setStyleSheet(
            "background-color: #F9F9F9; /* Fondo del encabezado */"
        )
        self.table_historial_2.setRowCount(14)
        self.table_historial_2.setObjectName("table_historial_2")
        self.table_historial_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(2, item)
        self.table_historial_2.horizontalHeader().setCascadingSectionResizes(True)
        self.table_historial_2.horizontalHeader().setDefaultSectionSize(117)
        self.table_historial_2.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Habitaciones Disponibles"))
        item = self.table_historial_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.table_historial_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "N° de Habitación"))
        item = self.table_historial_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tipo de habitación"))
    
    #Método para llenar la tabla con la información que le manda el controlador habitaciones_controller
    def llenar_tabla(self, data):
        habitaciones_disponibles = ()
        for item in data:
            if item[3] == 'disponible':
                habitaciones_disponibles += (item,)
        
        fila = 0
        self.table_historial_2.setRowCount(len(habitaciones_disponibles))
        for item in habitaciones_disponibles:
            self.table_historial_2.setItem(fila, 0, QTableWidgetItem(str(item[0])))
            self.table_historial_2.setItem(fila, 1, QTableWidgetItem(str(item[1])))
            if item[2] == 1:
                tipo_habitacion = "Simple"
            elif item[2] == 2:
                tipo_habitacion = "Doble"
            elif item[2] == 3:
                tipo_habitacion = "Matrimonial"
            else:
                tipo_habitacion = "Suite"
            self.table_historial_2.setItem(fila, 2, QTableWidgetItem(tipo_habitacion))
            fila += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Habitaciones()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
