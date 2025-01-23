# Form implementation generated from reading ui file 'views/ui/ventana_principal.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Ventana_Principal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 532)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 531))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("views/ui\\../../resources/images/hotel_imagen.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(420, 80, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(30)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 180, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/reservacion.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 360, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/habitacion.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 270, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.pushButton_3.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/cliente.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 270, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.pushButton_4.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/historial.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 180, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/servicio.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.btn_salir = QtWidgets.QPushButton(parent=Form)
        self.btn_salir.setGeometry(QtCore.QRect(640, 480, 75, 31))
        self.btn_salir.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/flecha_atras.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_salir.setIcon(icon5)
        self.btn_salir.setIconSize(QtCore.QSize(50, 50))
        self.btn_salir.setFlat(True)
        self.btn_salir.setObjectName("btn_salir")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "ROARI HOTEL"))
        self.pushButton.setText(_translate("Form", "     Reservar\n"
"     Habitación"))
        self.pushButton_2.setText(_translate("Form", "  Habitaciones \n"
"  Disponibles"))
        self.pushButton_3.setText(_translate("Form", "  Clientes \n"
"  Registrados"))
        self.pushButton_4.setText(_translate("Form", "   Historial \n"
"   de Reservas"))
        self.pushButton_5.setText(_translate("Form", " Servicio\n"
" a la Habitación"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Ventana_Principal()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
