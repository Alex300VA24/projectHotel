from sqlalchemy import Column, BigInteger, String, Enum, DECIMAL, CHAR, ForeignKey, TEXT, Date #type: ignore
from sqlalchemy.orm import relationship #type: ignore
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from .db import Base

class Administrador(Base):
    __tablename__ = 'administrador'
    
    idAdministrador = Column(BigInteger, primary_key=True, autoincrement=True)
    nombres = Column(String(50))
    apellidoPaterno = Column(String(30))
    apellidoMaterno = Column(String(30))
    correo = Column(String(100))
    contrasenia = Column(String(100))

    @classmethod
    def crear_administrador(cls, session):
        # Comprobar si ya existe un administrador
        if not session.query(cls).first():  # Si no hay administrador, lo crea
            correo = 'admin@ejemplo.com'
            contrasenia = '12345'
            hashed_password = generate_password_hash(contrasenia)

            # Crear el objeto Administrador
            nuevo_administrador = cls(correo=correo, contrasenia=hashed_password)
            session.add(nuevo_administrador)
            session.commit()
            print("Administrador creado con éxito.")
        else:
            print("Ya existe un administrador registrado.")

    def verificar_contrasenia(self, password: str) -> bool:
        """Verifica si la contraseña proporcionada coincide con la almacenada"""
        return check_password_hash(self.contrasenia, password)


class Cliente(Base):
    __tablename__ = 'cliente'
    
    idCliente = Column(BigInteger, primary_key=True, autoincrement=True)
    nombres = Column(String(50), nullable=False)
    apellidoPaterno = Column(String(30), nullable=False)
    apellidoMaterno = Column(String(30), nullable=False)
    telefono = Column(CHAR(9))


class TipoHabitacion(Base):
    __tablename__ = 'tipo_habitacion'
    
    idTipoHabitacion = Column(BigInteger, primary_key=True, autoincrement=True)
    tipo = Column(Enum('simple', 'doble', 'matrimonial', 'suit'), unique=True, nullable=False)
    precioNoche = Column(DECIMAL(10, 2), nullable=False)


class Habitacion(Base):
    __tablename__ = 'habitacion'
    
    idHabitacion = Column(BigInteger, primary_key=True, autoincrement=True)
    numeroHabitacion = Column(CHAR(3), unique=True, nullable=False)
    idTipo_Habitacion = Column(BigInteger, ForeignKey('tipo_habitacion.idTipoHabitacion'), nullable=False)
    estado = Column(Enum('disponible', 'ocupada', 'pendiente', 'mantenimiento'), nullable=False)

    tipo_habitacion = relationship("TipoHabitacion")


class Reserva(Base):
    __tablename__ = 'reserva'
    
    idReserva = Column(BigInteger, primary_key=True, autoincrement=True)
    idCliente = Column(BigInteger, ForeignKey('cliente.idCliente'), nullable=False)
    idHabitacion = Column(BigInteger, ForeignKey('habitacion.idHabitacion'), nullable=False)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=False)
    estado = Column(Enum('pagada', 'cancelada', 'pendiente'), nullable=False)

    cliente = relationship("Cliente")
    habitacion = relationship("Habitacion")


class Servicio(Base):
    __tablename__ = 'servicio'
    
    idServicio = Column(BigInteger, primary_key=True, autoincrement=True)
    concepto = Column(String(100), nullable=False)
    descripcion = Column(TEXT)
    costoServicio = Column(DECIMAL(10, 2), nullable=False)
    fechaConsumo = Column(Date, nullable=False)


class ConsumoServicio(Base):
    __tablename__ = 'consumo_servicio'
    
    idConsumoServicio = Column(BigInteger, primary_key=True, autoincrement=True)
    idReserva = Column(BigInteger, ForeignKey('reserva.idReserva'), nullable=False)
    idServicio = Column(BigInteger, ForeignKey('servicio.idServicio'), nullable=False)
    costoConsumoServicio = Column(DECIMAL(10, 2), nullable=False)

    reserva = relationship("Reserva")
    servicio = relationship("Servicio")
