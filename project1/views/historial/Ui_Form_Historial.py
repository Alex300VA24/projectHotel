# Form implementation generated from reading ui file 'views/ui/historial_reservaciones.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Historial(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 801, 141))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.514, y1:0.0343182, x2:0.500554, y2:0.727, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(350, 10, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("views/ui\\../../resources/images/logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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
        self.table_historial_2 = QtWidgets.QTableWidget(parent=Form)
        self.table_historial_2.setGeometry(QtCore.QRect(20, 180, 761, 401))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.table_historial_2.setFont(font)
        
        
        self.table_historial_2.setAlternatingRowColors(True)


        self.table_historial_2.setStyleSheet("background-color: #F9F9F9; /* Fondo del encabezado */")
        self.table_historial_2.setRowCount(14)
        self.table_historial_2.setColumnCount(8)
        self.table_historial_2.setObjectName("table_historial_2")
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        self.table_historial_2.setHorizontalHeaderItem(7, item)
        self.table_historial_2.horizontalHeader().setCascadingSectionResizes(True)
        self.table_historial_2.horizontalHeader().setDefaultSectionSize(117)
        self.table_historial_2.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Historial de Reservaciones"))
        item = self.table_historial_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.table_historial_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cliente"))
        item = self.table_historial_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Fecha de entrada"))
        item = self.table_historial_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Fecha de salida"))
        item = self.table_historial_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Estado"))
        item = self.table_historial_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "N° de Habitación"))
        item = self.table_historial_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Tipo de Habitación"))
        item = self.table_historial_2.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Monto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Historial()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
