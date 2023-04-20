from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import *
from PySide6.QtGui import QColor, QPalette

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tetris Game by Julian")

        color = Color("gray")

        layout = QVBoxLayout()

        start_button = QPushButton("Start Game")
        start_button.clicked.connect(self.start_button_clicked)
        settings_button = QPushButton("Settings")
        settings_button.clicked.connect(self.settings_button_clicked)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit_button_clicked)

        layout.addWidget(start_button)
        layout.addWidget(settings_button)
        layout.addWidget(exit_button)
        layout.addWidget(color)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def start_button_clicked(self):
        print("Starting Game!")
        self.setEnabled(False)
    
    def settings_button_clicked(self):
        print("Starting Game!")
        self.setEnabled(False)

    def exit_button_clicked(self):
        print("Ending Game!")
        self.setEnabled(False)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


