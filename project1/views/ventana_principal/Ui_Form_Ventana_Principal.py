# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget #type:ignore



class Ui_Form_Ventana_Principal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        font = QtGui.QFont()
<<<<<<< HEAD:project1/views/ventana_principal/Ui_Form_Ventana_Principal.py
        font.setFamily("Inter Medium")
        font.setPointSize(30)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_reservar = QtWidgets.QPushButton(parent=Form)
        self.btn_reservar.setGeometry(QtCore.QRect(550, 180, 161, 61))
=======
        font.setFamily("Tahoma")
        Form.setFont(font)
        Form.setStyleSheet("Qwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.965909, y1:0.04, x2:0, y2:1, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(610, 230, 161, 61))
>>>>>>> 49adb85 (tablasPorArreglar):project1/views/ventana_principal.py
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
<<<<<<< HEAD:project1/views/ventana_principal/Ui_Form_Ventana_Principal.py
        self.btn_reservar.setFont(font)
        self.btn_reservar.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/reservacion.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_reservar.setIcon(icon)
        self.btn_reservar.setIconSize(QtCore.QSize(50, 50))
        self.btn_reservar.setObjectName("btn_reservar")
        self.btn_habitaciones = QtWidgets.QPushButton(parent=Form)
        self.btn_habitaciones.setGeometry(QtCore.QRect(450, 360, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_habitaciones.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/habitacion.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_habitaciones.setIcon(icon1)
        self.btn_habitaciones.setIconSize(QtCore.QSize(50, 50))
        self.btn_habitaciones.setObjectName("btn_habitaciones")
        self.btn_clientes = QtWidgets.QPushButton(parent=Form)
        self.btn_clientes.setGeometry(QtCore.QRect(550, 270, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_clientes.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/cliente.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_clientes.setIcon(icon2)
        self.btn_clientes.setIconSize(QtCore.QSize(50, 50))
        self.btn_clientes.setObjectName("btn_clientes")
        self.btn_historial = QtWidgets.QPushButton(parent=Form)
        self.btn_historial.setGeometry(QtCore.QRect(380, 270, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_historial.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/historial.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_historial.setIcon(icon3)
        self.btn_historial.setIconSize(QtCore.QSize(50, 50))
        self.btn_historial.setObjectName("btn_historial")
        self.btn_servicio = QtWidgets.QPushButton(parent=Form)
        self.btn_servicio.setGeometry(QtCore.QRect(380, 180, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.btn_servicio.setFont(font)
        self.btn_servicio.setStyleSheet("")
=======
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* Fondo del botón */\n"
"    color: #333333;           /* Texto del botón */\n"
"    border: 2px solid #333333; /* Borde gris oscuro */\n"
"    border-radius: 8px;       /* Bordes redondeados */\n"
"    padding: 5px;             /* Espaciado interno */\n"
"    font-size: 14px;          /* Tamaño del texto */\n"
"    font-weight: bold;        /* Texto en negrita */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F9F9F9; /* Fondo cuando el mouse pasa por encima */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D9D9D9; /* Fondo cuando se presiona */\n"
"    color: #000000;           /* Cambia el texto a negro */\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/reservacion.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 410, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* Fondo del botón */\n"
"    color: #333333;           /* Texto del botón */\n"
"    border: 2px solid #333333; /* Borde gris oscuro */\n"
"    border-radius: 8px;       /* Bordes redondeados */\n"
"    padding: 5px;             /* Espaciado interno */\n"
"    font-size: 14px;          /* Tamaño del texto */\n"
"    font-weight: bold;        /* Texto en negrita */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F9F9F9; /* Fondo cuando el mouse pasa por encima */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D9D9D9; /* Fondo cuando se presiona */\n"
"    color: #000000;           /* Cambia el texto a negro */\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/habitacion.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 320, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* Fondo del botón */\n"
"    color: #333333;           /* Texto del botón */\n"
"    border: 2px solid #333333; /* Borde gris oscuro */\n"
"    border-radius: 8px;       /* Bordes redondeados */\n"
"    padding: 5px;             /* Espaciado interno */\n"
"    font-size: 14px;          /* Tamaño del texto */\n"
"    font-weight: bold;        /* Texto en negrita */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F9F9F9; /* Fondo cuando el mouse pasa por encima */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D9D9D9; /* Fondo cuando se presiona */\n"
"    color: #000000;           /* Cambia el texto a negro */\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/cliente.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 320, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* Fondo del botón */\n"
"    color: #333333;           /* Texto del botón */\n"
"    border: 2px solid #333333; /* Borde gris oscuro */\n"
"    border-radius: 8px;       /* Bordes redondeados */\n"
"    padding: 5px;             /* Espaciado interno */\n"
"    font-size: 14px;          /* Tamaño del texto */\n"
"    font-weight: bold;        /* Texto en negrita */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F9F9F9; /* Fondo cuando el mouse pasa por encima */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D9D9D9; /* Fondo cuando se presiona */\n"
"    color: #000000;           /* Cambia el texto a negro */\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/historial.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 230, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* Fondo del botón */\n"
"    color: #333333;           /* Texto del botón */\n"
"    border: 2px solid #333333; /* Borde gris oscuro */\n"
"    border-radius: 8px;       /* Bordes redondeados */\n"
"    padding: 5px;             /* Espaciado interno */\n"
"    font-size: 14px;          /* Tamaño del texto */\n"
"    font-weight: bold;        /* Texto en negrita */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F9F9F9; /* Fondo cuando el mouse pasa por encima */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D9D9D9; /* Fondo cuando se presiona */\n"
"    color: #000000;           /* Cambia el texto a negro */\n"
"}\n"
"")
>>>>>>> 49adb85 (tablasPorArreglar):project1/views/ventana_principal.py
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/servicio.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_servicio.setIcon(icon4)
        self.btn_servicio.setIconSize(QtCore.QSize(50, 50))
        self.btn_servicio.setObjectName("btn_servicio")
        self.btn_salir = QtWidgets.QPushButton(parent=Form)
        self.btn_salir.setGeometry(QtCore.QRect(710, 510, 75, 61))
        self.btn_salir.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("views/ui\\../../resources/images/icons/flecha_atras.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_salir.setIcon(icon5)
        self.btn_salir.setIconSize(QtCore.QSize(50, 50))
        self.btn_salir.setFlat(True)
        self.btn_salir.setObjectName("btn_salir")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("views/ui\\../../resources/images/hotel_imagen.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(550, 70, 91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("views/ui\\../../resources/images/logo.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
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
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.btn_salir.raise_()
        self.label.raise_()
        self.label_6.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
<<<<<<< HEAD:project1/views/ventana_principal/Ui_Form_Ventana_Principal.py
        self.label_2.setText(_translate("Form", "ROARI HOTEL"))
        self.btn_reservar.setText(_translate("Form", "     Reservar\n"
=======
        self.pushButton.setText(_translate("Form", "     Reservar\n"
>>>>>>> 49adb85 (tablasPorArreglar):project1/views/ventana_principal.py
"     Habitación"))
        self.btn_habitaciones.setText(_translate("Form", "  Habitaciones \n"
"  Disponibles"))
        self.btn_clientes.setText(_translate("Form", "  Clientes \n"
"  Registrados"))
<<<<<<< HEAD:project1/views/ventana_principal/Ui_Form_Ventana_Principal.py
        self.btn_historial.setText(_translate("Form", "   Historial \n"
"   de Reservas"))
        self.btn_servicio.setText(_translate("Form", " Servicio\n"
" a la Habitación"))
=======
        self.pushButton_4.setText(_translate("Form", "   Historial de\n"
"   Reservas"))
        self.pushButton_5.setText(_translate("Form", " Servicio a la\n"
" Habitación"))
        self.label_3.setText(_translate("Form", "BIENVENIDO(A)"))

>>>>>>> 49adb85 (tablasPorArreglar):project1/views/ventana_principal.py



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Ventana_Principal()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
