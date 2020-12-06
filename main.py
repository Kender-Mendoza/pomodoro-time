import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from modules.Chronometer import Chronometer

import threading
from concurrent.futures import Future

import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

# this class will create the main window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/mainWindow.ui", self)
        
        self.timer = Chronometer(2)
        self.count = 0

        # events
        self.start.clicked.connect(self._btnStart)
        self.pause.clicked.connect(self._btnPause)
        self.thread = None
        
        # Futures - Async
        self.future = Future()
        self.future.add_done_callback(self._chronometerFinish)
        #self.future.add_done_callback() # Se le debe de asignar la funcion para reiniciar

    def _btnStart(self):    
        '''
        Se le asigna un hilo al chronometro para que se ejecute aparte y no
        deterga la ejecucion de la interface.
        '''
        self.thread = threading.Thread(
            target=(lambda: self.future.set_result(self.timer.start(self._updateChronometerView))),
            daemon=True
        )

        self.thread.start()
    
    def _btnPause(self):
        self.timer.pause()

    def _updateChronometerView(self,minute,second):
        self.min.setText(str(minute))
        self.sec.setText(str(second))
        logging.info(f'{minute}:{second}')

    # esta funcion esperara el resultado del cronometro
    def _chronometerFinish(self,p):
        self.count += p.result()

        if self.count%2 != 0:
            self.counter.setText(str(p.result()))
            logging.info(f'{self.count}')
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
