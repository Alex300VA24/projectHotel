from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from HistorialController import HistorialController
from historial import Historial

class HistorialView(QMainWindow):
    def __init__(self, historial_controller):
        super().__init__()
        self.setWindowTitle("Historial de Reservas")
        self.setGeometry(100, 100, 800, 600)

        self.historial_controller = historial_controller

        # Crear tabla
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID Cliente", "Nombre Completo", "Fecha Reserva", "Fecha Salida",
            "N° Habitación", "Tipo Habitación", "Estado", "Monto"
        ])

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Cargar datos al iniciar
        self.cargar_datos()

    def cargar_datos(self):
        # Obtener datos del controlador
        datos = self.historial_controller.obtener_datos_historial()

        # Configurar filas de la tabla
        self.table.setRowCount(len(datos))

        for row, registro in enumerate(datos):
            self.table.setItem(row, 0, QTableWidgetItem(str(registro['idCliente'])))
            self.table.setItem(row, 1, QTableWidgetItem(registro['nombre_completo']))
            self.table.setItem(row, 2, QTableWidgetItem(str(registro['fecha_reserva'])))
            self.table.setItem(row, 3, QTableWidgetItem(str(registro['fecha_salida'])))
            self.table.setItem(row, 4, QTableWidgetItem(registro['numero_habitacion']))
            self.table.setItem(row, 5, QTableWidgetItem(registro['tipo_habitacion']))
            self.table.setItem(row, 6, QTableWidgetItem(registro['estado_habitacion']))
            self.table.setItem(row, 7, QTableWidgetItem(str(registro['monto'])))

if __name__ == "__main__":
    # Configuración de la base de datos
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'Hotel'
    }

    # Crear instancias del modelo, controlador y vista
    historial_model = Historial(db_config)
    historial_controller = HistorialController(historial_model)

    app = QApplication([])
    view = HistorialView(historial_controller)
    view.show()
    app.exec()