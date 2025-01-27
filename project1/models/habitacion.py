from .db import DBConnection


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
