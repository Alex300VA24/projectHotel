from .db import DBConnection

'''
CREATE TABLE cliente (
  idCliente BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombres VARCHAR(50) NOT NULL,
  apellidoPaterno VARCHAR(30) NOT NULL,
  apellidoMaterno VARCHAR(30) NOT NULL,
  telefono CHAR(9)
);

'''

class Cliente:
    def __init__(self, idCliente, nombres, apellidoPaterno, apellidoMaterno, telefono):
        self.idCliente = idCliente
        self.nombres = nombres
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.telefono = telefono

    @staticmethod
    def all():
        conn = DBConnection()
        cursor = conn.execute("SELECT * FROM cliente")
        clientes = []
        for row in cursor.fetchall():
            clientes.append(Cliente(row[0], row[1], row[2], row[3], row[4]))
        return clientes

    @staticmethod
    def find(idCliente):
        conn = DBConnection()
        cursor = conn.execute("SELECT * FROM cliente WHERE idCliente = %s", (idCliente,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Cliente(row[0], row[1], row[2], row[3], row[4])

    def save(self):
        conn = DBConnection()
        cursor = conn.execute(
            "INSERT INTO cliente (nombres, apellidoPaterno, apellidoMaterno, telefono) VALUES (%s, %s, %s, %s)",
            (self.nombres, self.apellidoPaterno, self.apellidoMaterno, self.telefono))
        conn.commit()
        self.idCliente = cursor.lastrowid

    def update(self):
        conn = DBConnection()
        conn.execute("UPDATE cliente SET nombres = %s, apellidoPaterno = %s, apellidoMaterno = %s, telefono = %s WHERE idCliente = %s",
                     (self.nombres, self.apellidoPaterno, self.apellidoMaterno, self.telefono, self.idCliente))
        conn.commit()

    def delete(self):
        conn = DBConnection()
        conn.execute("DELETE FROM cliente WHERE idCliente = %s", (self.idCliente,))
        conn.commit()

    def reservas(self):
        from .reserva import Reserva
        return Reserva.all_by_cliente(self.idCliente)