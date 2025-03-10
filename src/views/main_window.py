from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QLabel

class MainWindowView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contant Downloader")
        self.resize(1440, 900)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        url_layout = QHBoxLayout()
        self.url_inputLine = QLineEdit()
        self.url_inputLine.setPlaceholderText("URL을 입력하세요")
        self.download_button = QPushButton("다운로드")

        url_layout.addWidget(self.url_inputLine)
        url_layout.addWidget(self.download_button)

        self.downloaded_files_list = QListWidget()

        main_layout.addLayout(url_layout)
        main_layout.addWidget(QLabel("Downloaded Files: "))
        main_layout.addWidget(self.downloaded_files_list)