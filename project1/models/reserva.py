from .db import DBConnection
from .cliente import Cliente
# import bcrypt

"""
La clas reserva se va basar de esta tabla:
CREATE TABLE reserva (
  idReserva BIGINT PRIMARY KEY AUTO_INCREMENT,
  idCliente BIGINT NOT NULL,
  idHabitacion BIGINT NOT NULL,
  fechaInicio DATE NOT NULL,
  fechaFin DATE NOT NULL,
  estado ENUM('pagada', 'cancelada', 'pendiente') NOT NULL,
  FOREIGN KEY (idCliente) REFERENCES cliente(idCliente),
  FOREIGN KEY (idHabitacion) REFERENCES habitacion(idHabitacion)
);
"""


class Reserva:
    def __init__(
        self, idReserva, idCliente, idHabitacion, fechaInicio, fechaFin, estado
    ):
        self.idReserva = idReserva
        self.idCliente = idCliente
        self.idHabitacion = idHabitacion
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.estado = estado

    @staticmethod
    def all():
        conn = DBConnection()
        cursor = conn.execute("SELECT * FROM reserva")
        reservas = []
        for row in cursor.fetchall():
            reservas.append(Reserva(row[0], row[1], row[2], row[3], row[4], row[5]))
        return reservas

    @staticmethod
    def find(idReserva):
        conn = DBConnection()
        cursor = conn.execute(
            "SELECT * FROM reserva WHERE idReserva = %s", (idReserva,)
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return Reserva(row[0], row[1], row[2], row[3], row[4], row[5])

    def save(self):
        """conn = DBConnection().connect()
        if not conn:
            raise Exception("No se puede establacer conexion con la base de datos")
        """
        try:
            with Cliente.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO reserva (idCliente, idHabitacion, fechaInicio, fechaFin, estado) VALUES (%s, %s, %s, %s, %s)",
                    (
                        self.idCliente,
                        self.idHabitacion,
                        self.fechaInicio,
                        self.fechaFin,
                        self.estado,
                    ),
                )
            # Cliente.connection.commit()
            self.idReserva = cursor.lastrowid
        except Exception as e:
            # Cliente.connection.rollback()
            print(f"Error al guardar la reserva: {e}")
            raise e
        finally:
            Cliente.connection.close()

    def update(self):
        conn = DBConnection().connect()
        if not conn:
            raise Exception("No se puede establacer conexion con la base de datos")

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE reserva SET idCliente = %s, idHabitacion = %s, fechaInicio = %s, fechaFin = %s, estado = %s WHERE idReserva = %s",
                    (
                        self.idCliente,
                        self.idHabitacion,
                        self.fechaInicio,
                        self.fechaFin,
                        self.estado,
                        self.idReserva,
                    ),
                )
            cursor.commit()
            self.idReserva = cursor.lastrowid
        except Exception as e:
            conn.rollback()
            print(f"Error al guardar al cliente: {e}")
            raise e
        finally:
            conn.close()

    def delete(self):
        conn = DBConnection()
        conn.execute("DELETE FROM reserva WHERE idReserva = %s", (self.idReserva,))
        conn.commit()

    def cliente(self):
        from .cliente import Cliente

        return Cliente.find(self.idCliente)

    """def habitacion(self):
        from .habitacion import Habitacion
        return Habitacion.find(self.idHabitacion)"""
