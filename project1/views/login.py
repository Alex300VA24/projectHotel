

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget #type:ignore
from controllers.login_controller import Login_Controller



class Ui_Form_Login(object):
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
        self.label_2.setGeometry(QtCore.QRect(420, 30, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(30)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(460, 140, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(20)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_correo = QtWidgets.QLineEdit(parent=Form)
        self.txt_correo.setGeometry(QtCore.QRect(430, 250, 251, 22))
        self.txt_correo.setObjectName("txt_correo")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(430, 230, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(430, 330, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_contrasena = QtWidgets.QLineEdit(parent=Form)
        self.txt_contrasena.setGeometry(QtCore.QRect(430, 350, 251, 22))
        self.txt_contrasena.setObjectName("txt_contrasena")
        self.btn_salir = QtWidgets.QPushButton(parent=Form)
        self.btn_salir.setGeometry(QtCore.QRect(430, 430, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_salir.setFont(font)
        self.btn_salir.setObjectName("btn_salir")
        self.btn_ingresar = QtWidgets.QPushButton(parent=Form)
        self.btn_ingresar.setGeometry(QtCore.QRect(610, 430, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_ingresar.setFont(font)
        self.btn_ingresar.setObjectName("btn_ingresar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "ROARI HOTEL"))
        self.label_3.setText(_translate("Form", "INICIO SESIÓN"))
        self.label_4.setText(_translate("Form", "Correo Electrónico"))
        self.label_5.setText(_translate("Form", "Contraseña"))
        self.btn_salir.setText(_translate("Form", "Salir"))
        self.btn_ingresar.setText(_translate("Form", "Ingresar"))

class Form_Login(QWidget, Ui_Form_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la UI generada

        self.login_controller = Login_Controller(self)

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
