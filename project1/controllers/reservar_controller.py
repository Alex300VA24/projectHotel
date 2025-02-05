from unittest import case
from PyQt6.QtWidgets import QWidget, QMessageBox 
from PyQt6.QtCore import QCoreApplication
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
        
        # Inicializar estructura para precios de habitaciones
        self.precio_habitacion = {}
        
        # Cargar tipos de habitaciones en el combo box
        self.cargar_tipo_habitaciones()
        
        # Conectar eventos para actualización de datos
        self.ui.box_tipo_habitacion.currentIndexChanged.connect(self.actualizar_numeros_habitacion)
        self.ui.box_tipo_habitacion.currentIndexChanged.connect(self.actualizar_precio_total)
        self.ui.txt_noches.textChanged.connect(self.actualizar_precio_total)
        
        # Conectar eventos de botones
        self.ui.btn_cancelar.clicked.connect(self.regresar_ventana_prinicipal)
        self.ui.btn_guardar.clicked.connect(self.registrar_reserva)

    def registrar_reserva(self):
        try:
            # Obtener y validar datos de entrada
            nombre_completo = self.ui.txt_nombre_cliente.text().strip()
            if not nombre_completo or len(nombre_completo.split()) < 3:
                return self.mostrar_error("El nombre completo debe incluir al menos tres palabras.")
            
            nombres, apellido_paterno, apellido_materno = self._extraer_nombres(nombre_completo)
            tipo_documento = self.ui.box_documento.currentText()
            numero_documento = self.ui.txt_numero_documento.text().strip()
            nacionalidad = self.ui.txt_nacionalidad.text().strip()
            celular = self.ui.txt_celular.text().strip()
            numero_habitacion = self.ui.box_numero_habitacion.currentText()
            fecha_ingreso_str = self.ui.txt_fecha_ingreso.text().strip()
            
            # Validar cantidad de noches
            try:
                noches = int(self.ui.txt_noches.text().strip())
            except ValueError:
                return self.mostrar_error("La cantidad de noches debe ser un número válido.")
            
            # Validar costo total
            costo_total = self._obtener_costo_total()
            if costo_total is None:
                return
            
            # Verificar estado de la habitación
            estado_habitacion = Habitacion.estado_habitacion_numero(numero_habitacion)
            if estado_habitacion in ["pendiente", "ocupada", "mantenimiento"]:
                return self.mostrar_error(f"La habitación está en estado {estado_habitacion}")
            
            # Iniciar transacción en la base de datos
            Cliente.iniciar_transaccion()
            
            # Crear y guardar cliente
            cliente = Cliente(None, nombres, apellido_paterno, apellido_materno, tipo_documento, numero_documento, nacionalidad, celular)
            cliente_id = cliente.save()
            
            # Calcular fechas de ingreso y salida
            fecha_ingreso_dt = datetime.strptime(fecha_ingreso_str, "%d/%m/%Y")
            fecha_salida_dt = fecha_ingreso_dt + timedelta(days=noches)
            
            # Crear y guardar reserva
            reserva = Reserva(None, int(cliente_id), Habitacion.consultar_idHabitacion(numero_habitacion), fecha_ingreso_dt.strftime("%Y-%m-%d"), fecha_salida_dt.strftime("%Y-%m-%d"), estado="pendiente", costo=costo_total)
            reserva.save()
            
            # Actualizar estado de la habitación y confirmar transacción
            Habitacion.actualizar_estado(numero_habitacion)
            Cliente.commit_transaccion()
            
            self.mostrar_mensaje("Reserva guardada correctamente.")
            self.ventana_reservar.hide()
            self.regresar_ventana_prinicipal()
        except Exception as e:
            Cliente.rollback_transaccion()
            self.mostrar_error(f"Error al registrar la reserva: {e}")

    def cargar_tipo_habitaciones(self):
        try:
            tipos = TipoHabitacion.obtener_todos()
            self.ui.box_tipo_habitacion.addItems([tipo.tipo for tipo in tipos])
            self.ui.box_tipo_habitacion.setCurrentIndex(-1)
        except Exception as e:
            print(f"Error al cargar los tipos de habitaciones: {e}")

    def actualizar_numeros_habitacion(self):
        try:
            index_tipo = self.ui.box_tipo_habitacion.currentIndex()
            self.ui.box_numero_habitacion.clear()
            self.ui.box_numero_habitacion.addItems([str(numero) for numero in Habitacion.obtener_por_tipo(index_tipo + 1)])
        except Exception as e:
            print(f"Error al actualizar los números de habitación: {e}")

    def actualizar_precio_total(self):
        index_tipo = self.ui.box_tipo_habitacion.currentIndex()
        if index_tipo == -1:
            return
        
        try:
            precio_noche = TipoHabitacion.obtener_todos()[index_tipo].precio_noche
            cantidad_noches = int(self.ui.txt_noches.text())
        except (ValueError, IndexError):
            cantidad_noches = 0
        
        self.ui.lbl_total.setText(f"S/. {precio_noche * cantidad_noches}")

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
    
    def _extraer_nombres(self, nombre_completo):
        partes = nombre_completo.split(" ")
        return " ".join(partes[:-2]), partes[-2], partes[-1]
    
    def _obtener_costo_total(self):
        costo_total = self.ui.lbl_total.text().strip()
        if costo_total.startswith("S/."):
            try:
                return float(costo_total[4:].strip())
            except ValueError:
                self.mostrar_error("El costo total debe ser un número válido.")
        return None
    
    # Llama al modelo para conseguir el coste total de la reserva
    def conseguir_total_reserva(id_):
        datos = Reserva.conseguir_total_reserva(id_)
        return datos