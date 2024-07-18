import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        """ Constructor for empty window """
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application """
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty window in PyQt 6")
        self.show()  # Show window on screen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())