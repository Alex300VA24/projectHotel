# Form implementation generated from reading ui file 'servicio_habitacion.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 532)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 721, 81))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 100, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.txt_nombre_cliente = QtWidgets.QLineEdit(parent=Form)
        self.txt_nombre_cliente.setGeometry(QtCore.QRect(60, 180, 191, 22))
        self.txt_nombre_cliente.setObjectName("txt_nombre_cliente")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(60, 240, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_concepto = QtWidgets.QLineEdit(parent=Form)
        self.txt_concepto.setGeometry(QtCore.QRect(60, 260, 191, 22))
        self.txt_concepto.setObjectName("txt_concepto")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(470, 160, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(470, 240, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txt_costo = QtWidgets.QLineEdit(parent=Form)
        self.txt_costo.setGeometry(QtCore.QRect(470, 260, 191, 22))
        self.txt_costo.setObjectName("txt_costo")
        self.btn_guardar = QtWidgets.QPushButton(parent=Form)
        self.btn_guardar.setGeometry(QtCore.QRect(260, 330, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_guardar.setFont(font)
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_cancelar = QtWidgets.QPushButton(parent=Form)
        self.btn_cancelar.setGeometry(QtCore.QRect(390, 330, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.txt_descripcion = QtWidgets.QLineEdit(parent=Form)
        self.txt_descripcion.setGeometry(QtCore.QRect(470, 180, 191, 22))
        self.txt_descripcion.setObjectName("txt_descripcion")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "ROARI HOTEL"))
        self.label.setText(_translate("Form", "Servicio a la Habitación"))
        self.label_3.setText(_translate("Form", "Nombre de Cliente"))
        self.label_4.setText(_translate("Form", "Concepto"))
        self.label_7.setText(_translate("Form", "Descripción"))
        self.label_8.setText(_translate("Form", "Costo"))
        self.btn_guardar.setText(_translate("Form", "Guardar"))
        self.btn_cancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
