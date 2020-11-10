import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modules.Chronometer import Chronometer

# this class will create the main window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/mainWindow.ui", self)
        self.timer = Chronometer(2, self.min, self.sec)
        self.pausar.clicked.connect(self.timer.pause)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
