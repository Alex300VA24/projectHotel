from .db import DBConnection


class TipoHabitacion:
    def __init__(self, id_tipo_habitacion=None, tipo=None, precio_noche=None):
        self.id_tipo_habitacion = id_tipo_habitacion
        self.tipo = tipo
        self.precio_noche = precio_noche

    @staticmethod
    def obtener_todos():
        try:
            db = DBConnection()
            db.connect()

            query = "SELECT tipo, precioNoche FROM tipo_habitacion"
            result = db.query(query)

            habitaciones = []
            for row in result:
                tipo, precio_noche = row
                habitaciones.append(TipoHabitacion(None, tipo, precio_noche))

            db.disconnect()
            return habitaciones
        except Exception as e:
            raise Exception(f"Error consultando tipo de habitación: {e}")
