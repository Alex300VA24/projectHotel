# controller.py
from PyQt6.QtCore import pyqtSignal
from view import View
from model import Model


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Conectar la señal del botón a la función que maneja la adición de ítems
        self.view.addButton.clicked.connect(self.on_add_item)

    def on_add_item(self):
        '''new_item = Item("New Item", 100)  # Crear un nuevo ítem
        self.model.add_item(new_item)     # Añadir el ítem al modelo
        self.view.update_view() '''          # Actualizar la vista
        pass
