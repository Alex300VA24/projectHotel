import logging
from .db import DBConnection
from .cliente import Cliente
# import bcrypt


class Reserva:
    def __init__(
        self, idReserva, idCliente, idHabitacion, fechaInicio, fechaFin, estado, costo
    ):
        self.idReserva = idReserva
        self.idCliente = idCliente
        self.idHabitacion = idHabitacion
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.estado = estado
        self.costo = costo
    
    INSERT_SQL = """INSERT INTO reserva 
                    (idCliente, idHabitacion, fechaInicio, fechaFin, estado, total) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""

    UPDATE_SQL = """UPDATE reserva 
                    SET idCliente = %s, idHabitacion = %s, fechaInicio = %s, fechaFin = %s, estado = %s 
                    WHERE idReserva = %s"""

    def save(self):
        try:
            with Cliente.connection.cursor() as cursor:
                cursor.execute(
                    self.INSERT_SQL,
                    (self.idCliente, self.idHabitacion, self.fechaInicio, self.fechaFin, self.estado, self.costo),
                )
                self.idReserva = cursor.lastrowid
            Cliente.connection.commit()
        except Exception as e:
            Cliente.connection.rollback()
            logging.error(f"Error al guardar la reserva: {e}")
            raise

    def update(self):
        conn = DBConnection().connect()
        if not conn:
            raise ConnectionError("No se puede establecer conexión con la base de datos")

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    self.UPDATE_SQL,
                    (self.idCliente, self.idHabitacion, self.fechaInicio, self.fechaFin, self.estado, self.idReserva),
                )
            conn.commit()
        except Exception as e:
            conn.rollback()
            logging.error(f"Error al actualizar la reserva: {e}")
            raise
        finally:
            conn.close()




