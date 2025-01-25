from PyQt6.QtWidgets import QMessageBox #type:ignore

from views.FormServicio import FormServicio


class VentanaPrincipalController:
    def __init__(self, ventana_principal_view, login_view):
        self.ui = ventana_principal_view  # Guardamos la instancia de la vista (login)
        self.ventana_login = login_view
        self.ui.setupUi(self.ui)
        self.ui.btn_salir.clicked.connect(self.regresar_login)  # Conectamos el botón de salir
        self.ui.btn_servicio.clicked.connect(self.abrir_ventana_servicio) # Conectamos el botón de servicio

    

    def abrir_ventana_servicio(self):
        print("abrir ventana servicio")
        self.ui.close()
        print('antes de abrir')
        self.abrir_servicio()
        print('luego de abrir')

    def abrir_servicio(self):
        print('instanciando abrir servicio')
        ventana_servicio = FormServicio()
        print('asignando')
        self.ventana_servicio_view = ventana_servicio
        #self.ventana_servicio_view.setupUi(self.ventana_servicio_view)
        #cerramos ventana principal
        #self.ui_ventana_principal.btn_salir.clicked.connect(self.regresar_login)
        print('mostrando')
        self.ventana_servicio_view.show()
    
    def regresar_login(self):
        print('regresar login')
        self.ui.close()
        print('show login')
        self.ventana_login.show()
    


