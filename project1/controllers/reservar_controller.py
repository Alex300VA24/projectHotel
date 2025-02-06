from PyQt6.QtWidgets import QWidget, QMessageBox  # type:ignore
from PyQt6.QtCore import QCoreApplication  # type:ignore

# from project1.models import tipo_habitacion
from views.reservar.Ui_Form_Reservar_Habitacion import Ui_Form_Reservar_Habitacion
from models.cliente import Cliente
from models.reserva import Reserva
from models.habitacion import Habitacion
from models.tipo_habitacion import TipoHabitacion


class ReservarController:
    def __init__(self):
        self.ventana_reservar = QWidget()
        self.ui = Ui_Form_Reservar_Habitacion()
        self.ui.setupUi(self.ventana_reservar)
        self.ventana_principal_controller = None

        # Inicializar los precios de las habitaciones
        self.precio_habitacion = {}

        # Llenar el combo box con los tipos de habitaciones
        self.cargar_tipo_habitaciones()

        # Conectar el evento del combo box de tipo de habitación
        self.ui.box_tipo_habitacion.currentIndexChanged.connect(
            self.actualizar_numeros_habitacion
        )

        # Conectar eventos
        self.ui.box_tipo_habitacion.currentIndexChanged.connect(
            self.calcular_precio_total
        )
        self.ui.txt_noches.textChanged.connect(self.calcular_precio_total)

        self.ui.btn_cancelar.clicked.connect(self.regresar_ventana_prinicipal)
        self.ui.btn_guardar.clicked.connect(self.guardar_reserva)

    def cargar_tipo_habitaciones(self):
        """Llena el combo box con los tipos de habitaciones."""
        try:
            tipos = TipoHabitacion.obtener_todos()  # Obtener los registros del modelo
            lista_tipos = [
                tipo_habitacion.tipo for tipo_habitacion in tipos
            ]  # Crear lista de nombres
            self.ui.box_tipo_habitacion.addItems(lista_tipos)  # Llenar el combo box
            # Forzar que no haya selección inicial
            self.ui.box_tipo_habitacion.setCurrentIndex(-1)
        except Exception as e:
            print(f"Error al cargar los tipos de habitaciones: {e}")

    def actualizar_numeros_habitacion(self):
        """Actualiza el combo box de número de habitación según el tipo seleccionado."""
        try:
            # Obtener el ID del tipo seleccionado
            index_tipo = self.ui.box_tipo_habitacion.currentIndex()
            print(index_tipo)

            # Obtener los números de habitación disponibles para ese tipo
            numeros_habitacion = Habitacion.obtener_por_tipo(index_tipo + 1)
            print(numeros_habitacion)

            # Limpiar y llenar el combo box de número de habitación
            self.ui.box_numero_habitacion.clear()
            self.ui.box_numero_habitacion.addItems(
                [str(numero) for numero in numeros_habitacion]
            )

        except Exception as e:
            print(f"Error al actualizar los números de habitación: {e}")

    def calcular_precio_total(self):
        # Obtener el índice del tipo de habitación seleccionado
        index_tipo = self.ui.box_tipo_habitacion.currentIndex()
        if index_tipo == -1:  # Si no se ha seleccionado ningún tipo de habitación
            return

        precio_noche = TipoHabitacion.obtener_todos()
        lista_precios = [precio.precio_noche for precio in precio_noche]
        print(precio_noche)

        # cantidad_noches = 0
        # Obtener la cantidad de noches ingresada
        try:
            cantidad_noches = int(self.ui.txt_noches.text())
        except ValueError:
            cantidad_noches = 0  # Si no se ingresa un número válido, asignamos 0

        # Calcular el precio total
        precio_total = lista_precios[index_tipo] * cantidad_noches

        # Actualizar el campo del precio total en la interfaz
        self.ui.lbl_total.setText(f"S/. {precio_total}")

    def regresar_ventana_prinicipal(self):
        self.ventana_reservar.hide()
        if self.ventana_principal_controller:
            self.ventana_principal_controller.mostrar_ventana()

    def mostrar_ventana(self):
        self.ventana_reservar.show()

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self.ventana_reservar, "Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(
            self.ventana_reservar, "Mensaje de reserva realizada", mensaje
        )
        self.ventana_reservar.hide()  # Cerramos la ventana de login
        self.regresar_ventana_prinicipal()  # Abrimos la ventana principal

    def guardar_reserva(self):
        try:
            # Obtener los datos de la interfaz
            nombre = self.ui.txt_nombre_cliente.text().strip()
            celular = self.ui.txt_celular.text().strip()
            fecha_ingreso = self.ui.txt_fecha_ingreso.text().strip()
            cantidad_noches = self.ui.txt_noches.text().strip()
            tipo_habitacion = self.ui.box_tipo_habitacion.currentText()
            numero_habitacion = self.ui.box_numero_habitacion.currentText()

            print(
                nombre,
                celular,
                fecha_ingreso,
                cantidad_noches,
                tipo_habitacion,
                numero_habitacion,
            )
            self.mostrar_mensaje("Reserva guardada correctamente")
        except Exception as e:
            self.mostrar_error(f"Ocurrió un error: {e}")
