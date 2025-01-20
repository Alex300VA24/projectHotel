# view.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QAbstractListModel, QVariant
from model import Model


class ItemListModel(QAbstractListModel):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items

    def rowCount(self, parent=None):
        return len(self.items)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            item = self.items[index.row()]
            return f"{item.name} - {item.value}"


class View(QWidget):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model

        self.setWindowTitle("MVC Example")

        self.layout = QVBoxLayout(self)

        self.listView = QListView(self)
        self.layout.addWidget(self.listView)

        self.addButton = QPushButton("Add Item", self)
        self.layout.addWidget(self.addButton)

        self.update_view()

    def update_view(self):
        self.listModel = ItemListModel(self.model.get_items())
        self.listView.setModel(self.listModel)
