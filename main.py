import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from modules.Chronometer import Chronometer

import threading
from concurrent.futures import Future

import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

# this class will create the main window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/mainWindow.ui", self)
        
        self.timer = Chronometer(2)
        self.pause.clicked.connect(self._test)

        # Async
        self.thread = threading.Thread(
            target= self.timer.start,
            args=(self._updateChronometerView, ),
            daemon=True
        )
        self.thread.start()

    def _updateChronometerView(self,minute,second):
        self.min.setText(str(minute))
        self.sec.setText(str(second))
        logging.info(f'{minute}:{second}')

    def _test(self):
        logging.info("Estoy saludando de forma asyncrona")
        

    # esta funcion esperara el resultado del cronometro
    def _chronometerFinish(self,p):
        result = p.result()
        if result%2 != 0:
            self.counter.setText(str(p.result()))
            print(format(p.result()))
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
