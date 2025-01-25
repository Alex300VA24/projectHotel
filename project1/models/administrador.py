# models/usuario.py
from .db import DBConnection
#import bcrypt

class Administrador:
    @staticmethod
    def validar_usuario(correo, password):
        try:
            db = DBConnection()
            db.connect()
            
            query = "SELECT * FROM administrador WHERE correo = %s AND contrasenia = %s"
            result = db.query(query, (correo, password))
            
            # Cerrar la conexión
            db.disconnect()

            return bool(result)

        except Exception as e:
            raise Exception(f"Error validando usuario: {e}")
