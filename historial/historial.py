import mysql.connector

class Historial:
    def __init__(self, db_config):
        self.db_config = db_config

    def obtener_historial_reservas(self):
        try:
            # Conexión a la base de datos
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor(dictionary=True)

            # Consulta SQL para unir las tablas Reserva, Habitacion y Tipo_Habitacion
            query = """
                SELECT 
                    r.idCliente,
                    CONCAT(c.nombres, ' ', c.apellidoPaterno, ' ', c.apellidoMaterno) AS nombre_completo,
                    r.fechaInicio AS fecha_reserva,
                    r.fechaFin AS fecha_salida,
                    h.numeroHabitacion AS numero_habitacion,
                    th.tipo AS tipo_habitacion,
                    h.estado AS estado_habitacion,
                    r.total AS monto
                FROM reserva r
                JOIN cliente c ON r.idCliente = c.idCliente
                JOIN habitacion h ON r.idHabitacion = h.idHabitacion
                JOIN tipo_habitacion th ON h.idTipo_Habitacion = th.idTipoHabitacion;
            """

            cursor.execute(query)
            resultados = cursor.fetchall()

            return resultados

        except mysql.connector.Error as err:
            print(f"Error al consultar la base de datos: {err}")
            return []

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()