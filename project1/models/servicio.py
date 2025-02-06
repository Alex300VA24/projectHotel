from csv import Error
from .db import DBConnection


class Servicio:
    def __init__(
        self,
        id_servicio=None,
        concepto=None,
        descripcion=None,
        costo_servicio=None,
        fecha_consumo=None,
    ):
        self.id_servicio = id_servicio
        self.concepto = concepto
        self.descripcion = descripcion
        self.costo_servicio = costo_servicio
        self.fecha_consumo = fecha_consumo

    @classmethod
    def crear_servicio(cls, concepto, descripcion, costo_servicio, fecha_consumo):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
                INSERT INTO servicio (concepto, descripcion, costoServicio, fechaConsumo)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(
                query, (concepto, descripcion, costo_servicio, fecha_consumo)
            )
            conexion.commit()
            cursor.close()
            conexion.close()

    @classmethod
    def obtener_todos_los_servicios(cls):
        """Obtiene todos los nombres de los servicios disponibles."""
        conexion = DBConnection()
        conexion.connect()

        try:
            query = "SELECT concepto FROM servicio"
            resultados = conexion.query(query)
            servicios = [
                fila[0] for fila in resultados
            ]  # Asumiendo que fetchall() devuelve una lista de tuplas
        except Exception as e:
            cls.mostrar_error(f"Error obteniendo servicios: {e}")
            servicios = []
        finally:
            conexion.disconnect()

        return servicios

    @classmethod
    def obtener_detalles(cls, nombre_servicio):
        """Obtiene los detalles de un servicio específico."""
        conexion = DBConnection()
        conexion.connect()

        try:
            query = """
                SELECT d.detalle
                FROM servicio s
                JOIN detalle_servicio d ON s.idServicio = d.idServicio
                WHERE s.concepto = %s
            """
            resultados = conexion.query(query, (nombre_servicio,))
            detalles = [
                fila[0] for fila in resultados
            ]  # Asumiendo que fetchall() devuelve una lista de tuplas
        except Exception as e:
            cls.mostrar_error(f"Error obteniendo detalles del servicio '{nombre_servicio}': {e}")
            detalles = []
        finally:
            conexion.disconnect()

        return detalles

    @classmethod
    def obtener_precios(cls, nombre_servicio):
        """
        Obtiene los detalles y precios de un servicio a partir de su nombre.
        :param nombre_servicio: Nombre del servicio en la tabla servicio.
        :return: Diccionario {detalle: precio}.
        """
        precios = {}

        db = DBConnection()
        connection = db.connect()  # Establecer la conexión

        if connection:
            try:
                # Obtener idServicio desde el nombre del servicio
                query_id = "SELECT idServicio FROM servicio WHERE concepto = %s"
                resultado_id = db.query(query_id, (nombre_servicio,))

                if not resultado_id:
                    cls.mostrar_mensaje(f"No se encontró el servicio: {nombre_servicio}")
                    return precios  # Retorna vacío si no encuentra el servicio

                id_servicio = resultado_id[0][0]  # Extraer el ID del resultado

                # Obtener los detalles y precios usando el idServicio
                query_precios = """
                    SELECT detalle, precio 
                    FROM detalle_servicio 
                    WHERE idServicio = %s
                """
                resultados = db.query(query_precios, (id_servicio,))

                # Convertimos los resultados en un diccionario {detalle: precio}
                for detalle, precio in resultados:
                    precios[detalle] = precio

            except Exception as e:
                cls.mostrar_error(f"Error al obtener los precios: {e}")

            finally:
                db.disconnect()  # Cerrar la conexión

        return precios
    
    # Método para conseguir información del servicio según el id del cliente que se ingresa
    @staticmethod
    def conseguir_total_servicio(id):
        conexion = DBConnection()
        conexion.connect()
        if conexion:
            query = """
                SELECT idServicio, concepto, descripcion, costoServicio FROM servicio WHERE idCliente = %s
            """
            resultado_servicio = conexion.query(query, (id,))
            return resultado_servicio    

    def save(self, nombre_cliente):
        """
        Guarda un nuevo servicio en la base de datos, utilizando el nombre del cliente.
        :param nombre_cliente: Nombre del cliente para buscar en la base de datos.
        :param concepto: Concepto del servicio.
        :param descripcion: Descripción del servicio.
        :param costo_total: Costo total del servicio.
        :return: Mensaje de éxito o error.
        """
        db = DBConnection()
        connection = db.connect()

        if not connection:
            return "Error: No se pudo conectar a la base de datos."

        try:
            cursor = connection.cursor()

            # Verificar si el cliente existe usando el nombre
            cursor.execute(
                "SELECT idCliente FROM cliente WHERE CONCAT(nombres, ' ', apellidoPaterno) = %s",
                (nombre_cliente,),
            )
            cliente = cursor.fetchone()

            if not cliente:
                return "Error: Cliente no encontrado."

            # Insertar el servicio
            query = """INSERT INTO servicio (idCliente, concepto, descripcion, costoServicio, fechaConsumo) 
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(
                query,
                (
                    cliente[0],
                    self.concepto,
                    self.descripcion,
                    self.costo_servicio,
                    self.fecha_consumo,
                ),
            )

            connection.commit()
            return "Servicio registrado correctamente."

        except Error as e:
            connection.rollback()
            return f"Error al registrar el servicio: {e}"

        finally:
            cursor.close()
            db.disconnect()
