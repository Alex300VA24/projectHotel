from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

class Ui_Form_Clientes(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("QWidget{\n    background-color: rgb(242, 242, 242);\n}")
        self.table_historial = QtWidgets.QTableWidget(parent=Form)
        self.table_historial.setGeometry(QtCore.QRect(20, 180, 761, 401))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.table_historial.setFont(font)
        self.table_historial.setStyleSheet(
            "background-color: #F9F9F9; /* Fondo del encabezado */"
        )
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
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(
            QtGui.QPixmap("views/ui\\../../resources/images/logo.jpg")
        )
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
        self.label_3.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.514, y1:0.0343182, x2:0.500554, y2:0.727, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.table_historial.raise_()
        self.btn_regresar.raise_()
        self.label_6.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

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
    
    #Método para llenar la tabla con la información que le manda el controlador clientes_controller
    def llenar_tabla(self, data):
        print(data)
        
        fila = 0
        self.table_historial.setRowCount(len(data))
        for item in data:
            self.table_historial.setItem(fila, 0, QTableWidgetItem(str(item[0])))
            nombre_completo = item[1] + ' '
            nombre_completo += item[2] + ' '
            nombre_completo += item[3]
            self.table_historial.setItem(fila, 1, QTableWidgetItem(nombre_completo))            
            self.table_historial.setItem(fila, 2, QTableWidgetItem(item[4]))
            fila += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Clientes()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
