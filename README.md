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

## Menu Principal

Aquí se muestra el menú principal del programa:

<img width="992" height="781" alt="image" src="https://github.com/user-attachments/assets/5b056464-6f25-4fe1-b0e3-a613ae2a9803" />


---

## 🚀 Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/Alex300VA24/projectHotel.git
   cd HotelDesk

2. **Instala dependencias**:

   ```bash
   pip install -r requirements.txt

3. **Para ejecutar la aplicación:**:

    ```bash
    python main.py

4. **Genera la Base de Datos**:

    Este proyecto usa una base de datos MySQL.

    Opción 1: MySQL / MariaDB
    Abre tu cliente de MySQL (por ejemplo, MySQL Workbench o consola).

    Ejecuta el archivo db_hotel.sql ubicado en resources/db/.. :

        SOURCE ruta/al/archivo/db_hotel.sql;

    Opcion 2: En consola


        mysql -u tu_usuario -p < db_hotel.sql
        



