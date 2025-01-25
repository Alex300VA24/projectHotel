# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget #type:ignore


class Ui_Form_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        Form.setFont(font)
        Form.setStyleSheet("Qwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.965909, y1:0.04, x2:0, y2:1, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(550, 70, 91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("views/ui\\../../resources/images/logo.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setGeometry(QtCore.QRect(450, 260, 291, 16))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.btn_salir = QtWidgets.QPushButton(parent=Form)
        self.btn_salir.setEnabled(True)
        self.btn_salir.setGeometry(QtCore.QRect(480, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_salir.setFont(font)
        self.btn_salir.setStyleSheet("QPushButton {\n"
"    background-color: #EC4424; /* Rojo */\n"
"    color: #FFFFFF; /* Texto blanco */\n"
"    border-radius: 8px; /* Bordes redondeados opcionales */\n"
"    font-weight: bold; /* Negrita opcional */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FF5733; /* Rojo más claro en hover */\n"
"}\n"
"")
        self.btn_salir.setObjectName("btn_salir")
        self.txt_contrasena = QtWidgets.QLineEdit(parent=Form)
        self.txt_contrasena.setGeometry(QtCore.QRect(450, 320, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.txt_contrasena.setFont(font)
        self.txt_contrasena.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_contrasena.setFrame(False)
        self.txt_contrasena.setObjectName("txt_contrasena")
        self.frame_3 = QtWidgets.QFrame(parent=Form)
        self.frame_3.setGeometry(QtCore.QRect(450, 340, 291, 16))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.txt_correo = QtWidgets.QLineEdit(parent=Form)
        self.txt_correo.setGeometry(QtCore.QRect(450, 240, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.txt_correo.setFont(font)
        self.txt_correo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(51, 51, 51);")
        self.txt_correo.setFrame(False)
        self.txt_correo.setObjectName("txt_correo")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(450, 220, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(390, 0, 411, 191))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.514, y1:0.0343182, x2:0.500554, y2:0.727, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("views/ui\\../../resources/images/hotel_imagen.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(450, 300, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_ingresar = QtWidgets.QPushButton(parent=Form)
        self.btn_ingresar.setGeometry(QtCore.QRect(610, 410, 101, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 169, 169))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.btn_ingresar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_ingresar.setFont(font)
        self.btn_ingresar.setStyleSheet("QPushButton {\n"
"    background-color: #A9A9A9; /* Gris medio */\n"
"    color: #FFFFFF; /* Texto blanco */\n"
"    border-radius: 8px; /* Bordes redondeados opcionales */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #808080; /* Gris oscuro en hover */\n"
"}")
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.label_3.raise_()
        self.label_6.raise_()
        self.btn_salir.raise_()
        self.txt_contrasena.raise_()
        self.frame_3.raise_()
        self.txt_correo.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.btn_ingresar.raise_()
        self.frame_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_salir.setText(_translate("Form", "Ingresar"))
        self.label_4.setText(_translate("Form", "Correo Electrónico"))
        self.label_3.setText(_translate("Form", "INICIAR SESIÓN"))
        self.label_5.setText(_translate("Form", "Contraseña"))
<<<<<<< HEAD:project1/views/login/Ui_Form_Login.py
        self.btn_salir.setText(_translate("Form", "Salir"))
        self.btn_ingresar.setText(_translate("Form", "Ingresar"))
  


=======
        self.btn_ingresar.setText(_translate("Form", "Salir"))



class Form_Login(QWidget, Ui_Form_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la UI generada

        self.login_controller = Login_Controller(self)

    
>>>>>>> 49adb85 (tablasPorArreglar):project1/views/login.py
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
