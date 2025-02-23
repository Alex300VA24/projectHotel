from .db import DBConnection
from .cliente import Cliente


class Habitacion:
    def __init__(
        self,
        id_habitacion=None,
        numero_habitacion=None,
        id_tipo_habitacion=None,
        estado=None,
    ):
        self.id_habitacion = id_habitacion
        self.numero_habitacion = numero_habitacion
        self.id_tipo_habitacion = id_tipo_habitacion
        self.estado = estado

    @classmethod
    def estado_habitacion(cls):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            query = """
                SELECT * FROM habitacion
            """
            resultado = conexion.query(query)
            conexion.disconnect()
            return resultado

    @staticmethod
    def estado_habitacion_numero(numero_habitacion):
        try:
            # Verificar si la conexión está activa
            if not Cliente.connection or not Cliente.connection.is_connected():
                conexion = DBConnection()
                Cliente.connection = conexion.connect()

            # Crear el cursor y ejecutar la consulta
            cursor = Cliente.connection.cursor()
            try:
                query = """
                    SELECT estado 
                    FROM habitacion 
                    WHERE numeroHabitacion = %s
                """
                cursor.execute(query, (numero_habitacion,))
                habitacion = cursor.fetchone()

                # Si se encuentra la habitación, devolver el estado
                if habitacion:
                    return habitacion[0]  # 'estado' está en la primera columna
                else:
                    return None  # La habitación no existe
            finally:
                cursor.close()  # Asegurar que el cursor se cierre
        except Exception as e:
            raise Exception(f"Error al consultar el estado de la habitación: {e}")

    @classmethod
    def obtener_por_tipo(cls, id_tipo_habitacion):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            query = """
                SELECT numeroHabitacion FROM habitacion WHERE idTipo_habitacion = %s
            """
            resultado = conexion.query(query, (id_tipo_habitacion,))
            conexion.disconnect()
            return [fila[0] for fila in resultado]

    @staticmethod
    def consultar_idHabitacion(numero_habitacion):
        cursor = Cliente.connection.cursor()
        query = "SELECT idHabitacion FROM Habitacion WHERE numeroHabitacion = %s"
        cursor.execute(query, (numero_habitacion,))
        habitacion = cursor.fetchone()
        cursor.close()
        if habitacion:
            return habitacion[0]
        else:
            raise Exception("Habitación no encontrada.")

    @staticmethod
    def actualizar_estado(numero_habitacion):
        try:
            with Cliente.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE habitacion SET estado = %s WHERE numeroHabitacion = %s",
                    ("pendiente", numero_habitacion),
                )
            # Cliente.connection.commit()  # Confirma los cambios
        except Exception as e:
            Cliente.connection.rollback()  # Revierte los cambios en caso de error
            raise ValueError(f'El programa lanzó este error: {e}')# Relanza la excepción sin modificarla
