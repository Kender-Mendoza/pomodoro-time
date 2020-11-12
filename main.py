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

        self.reiniciar.setEnabled(False)
        self.pausar.setVisible(False)
        self.saltar.setVisible(False)

        # events of the btn
        self.iniciar.clicked.connect(self._pushInit)
        self.pausar.clicked.connect(self._pushPause)
        self.reiniciar.clicked.connect(self._pushRestart)
        self.saltar.clicked.connect(self._pushSkip)

    def _pushInit(self):
        self.iniciar.setVisible(False)
        self.pausar.setVisible(True)
        self.reiniciar.setEnabled(True)
        self.reiniciar.setVisible(True)
        self.saltar.setVisible(False)
        self.timer.init()
    
    def _pushPause(self):
        self.iniciar.setText("Continuar")
        self.iniciar.setVisible(True)
        self.pausar.setVisible(False)
        self.saltar.setVisible(True)
        self.reiniciar.setVisible(False)
        self.timer.pause()

    def _pushRestart(self):
        self.iniciar.setText("Iniciar")
        self.iniciar.setVisible(True)
        self.reiniciar.setEnabled(False)
        self.pausar.setVisible(False)
        self.saltar.setVisible(False)
        self.timer.restart()

    def _pushSkip(self):
        self._pushRestart()
        self.reiniciar.setVisible(True)
        # se debe de aumentar el pomodoro        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
