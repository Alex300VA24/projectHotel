import sys
from PyQt6.QtWidgets import QApplication  # type: ignore
from views.login.FormLogin import FormLogin  # Importa solo la vista
from controllers.login_controller import LoginController  # Importa el controlador
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    app = QApplication(sys.argv)
    
    # Crear instancia de la vista
    login_view = FormLogin()
    
    # Pasar la vista al controlador
    login_controller = LoginController(login_view)
    
    # Mostrar la vista (el controlador manejará los eventos)
    login_view.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
