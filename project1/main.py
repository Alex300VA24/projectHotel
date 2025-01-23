
import sys
from PyQt6.QtWidgets import QApplication
from views.login import Form_Login
from controllers.login_controller import Login_Controller
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    app = QApplication(sys.argv)
    
    # Cargar la ventana principal y pasar el controlador
    main_window = Form_Login()
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

