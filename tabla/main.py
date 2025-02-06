import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QWidget, QMessageBox, QLabel
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabla dinámica con consulta")
        self.setGeometry(100, 100, 600, 400)

        # Crear el widget principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Crear la tabla
        self.table = QTableWidget(5, 3)  # 5 filas, 3 columnas
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Edad"])
        self.fill_table()
        layout.addWidget(self.table)

        # Crear el botón externo
        self.btn_consultar = QPushButton("Consultar Registro Seleccionado")
        self.btn_consultar.clicked.connect(self.consultar_registro)
        layout.addWidget(self.btn_consultar)

        # Almacenar referencia a la ventana dinámica
        self.dynamic_window = None

    def fill_table(self):
        """Llena la tabla con datos de ejemplo."""
        data = [
            (1, "Juan", 25),
            (2, "María", 30),
            (3, "Pedro", 35),
            (4, "Ana", 28),
            (5, "Luis", 32),
        ]
        for row, (id_, name, age) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(str(id_)))
            self.table.setItem(row, 1, QTableWidgetItem(name))
            self.table.setItem(row, 2, QTableWidgetItem(str(age)))

    def consultar_registro(self):
        """Consulta el registro seleccionado y muestra una nueva ventana."""
        selected_items = self.table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un registro.")
            return

        # Obtener datos de la fila seleccionada
        selected_row = self.table.currentRow()
        id_ = self.table.item(selected_row, 0).text()
        name = self.table.item(selected_row, 1).text()
        age = self.table.item(selected_row, 2).text()

        # Abrir una ventana dinámica con la información seleccionada
        self.open_dynamic_window(id_, name, age)

    def open_dynamic_window(self, id_, name, age):
        """Abre una nueva ventana dinámica con la información seleccionada."""
        if self.dynamic_window is not None:
            self.dynamic_window.close()  # Cierra cualquier ventana previa

        self.dynamic_window = QWidget()
        self.dynamic_window.setWindowTitle("Información del Registro")
        self.dynamic_window.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout(self.dynamic_window)
        layout.addWidget(QLabel(f"ID: {id_}"))
        layout.addWidget(QLabel(f"Nombre: {name}"))
        layout.addWidget(QLabel(f"Edad: {age}"))

        self.dynamic_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
