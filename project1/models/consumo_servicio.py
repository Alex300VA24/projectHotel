# from .db import DBConnection

"""CREATE TABLE Consumo_Servicio (
  idConsumoServicio BIGINT PRIMARY KEY AUTO_INCREMENT,
  idReserva BIGINT NOT NULL,
  idServicio BIGINT NOT NULL,
  costoConsumoServicio DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (idReserva) REFERENCES reserva(idReserva),
  FOREIGN KEY (idServicio) REFERENCES servicio(idServicio)
);"""
