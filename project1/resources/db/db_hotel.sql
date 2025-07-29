drop database if exists Hotel;
create database if not exists Hotel;
use Hotel;


CREATE TABLE administrador (
	idAdministrador BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombres VARCHAR(50), 
    apellidoPaterno VARCHAR(30),
    apellidoMaterno VARCHAR(30),
    correo VARCHAR(100),
    contrasenia VARCHAR(100)
);

CREATE TABLE cliente (
  idCliente BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombres VARCHAR(50) NOT NULL,
  apellidoPaterno VARCHAR(30) NOT NULL,
  apellidoMaterno VARCHAR(30) NOT NULL,
  tipoDocumento ENUM('dni', 'pasaporte') NOT NULL,
  documentoIdentidad VARCHAR(10) UNIQUE NOT NULL,
  paisOrigen VARCHAR(20) NOT NULL,
  telefono VARCHAR(9)
);

CREATE TABLE Tipo_Habitacion (
  idTipoHabitacion BIGINT PRIMARY KEY AUTO_INCREMENT,
  tipo ENUM('simple', 'doble', 'matrimonial', 'suit') NOT NULL,
  precioNoche DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Habitacion (
  idHabitacion BIGINT PRIMARY KEY AUTO_INCREMENT,
  numeroHabitacion CHAR(3) UNIQUE NOT NULL,
  idTipo_Habitacion BIGINT NOT NULL,
  estado ENUM('disponible', 'ocupada', 'pendiente', 'mantenimiento') NOT NULL,
  FOREIGN KEY (idTipo_Habitacion) REFERENCES Tipo_Habitacion(idTipoHabitacion)
);

CREATE TABLE reserva (
  idReserva BIGINT PRIMARY KEY AUTO_INCREMENT,
  idCliente BIGINT NOT NULL,
  idHabitacion BIGINT NOT NULL,
  fechaInicio DATE NOT NULL,
  fechaFin DATE NOT NULL,
  estado ENUM('pagada', 'cancelada', 'pendiente') NOT NULL,
  total REAL NOT NULL,
  FOREIGN KEY (idCliente) REFERENCES cliente(idCliente),
  FOREIGN KEY (idHabitacion) REFERENCES habitacion(idHabitacion)
);

CREATE TABLE servicio (
  idServicio BIGINT PRIMARY KEY AUTO_INCREMENT,
  idCliente BIGINT NOT NULL,
  concepto VARCHAR(100) NOT NULL,
  descripcion TEXT,
  costoServicio DECIMAL(10, 2) NOT NULL,
  fechaConsumo DATE NOT NULL,
  
  FOREIGN KEY (idCliente) REFERENCES cliente(idCliente)
);


-- Tabla de Detalles de Servicios
CREATE TABLE detalle_servicio (
    idDetalle BIGINT AUTO_INCREMENT PRIMARY KEY,
    idServicio BIGINT,
    detalle VARCHAR(255) NOT NULL,
    precio REAL NOT NULL,
    FOREIGN KEY (idServicio) REFERENCES servicio(idServicio) ON DELETE CASCADE
);


-- REGISTROS

-- Insertar registros en la tabla administrador
INSERT INTO administrador (nombres, apellidoPaterno, apellidoMaterno, correo, contrasenia)
VALUES 
('Carlos', 'García', 'Pérez', 'carlos.garcia@hotelperu.com', 'admin123'),
('Lucía', 'Martínez', 'Sánchez', 'lucia.martinez@hotelperu.com', 'admin456');

-- Insertar registros en la tabla cliente
INSERT INTO cliente (nombres, apellidoPaterno, apellidoMaterno, tipoDocumento, documentoIdentidad, paisOrigen, telefono)
VALUES 
('Juan','Torres', 'Vega', 'dni','12345678', 'Peru','987654321'),
('Ana', 'López', 'Ramos', 'dni','98765432','Peru','987123456'),
('Luis', 'Guzmán', 'Flores', 'pasaporte','A12345678','Argentina','986543210');



-- Insertar registros en la tabla Tipo_Habitacion
INSERT INTO Tipo_Habitacion (tipo, precioNoche)
VALUES 
('simple', 150.00),
('doble', 250.00),
('matrimonial', 350.00),
('suit', 500.00);


-- Insertar registros en la tabla Habitacion
INSERT INTO Habitacion (numeroHabitacion, idTipo_Habitacion, estado)
VALUES 
('101', 1, 'disponible'),
('102', 1, 'ocupada'),
('201', 2, 'disponible'),
('202', 2, 'pendiente'),
('301', 3, 'disponible'),
('302', 3, 'mantenimiento'),
('401', 4, 'ocupada');


-- Insertar registros en la tabla reserva
INSERT INTO reserva (idCliente, idHabitacion, fechaInicio, fechaFin, estado, total)
VALUES 
(1, 1, '2025-01-20', '2025-01-22', 'pagada', 100.00),
(2, 3, '2025-01-21', '2025-01-24', 'pendiente', 200.00),
(3, 7, '2025-01-19', '2025-01-25', 'cancelada', 150.00);

-- Insertar registros en la tabla servicio
INSERT INTO servicio (idCliente, concepto, descripcion, costoServicio, fechaConsumo)
VALUES
(1, 'Desayuno a la Cama', 'Desayuno variado servido en la habitación.', 50.00, '2025-01-20'),
(2, 'Menú Nocturno', 'Opciones de comida ligera para la noche.', 30.00, '2025-01-21'),
(3, 'Menú Infantil', 'Comidas especiales para niños.', 100.00, '2025-01-22'),
(1, 'Lavanderia', 'Servicios de lavado y planchado.', 40.00, '2025-02-01'),
(2, 'Bebidas', 'Variedad de bebidas alcohólicas y no alcohólicas.', 40.00, '2025-03-02'),
(3, 'Postres', 'Postres gourmet y tradicionales.', 35.00, '2025-01-30'),
(1, 'Spa', 'Tratamientos de relajación y bienestar.', 30.00, '2025-02-06'),
(2, 'Entretenimiento', 'Opciones de entretenimiento en la habitación.', 60.00, '2025-04-01'); 




-- Insertar Detalles para Desayuno a la Cama
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(1, 'Café espresso con granos arábica', 12.00),
(1, 'Cappuccino con leche entera y crema', 14.00),
(1, 'Huevos fritos con mantequilla', 18.00),
(1, 'Tostadas de pan artesanal con mermelada', 15.00),
(1, 'Ensalada de frutas', 20.00);

-- Insertar Detalles para Menú Nocturno
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(2, 'Mini slider de pollo con mayonesa', 24.00),
(2, 'Taco de camarones', 24.00),
(2, 'Crema de champiñones con queso parmesano', 18.00),
(2, 'Brownie de chocolate oscuro', 20.00),
(2, 'Cheesecake de frutos rojos con galleta', 22.00);

-- Insertar Detalles para Menú Infantil
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(3, 'Nuggets de pollo empanizados con panko', 18.00),
(3, 'Mini pizza de jamón con queso mozzarella', 20.00),
(3, 'Mini pizza de pepperoni con salsa de tomate', 20.00),
(3, 'Spaghetti a la boloñesa con carne de res', 22.00),
(3, 'Batido de fresa con leche entera y miel', 15.00);

-- Insertar Detalles para Lavandería
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(4, 'Lavado express de ropa casual', 30.00),
(4, 'Lavado de prendas delicadas', 35.00),
(4, 'Planchado de camisas con vapor', 25.00),
(4, 'Planchado de trajes', 30.00);

-- Insertar Detalles para Bebidas
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(5, 'Café latte con leche vaporizada', 14.00),
(5, 'Espresso doble con frutos secos', 14.00),
(5, 'Mojito cubano con ron y hierbabuena', 28.00),
(5, 'Margarita de maracuyá con tequila reposado', 28.00),
(5, 'Pisco Sour con clara de huevo y jarabe de goma', 26.00);

-- Insertar Detalles para Postres
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(6, 'Volcán de chocolate', 25.00),
(6, 'Cheesecake de maracuyá', 22.00),
(6, 'Tiramisú clásico con cacao', 24.00),
(6, 'Alfajor relleno de dulce de leche', 15.00),
(6, 'Crème brûlée de vainilla', 23.00);

-- Insertar Detalles para Spa
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(7, 'Masaje relajante con aceites esenciales de lavanda', 120.00),
(7, 'Masaje descontracturante con piedras calientes', 130.00),
(7, 'Baño de burbujas con sales aromáticas', 80.00),
(7, 'Terapia facial hidratante con colágeno', 100.00),
(7, 'Exfoliación corporal con café y coco', 95.00);

-- Insertar Detalles para Entretenimiento
INSERT INTO detalle_servicio (idServicio, detalle, precio) VALUES
(8, 'Cine privado', 150.00),
(8, 'Alquiler de PlayStation', 100.00),
(8, 'Alquiler de Xbox', 90.00),
(8, 'Sistema de karaoke con micrófonos inalámbricos', 80.00),
(8, 'Mix de snacks gourmet', 35.00);

