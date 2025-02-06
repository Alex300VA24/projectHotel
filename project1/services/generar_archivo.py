from fpdf import FPDF
from controllers.servicio_controller import ServicioController
from PyQt6.QtWidgets import QMessageBox

class GenerarArchivo:
    def __init__(self, dynamic_window):
        self.dynamic_window = dynamic_window  # Esto es para interactuar con la ventana de la interfaz, si es necesario
        
    def generar_pdf(self, nombre, celular, precio_reserva, resumen_servicio, id_servicio):
        """Genera un PDF con la información de la ventana."""
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        pdf.set_font("Arial", size=12)

        # Se agrega el título
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="Resumen de Gasto del Cliente", ln=True, align='C')
        
        # Se agregan los detalles
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(100, 10, f"Nombre: {nombre}")
        pdf.ln(10)
        pdf.cell(100, 10, f"Celular: {celular}")
        pdf.ln(10)        

        # Resumen de servicios
        pdf.ln(10)
        pdf.cell(100, 10, "Resumen de los Servicios:")
        pdf.ln(10)
        
        i = 0
        total_servicio = 0
        for dato_servicio in resumen_servicio:
            pdf.cell(100, 10, f"{i + 1}. {dato_servicio[1]} - {dato_servicio[2]} - S/.{dato_servicio[3]}", ln=True)
            total_servicio += dato_servicio[3]
            i += 1           
        
        pdf.cell(100, 10, f"Total de los servicios solicitados: S/.{total_servicio}")
        pdf.ln(10)
        
        pdf.cell(100, 10, f"Total de la reserva: S/.{precio_reserva}", ln=True)
        pdf.ln(10)
        
        # Total general (reserva + servicios)
        total_estadia = float(precio_reserva) + float(total_servicio)
        pdf.cell(100, 10, f"Coste total: S/.{total_estadia}")
        
        # Guardar el archivo PDF
        pdf_output_path = f"Resumen_Gasto_{nombre}.pdf"
        pdf.output(pdf_output_path)
        
        QMessageBox.information(self.dynamic_window, "PDF Generado", f"El PDF ha sido generado y guardado en {pdf_output_path}")