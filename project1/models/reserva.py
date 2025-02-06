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

    # Método para conseguir únicamente el total de una reserva según el id del cliente que se ingresa
    @staticmethod
    def conseguir_total_reserva(id):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            query = """
                SELECT total FROM reserva WHERE idCliente = %s
            """
            resultado = conexion.query(query, (id,))
            precio_reserva = resultado[0][0]
            conexion.disconnect()
            return precio_reserva

    def save(self):
        try:
            with Cliente.connection.cursor() as cursor:
                cursor.execute(
                    self.INSERT_SQL,
                    (
                        self.idCliente,
                        self.idHabitacion,
                        self.fechaInicio,
                        self.fechaFin,
                        self.estado,
                        self.costo,
                    ),
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
            raise ConnectionError(
                "No se puede establecer conexión con la base de datos"
            )

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    self.UPDATE_SQL,
                    (
                        self.idCliente,
                        self.idHabitacion,
                        self.fechaInicio,
                        self.fechaFin,
                        self.estado,
                        self.idReserva,
                    ),
                )
            conn.commit()
        except Exception as e:
            conn.rollback()
            logging.error(f"Error al actualizar la reserva: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def obtener_historial_reservas():
        conexion = DBConnection()
        conexion.connect()

        if not conexion:
            raise ConnectionError(
                "No se puede establecer conexión con la base de datos"
            )

        if conexion:
            query = """
                    SELECT 
                        r.idReserva,
                        CONCAT(c.nombres, ' ', c.apellidoPaterno, ' ', c.apellidoMaterno) AS nombre_completo,
                        r.fechaInicio AS fecha_reserva,
                        r.fechaFin AS fecha_salida,
                        r.estado AS estado_reserva,
                        h.numeroHabitacion AS numero_habitacion,
                        th.tipo AS tipo_habitacion,
                        r.total AS monto
                    FROM reserva r
                    JOIN cliente c ON r.idCliente = c.idCliente
                    JOIN habitacion h ON r.idHabitacion = h.idHabitacion
                    JOIN tipo_habitacion th ON h.idTipo_Habitacion = th.idTipoHabitacion;
                    """
            resultado = conexion.query(query)
            conexion.disconnect()
            return resultado

    @staticmethod
    def actualizar_estado_reserva(id_reserva, nuevo_estado):
        conn = DBConnection().connect()
        if not conn:
            raise ConnectionError(
                "No se puede establecer conexión con la base de datos"
            )

        try:
            query = "UPDATE reserva SET estado = %s WHERE idReserva = %s"
            with conn.cursor() as cursor:
                cursor.execute(
                    query,
                    (nuevo_estado, id_reserva),
                )
            conn.commit()
        except Exception as e:
            conn.rollback()
            logging.error(f"Error al actualizar estado de reserva: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def reserva_pagada(nombre_cliente):
        query = """
        SELECT EXISTS (
            SELECT 1 
            FROM reserva r
            JOIN cliente c ON r.idCliente = c.idCliente
            WHERE CONCAT(c.nombres, ' ', c.apellidoPaterno) = %s
            AND r.estado = 'pagada'
        ) AS existe;
        """
        db = DBConnection()  # Instanciamos dentro del método
        try:
            db.connect()
            cursor = db.connection.cursor()
            cursor.execute(query, (nombre_cliente,))
            resultado = cursor.fetchone()[0]  # Devuelve 1 si existe, 0 si no
            cursor.close()
            return bool(resultado)  # Convierte 1 o 0 en True o False
        except Exception as e:
            print(f"Error al verificar reserva: {e}")
            return False
        finally:
            db.disconnect()
