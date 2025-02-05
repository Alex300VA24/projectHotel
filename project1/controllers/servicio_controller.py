from PyQt6.QtWidgets import (  # type: ignore
    QWidget,
    QListWidgetItem,
    QHBoxLayout,
    QVBoxLayout,
    QSpinBox,
    QLabel,
    QCheckBox,
    QMessageBox,
)  # type:ignore
from models.servicio import Servicio
from views.servicio.Ui_Form_Servicio import Ui_Form_Servicio
from datetime import date


class ServicioController:
    def __init__(self):
        self.ventana_servicio = QWidget()
        self.ui = Ui_Form_Servicio()
        self.ui.setupUi(self.ventana_servicio)
        self.ventana_principal_controller = None

        self.ui.btn_cancelar.clicked.connect(self.regresar_ventana_prinicipal)
        self.ui.box_concepto.currentIndexChanged.connect(
            self.actualizar_lista_servicios
        )
        self.ui.btn_guardar.clicked.connect(self.solicitar_servicio)

        # Cargar servicios en el comboBox al iniciar la ventana
        self.cargar_servicios_en_combo()

    def cargar_servicios_en_combo(self):
        """Carga los nombres de los servicios en el ComboBox desde la base de datos."""
        servicios = Servicio.obtener_todos_los_servicios()
        self.ui.box_concepto.addItems(servicios)

    def actualizar_lista_servicios(self):
        # Verificar si el groupBox ya tiene un layout
        layout = self.ui.groupBox_lista.layout()

        # Si no tiene layout, asignamos uno
        if layout is None:
            layout = QVBoxLayout()
            self.ui.groupBox_lista.setLayout(layout)
        else:
            # Limpiar los widgets anteriores
            for i in reversed(range(layout.count())):
                widget_to_remove = layout.itemAt(i).widget()
                if widget_to_remove is not None:
                    widget_to_remove.deleteLater()

        # Obtener el servicio seleccionado del ComboBox
        servicio_seleccionado = self.ui.box_concepto.currentText()

        # Lista de detalles según el servicio seleccionado
        detalles_servicio = Servicio.obtener_detalles(servicio_seleccionado)
        precios_servicios = Servicio.obtener_precios(servicio_seleccionado)
        print(precios_servicios)

        # Función para actualizar el QTextEdit y QLabel
        def actualizar_descripcion():
            total = 0
            descripcion_texto = ""

            for i in range(layout.count()):
                contenedor = layout.itemAt(i).widget()
                if contenedor:
                    checkbox = contenedor.findChild(QCheckBox)
                    spinbox = contenedor.findChild(QSpinBox)

                    if checkbox and spinbox and checkbox.isChecked():
                        nombre_servicio = checkbox.text()
                        cantidad = spinbox.value()
                        precio_unitario = precios_servicios.get(nombre_servicio, 0)
                        subtotal = cantidad * precio_unitario
                        total += subtotal

                        descripcion_texto += (
                            f"{nombre_servicio} x{cantidad} - ${subtotal:.2f}\n"
                        )

            self.ui.txt_descripcion.setPlainText(descripcion_texto)
            self.ui.lbl_total.setText(f"S/. {total:.2f}")

        for detalle in detalles_servicio:
            # Contenedor QWidget para cada ítem (CheckBox + SpinBox)
            contenedor_widget = QWidget()
            contenedor_layout = QHBoxLayout(contenedor_widget)

            # CheckBox con el nombre del detalle
            checkbox = QCheckBox(detalle)

            # SpinBox para seleccionar la cantidad (de 1 a 10 por ejemplo)
            spinbox = QSpinBox()
            spinbox.setMinimum(1)
            spinbox.setMaximum(10)
            spinbox.setValue(1)  # Valor predeterminado

            # Conectar señales de cambio a la función de actualización
            checkbox.stateChanged.connect(actualizar_descripcion)
            spinbox.valueChanged.connect(actualizar_descripcion)

            # Añadir los widgets al layout del contenedor
            contenedor_layout.addWidget(checkbox)
            contenedor_layout.addWidget(QLabel(":"))
            contenedor_layout.addWidget(spinbox)

            # Añadir el contenedor al layout principal del groupBox
            layout.addWidget(contenedor_widget)

    def mostrar_detalles_servicio(self):
        """Muestra los detalles del servicio seleccionado en el QListWidget."""
        servicio_seleccionado = self.ui.box_concepto.currentText()

        # Obtener detalles del servicio seleccionado
        detalles = Servicio.obtener_detalles(servicio_seleccionado)

        # Limpiar lista antes de agregar nuevos elementos
        self.ui.listWidget_servicio.clear()

        # Agregar detalles al QListWidget
        for detalle in detalles:
            item = QListWidgetItem(detalle)
            self.ui.listWidget_servicio.addItem(item)

    def solicitar_servicio(self):
        """
        Extrae los datos de la interfaz y solicita el registro del servicio.
        """
        # Obtener los datos de la UI
        nombre_cliente = self.ui.txt_nombre_cliente.text().strip()
        concepto = self.ui.box_concepto.currentText().strip()
        descripcion = self.ui.txt_descripcion.toPlainText().strip()
        costo_total = self.ui.lbl_total.text().strip()

        # Validar que los campos no estén vacíos
        if not nombre_cliente or not concepto or not costo_total:
            QMessageBox.warning(self.ui, "Error", "Todos los campos son obligatorios.")
            return

        # Eliminar el prefijo "S/. " del costo total y convertir a float
        if costo_total.startswith("S/."):
            costo_total = costo_total[
                4:
            ].strip()  # Elimina "S/. " (los primeros 4 caracteres)

        # Intentar convertir el costo a número
        try:
            costo_total = float(costo_total)
        except ValueError:
            QMessageBox.warning(
                self.ui, "Error", "El costo total debe ser un número válido."
            )
            return
        # Crear reserva
        servicio = Servicio(None, concepto, descripcion, costo_total, date.today())
        # Guardar el servicio en la base de datos
        resultado = servicio.save(nombre_cliente)

        # Mostrar mensaje según el resultado
        if resultado.startswith("Error"):
            self.mostrar_error(resultado)
        else:
            self.mostrar_mensaje(resultado)

            # Limpiar los campos después de registrar el servicio
            self.ui.txt_nombre_cliente.clear()
            self.ui.txt_descripcion.clear()
            self.ui.lbl_total.setText("S/. 0.00")
            # Obtener el layout del groupBox_lista
            layout = self.ui.groupBox_lista.layout()

            if layout:
                # Limpiar los widgets anteriores del layout
                for i in reversed(range(layout.count())):
                    widget_to_remove = layout.itemAt(i).widget()
                    if widget_to_remove is not None:
                        widget_to_remove.deleteLater()

    def regresar_ventana_prinicipal(self):
        self.ventana_servicio.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self.ventana_servicio, "Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(
            self.ventana_servicio, "Mensaje de Servicio a la Habitación", mensaje
        )

    def mostrar_ventana(self):
        self.ventana_servicio.show()
    
    # Llama al modelo para conseguir el coste total de los servicios
    def conseguir_total_servicio(id_):
        datos = Servicio.conseguir_total_servicio(id_)
        return datos
    
    def conseguir_total_detalle_servicio(id_):
        datos = Servicio.conseguir_total_detalle_servicio(id_)
        return datos
