import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modules.Chronometer import Chronometer

# this class will create the main window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/mainWindow.ui", self)
        self.timer = Chronometer(5, self.min, self.sec)

        # events of the btn
        self.iniciar.clicked.connect(self.timer.init)
        self.pausar.clicked.connect(self.timer.pause)

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
