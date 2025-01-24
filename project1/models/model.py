from db import DBConnection 
from hashlib import sha256

class Administrador:
    def __init__(self, id_administrador=None, nombres=None, apellido_paterno=None, apellido_materno=None, correo=None, contrasenia=None):
        self.id_administrador = id_administrador
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo = correo
        self.contrasenia = contrasenia

    @classmethod
    def crear_administrador(cls):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM administrador LIMIT 1")
            administrador = cursor.fetchone()
            
            if not administrador:  # Si no hay administrador, lo crea
                correo = 'admin@ejemplo.com'
                contrasenia = '12345'
                contrasenia_hash = sha256(contrasenia.encode()).hexdigest()

                query = """
                    INSERT INTO administrador (correo, contrasenia)
                    VALUES (%s, %s)
                """
                cursor.execute(query, (correo, contrasenia_hash))
                conexion.commit()
                print("Administrador creado con éxito.")
            else:
                print("Ya existe un administrador registrado.")
            cursor.close()
            conexion.close()

    def verificar_contrasenia(self, password: str) -> bool:
        """Verifica si la contraseña proporcionada coincide con la almacenada"""
        contrasenia_hash = sha256(password.encode()).hexdigest()
        return self.contrasenia == contrasenia_hash


class Cliente:
    def __init__(self, id_cliente=None, nombres=None, apellido_paterno=None, apellido_materno=None, telefono=None):
        self.id_cliente = id_cliente
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono

    @classmethod
    def crear_cliente(cls, nombres, apellido_paterno, apellido_materno, telefono):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
                INSERT INTO cliente (nombres, apellidoPaterno, apellidoMaterno, telefono)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombres, apellido_paterno, apellido_materno, telefono))
            conexion.commit()
            cursor.close()
            conexion.close()


class TipoHabitacion:
    def __init__(self, id_tipo_habitacion=None, tipo=None, precio_noche=None):
        self.id_tipo_habitacion = id_tipo_habitacion
        self.tipo = tipo
        self.precio_noche = precio_noche

    @classmethod
    def crear_tipo_habitacion(cls, tipo, precio_noche):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
                INSERT INTO tipo_habitacion (tipo, precioNoche)
                VALUES (%s, %s)
            """
            cursor.execute(query, (tipo, precio_noche))
            conexion.commit()
            cursor.close()
            conexion.close()


class Habitacion:
    def __init__(self, id_habitacion=None, numero_habitacion=None, id_tipo_habitacion=None, estado=None):
        self.id_habitacion = id_habitacion
        self.numero_habitacion = numero_habitacion
        self.id_tipo_habitacion = id_tipo_habitacion
        self.estado = estado

    @classmethod
    def crear_habitacion(cls, numero_habitacion, id_tipo_habitacion, estado):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
                INSERT INTO habitacion (numeroHabitacion, idTipo_Habitacion, estado)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (numero_habitacion, id_tipo_habitacion, estado))
            conexion.commit()
            cursor.close()
            conexion.close()


class Reserva:
    def __init__(self, id_reserva=None, id_cliente=None, id_habitacion=None, fecha_inicio=None, fecha_fin=None, estado=None):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_habitacion = id_habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    @classmethod
    def crear_reserva(cls, id_cliente, id_habitacion, fecha_inicio, fecha_fin, estado):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
                INSERT INTO reserva (idCliente, idHabitacion, fechaInicio, fechaFin, estado)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (id_cliente, id_habitacion, fecha_inicio, fecha_fin, estado))
            conexion.commit()
            cursor.close()
            conexion.close()


class Servicio:
    def __init__(self, id_servicio=None, concepto=None, descripcion=None, costo_servicio=None, fecha_consumo=None):
        self.id_servicio = id_servicio
        self.concepto = concepto
        self.descripcion = descripcion
        self.costo_servicio = costo_servicio
        self.fecha_consumo = fecha_consumo

    @classmethod
    def crear_servicio(cls, concepto, descripcion, costo_servicio, fecha_consumo):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
                INSERT INTO servicio (concepto, descripcion, costoServicio, fechaConsumo)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (concepto, descripcion, costo_servicio, fecha_consumo))
            conexion.commit()
            cursor.close()
            conexion.close()


class ConsumoServicio:
    def __init__(self, id_consumo_servicio=None, id_reserva=None, id_servicio=None, costo_consumo_servicio=None):
        self.id_consumo_servicio = id_consumo_servicio
        self.id_reserva = id_reserva
        self.id_servicio = id_servicio
        self.costo_consumo_servicio = costo_consumo_servicio

    @classmethod
    def crear_consumo_servicio(cls, id_reserva, id_servicio, costo_consumo_servicio):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
                INSERT INTO consumo_servicio (idReserva, idServicio, costoConsumoServicio)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (id_reserva, id_servicio, costo_consumo_servicio))
            conexion.commit()
            cursor.close()
            conexion.close()
