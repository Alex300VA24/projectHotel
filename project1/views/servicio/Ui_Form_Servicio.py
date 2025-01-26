from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Servicio(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("QWidget{\n    background-color: rgb(242, 242, 242);\n}")
        self.txt_nombre_cliente = QtWidgets.QLineEdit(parent=Form)
        self.txt_nombre_cliente.setGeometry(QtCore.QRect(60, 190, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.txt_nombre_cliente.setFont(font)
        self.txt_nombre_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_nombre_cliente.setFrame(False)
        self.txt_nombre_cliente.setObjectName("txt_nombre_cliente")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(60, 250, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_concepto = QtWidgets.QLineEdit(parent=Form)
        self.txt_concepto.setGeometry(QtCore.QRect(60, 270, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.txt_concepto.setFont(font)
        self.txt_concepto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_concepto.setFrame(False)
        self.txt_concepto.setObjectName("txt_concepto")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(450, 170, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(450, 250, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txt_costo = QtWidgets.QLineEdit(parent=Form)
        self.txt_costo.setGeometry(QtCore.QRect(450, 270, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.txt_costo.setFont(font)
        self.txt_costo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_costo.setFrame(False)
        self.txt_costo.setObjectName("txt_costo")
        self.btn_guardar = QtWidgets.QPushButton(parent=Form)
        self.btn_guardar.setGeometry(QtCore.QRect(480, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_guardar.setFont(font)
        self.btn_guardar.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #EC4424; /* Rojo */\n"
            "    color: #FFFFFF; /* Texto blanco */\n"
            "    border-radius: 8px; /* Bordes redondeados opcionales */\n"
            "    font-weight: bold; /* Negrita opcional */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #FF5733; /* Rojo más claro en hover */\n"
            "}"
        )
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_cancelar = QtWidgets.QPushButton(parent=Form)
        self.btn_cancelar.setGeometry(QtCore.QRect(610, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #A9A9A9; /* Gris medio */\n"
            "    color: #FFFFFF; /* Texto blanco */\n"
            "    border-radius: 8px; /* Bordes redondeados opcionales */\n"
            "    font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #808080; /* Gris oscuro en hover */\n"
            "}"
        )
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.txt_descripcion = QtWidgets.QLineEdit(parent=Form)
        self.txt_descripcion.setGeometry(QtCore.QRect(450, 190, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.txt_descripcion.setFont(font)
        self.txt_descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_descripcion.setFrame(False)
        self.txt_descripcion.setObjectName("txt_descripcion")
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setGeometry(QtCore.QRect(60, 210, 291, 16))
        self.frame_2.setStyleSheet("background: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(parent=Form)
        self.frame_3.setGeometry(QtCore.QRect(60, 290, 291, 16))
        self.frame_3.setStyleSheet("background: transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(parent=Form)
        self.frame_4.setGeometry(QtCore.QRect(450, 210, 291, 16))
        self.frame_4.setStyleSheet("background: transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(parent=Form)
        self.frame_5.setGeometry(QtCore.QRect(450, 290, 291, 16))
        self.frame_5.setStyleSheet("background: transparent;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_5.setLineWidth(1)
        self.frame_5.setObjectName("frame_5")
        self.label_12 = QtWidgets.QLabel(parent=Form)
        self.label_12.setGeometry(QtCore.QRect(350, 20, 91, 91))
        self.label_12.setText("")
        self.label_12.setPixmap(
            QtGui.QPixmap("views/ui\\../../resources/images/logo.jpg")
        )
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 801, 141))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(20)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(False)
        self.label_11.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.514, y1:0.0343182, x2:0.500554, y2:0.727, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.label_11.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.txt_nombre_cliente.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.txt_concepto.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.txt_costo.raise_()
        self.btn_guardar.raise_()
        self.btn_cancelar.raise_()
        self.txt_descripcion.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.label_12.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Nombre de Cliente"))
        self.label_4.setText(_translate("Form", "Concepto"))
        self.label_7.setText(_translate("Form", "Descripción"))
        self.label_8.setText(_translate("Form", "Costo"))
        self.btn_guardar.setText(_translate("Form", "Guardar"))
        self.btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label_11.setText(_translate("Form", "Reservar Habitación"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Servicio()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
