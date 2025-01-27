# model/db.py
import mysql.connector  # type: ignore
from mysql.connector import Error  # type: ignore

# config/config.py
DATABASE_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "Hotel",
    "port": 3306,
}


class DBConnection:
    def __init__(self):
        self.connection = None
        self.host = DATABASE_CONFIG["host"]
        self.user = DATABASE_CONFIG["user"]
        self.password = DATABASE_CONFIG["password"]
        self.database = DATABASE_CONFIG["database"]
        self.port = DATABASE_CONFIG["port"]

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")

    def query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()


class TipoHabitacion:
    def __init__(self, tipo=None, precio_noche=None):
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
                habitaciones.append(TipoHabitacion(tipo, precio_noche))

            db.disconnect()
            return habitaciones
        except Exception as e:
            raise Exception(f"Error consultando tipo de habitación: {e}")

        # self.tipo = tipo
        # self.precio_noche = precio_noche


tipo_habitacion = TipoHabitacion()
habitaciones = tipo_habitacion.obtener_todos()

