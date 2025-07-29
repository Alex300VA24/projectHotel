# 🏨 HotelDesk - Sistema de Gestión Hotelera

**HotelDesk** es una aplicación de escritorio desarrollada en Python con PyQt6 que permite a los hoteles gestionar de manera eficiente sus operaciones. El sistema implementa la arquitectura **MVC (Modelo-Vista-Controlador)**, asegurando una separación clara entre lógica, interfaz y control de datos.

---

## 📌 Características Principales

- 📦 **Servicio a la Habitación:** Permite registrar pedidos de servicios a los huéspedes.
- 🛏️ **Reservar Habitación:** Gestión de reservas con asignación automática de habitaciones disponibles.
- 📖 **Historial de Reservas:** Visualización del historial de reservas realizadas por los clientes.
- 👤 **Clientes Registrados:** Listado completo de todos los clientes del sistema.
- 🏠 **Habitaciones Disponibles:** Muestra en tiempo real las habitaciones libres para ser reservadas.

---

## 🧱 Arquitectura

Este proyecto está estructurado siguiendo el patrón de diseño **MVC**:

- **Modelo (`/models`)**: Gestión de datos, consultas y lógica de negocio.
- **Vista (`/views`)**: Interfaz gráfica desarrollada con PyQt6.
- **Controlador (`/controllers`)**: Comunicación entre la vista y el modelo.

---

## 📷 Menú Principal

Aquí se muestra el menú principal del programa:

<img width="992" height="781" alt="Menú Principal" src="https://github.com/user-attachments/assets/5b056464-6f25-4fe1-b0e3-a613ae2a9803" />

---

## 🚀 Instalación

Sigue los siguientes pasos para ejecutar la aplicación correctamente:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Alex300VA24/projectHotel.git
   cd HotelDesk
Instala las dependencias:


pip install -r requirements.txt
Ejecuta la aplicación:


python main.py
🛠️ Generar la Base de Datos
Este proyecto utiliza una base de datos MySQL.

Opción 1: Usando un cliente MySQL (Workbench, consola, DBeaver)
Abre tu cliente de base de datos.

Ejecuta el script db_hotel.sql ubicado en resources/db/:


SOURCE resources/db/db_hotel.sql;
Opción 2: Desde la línea de comandos (terminal)

mysql -u tu_usuario -p < resources/db/db_hotel.sql
🔐 Asegúrate de que las credenciales (usuario, contraseña, base de datos) coincidan con tu archivo de configuración o conexión.

📁 Estructura del Proyecto

HotelDesk/
│
├── controllers/           # Lógica del controlador
├── models/                # Gestión de datos y lógica de negocio
├── views/                 # Interfaces gráficas en PyQt6
├── resources/
│   └── db/
│       └── db_hotel.sql   # Script SQL para crear la base de datos
├── assets/                # Imágenes, íconos, etc.
├── main.py                # Punto de entrada principal
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación
