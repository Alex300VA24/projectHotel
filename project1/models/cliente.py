from sqlite3 import Cursor
from .db import DBConnection
import mysql.connector  # type: ignore
from mysql.connector import Error  # type: ignore


class Cliente:
    connection = None

    def __init__(
        self,
        idCliente,
        nombres,
        apellido_paterno,
        apellido_materno,
        tipo_documento,
        documento,
        pais,
        telefono,
    ):
        self._idCliente = idCliente
        self.nombres = nombres
        self.apellidoPaterno = apellido_paterno
        self.apellidoMaterno = apellido_materno
        self.tipoDocumento = tipo_documento
        self.documento = documento
        self.pais = pais
        self.telefono = telefono

    @staticmethod
    def conseguir_clientes():
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            query = """
                SELECT * FROM cliente
            """
            resultado = conexion.query(query)
            conexion.disconnect()
            return resultado
        
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
            print(precio_reserva)
            conexion.disconnect()
            return precio_reserva
        
    @staticmethod
    def conseguir_total_servicio(id):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            query = """
                SELECT idServicio, concepto, descripcion, costoServicio FROM servicio WHERE idCliente = %s
            """
            resultado_servicio = conexion.query(query, (id,))
            print(resultado_servicio)
            return resultado_servicio
        
    @staticmethod
    def conseguir_total_detalle_servicio(id):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            query = """
                SELECT detalle, precio FROM detalle_servicio WHERE idServicio = %s
            """
            resultado_detalle_servicio = conexion.query(query, (id,))
            print(resultado_detalle_servicio)
            return resultado_detalle_servicio

    def get_idCliente(self):
        return self._idCliente

    @staticmethod
    def iniciar_transaccion():
        Cliente.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Hotel",
        )
        Cliente.connection.start_transaction()

    @staticmethod
    def commit_transaccion():
        if Cliente.connection:
            Cliente.connection.commit()
            Cliente.connection.close()
            Cliente.connection = None

    @staticmethod
    def rollback_transaccion():
        if Cliente.connection:
            Cliente.connection.rollback()
            Cliente.connection.close()
            Cliente.connection = None

    def save(self):
        # Crear una conexión a la base de datos
        """conn = (
            DBConnection().connect()
        )  # Asegúrate de que el método connect() retorne una conexión válida

        if not conn:
            raise Exception("No se pudo establecer la conexión a la base de datos")
        """
        try:
            with Cliente.connection.cursor() as cursor:  # Usa el cursor correctamente
                # Ejecutar la consulta SQL
                cursor.execute(
                    """
                    INSERT INTO cliente (
                        nombres, apellidoPaterno, apellidoMaterno,
                        tipoDocumento, documentoIdentidad, paisOrigen, telefono
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        self.nombres,
                        self.apellidoPaterno,
                        self.apellidoMaterno,
                        self.tipoDocumento,
                        self.documento,
                        self.pais,
                        self.telefono,
                    ),
                )
                # Cliente.connection.commit()  # Confirmar los cambios en la base de datos
                self._idCliente = cursor.lastrowid  # Obtener el ID generado
                print("id del cliente generado: {}".format(self.get_idCliente()))
        except Exception as e:
            Cliente.connection.rollback()  # Revertir los cambios en caso de error
            print(f"Error al guardar el cliente: {e}")
        return self._idCliente

    def update(self):
        conn = DBConnection()
        conn.execute(
            "UPDATE cliente SET nombres = %s, apellidoPaterno = %s, apellidoMaterno = %s, telefono = %s WHERE idCliente = %s",
            (
                self.nombres,
                self.apellidoPaterno,
                self.apellidoMaterno,
                self.telefono,
                self.idCliente,
            ),
        )
        conn.commit()

    def delete(self):
        conn = DBConnection()
        conn.execute("DELETE FROM cliente WHERE idCliente = %s", (self.idCliente,))
        conn.commit()

    def consultar_idCliente(self):
        conn = DBConnection()
        cursor = conn.execute(
            "SELECT idCliente FROM cliente WHERE documentoIdentidad = %s",
            (self.documento,),
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return row[0]
