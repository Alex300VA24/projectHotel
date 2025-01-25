# model/db.py
import mysql.connector  # type: ignore
from mysql.connector import Error # type: ignore
from config import config
import bcrypt


class DBConnection:
    def __init__(self):
        self.connection = None
        self.host = config.DATABASE_CONFIG["host"]
        self.user = config.DATABASE_CONFIG["user"]
        self.password = config.DATABASE_CONFIG["password"]
        self.database = config.DATABASE_CONFIG["database"]
        self.port = config.DATABASE_CONFIG["port"]

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port = self.port
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
    
    



