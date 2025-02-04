from unittest import case
from PyQt6.QtWidgets import QWidget, QMessageBox  # type:ignore
from PyQt6.QtCore import QCoreApplication  # type:ignore
from datetime import datetime, timedelta

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
        self.cliente = None

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
        self.ui.btn_guardar.clicked.connect(self.registrar_reserva)

    def registrar_reserva(self):
        try:
            # Obtener los datos desde la Vista
            nombre_completo = self.ui.txt_nombre_cliente.text().strip()
            nombre_completo_separado = nombre_completo.split(" ")
            nombres = " ".join(nombre_completo_separado[:-2])
            apellido_paterno = nombre_completo_separado[-2]
            apellido_materno = nombre_completo_separado[-1]

            tipo_documento = self.ui.box_documento.currentText()
            numero_documento = self.ui.txt_numero_documento.text().strip()
            nacionalidad = self.ui.txt_nacionalidad.text().strip()
            celular = self.ui.txt_celular.text().strip()
            numero_habitacion = self.ui.box_numero_habitacion.currentText()
            fecha_ingreso_str = self.ui.txt_fecha_ingreso.text().strip()
            noches = int(self.ui.txt_noches.text().strip())
            costo_total = self.ui.lbl_total.text().strip()

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

            # Verificar disponibilidad de la habitacion
            estado_habitacion = Habitacion.estado_habitacion_numero(numero_habitacion)
            if estado_habitacion in ["pendiente", "ocupada", "mantenimiento"]:
                self.mostrar_error(f"La habitacion está en estado {estado_habitacion}")
            else:
                # Iniciar transacción en el modelo
                Cliente.iniciar_transaccion()

                # Crear cliente
                cliente = Cliente(
                    None,
                    nombres,
                    apellido_paterno,
                    apellido_materno,
                    tipo_documento,
                    numero_documento,
                    nacionalidad,
                    celular,
                )

                cliente_id = cliente.save()

                # Calcular fechas de ingreso y salida
                fecha_ingreso_dt = datetime.strptime(fecha_ingreso_str, "%d/%m/%Y")
                fecha_salida_dt = fecha_ingreso_dt + timedelta(days=noches)

                # Crear reserva
                reserva = Reserva(
                    None,
                    int(cliente_id),
                    Habitacion.consultar_idHabitacion(numero_habitacion),
                    fecha_ingreso_str,
                    fecha_salida_dt.strftime("%Y-%m-%d"),
                    estado="pendiente",
                    costo=costo_total,
                )
                # Guardar reserva en la base de datos
                reserva.save()

                Habitacion.actualizar_estado(numero_habitacion)

                # Confirmar transacción
                Cliente.commit_transaccion()
                self.mostrar_mensaje("Reserva guardada correctamente.")
                self.ventana_reservar.hide()
                self.regresar_ventana_prinicipal()

        except Exception as e:
            # Rollback en caso de error
            Cliente.rollback_transaccion()
            self.mostrar_error(f"Error al registrar la reserva: {e}")

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
        QMessageBox.information(self.ventana_reservar, "Mensaje de reserva", mensaje)
