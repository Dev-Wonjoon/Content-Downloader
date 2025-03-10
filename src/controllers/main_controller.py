from PySide6.QtWidgets import QMainWindow
from src.views.main_window import MainWindowView

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = MainWindowView()