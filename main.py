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
    POMODORO = 10
    LONG_BREAK = 5
    SHORT_BREAK = 3

    def __init__(self):
        super().__init__()
        uic.loadUi("./views/mainWindow.ui", self)
        
        self.timer = Chronometer(self.POMODORO)
        self.count = 0
        self.pomoCount = 0

        # events btn
        self.start.clicked.connect(self._startChronometer)
        self.pause.clicked.connect(self._pauseChronometer)
        self.restart.clicked.connect(self._restartChronometer)
        self.skip.clicked.connect(self._skipChronometer)

        # order btn
        self._orderBtn('init')
        self.restart.setEnabled(False)

    def _startChronometer(self):
        if self._isPomodoro(): self._orderBtn('run')
        else: self._orderBtn('auto')
        self.restart.setEnabled(True)

        ''' Se le asigna un hilo al chronometro para que se ejecute aparte y no
        deterga la ejecucion de la interface.'''
        self.future = Future()
        self.future.add_done_callback(self._chronometerFinish)
        
        self.thread = threading.Thread(
            target=(lambda: self.future.set_result(self.timer.start(self._updateChronometerView))),
            daemon=True
        )
        self.thread.start()

    def _pauseChronometer(self):
        if self._isPomodoro(): self._orderBtn('init')
        else: self._orderBtn('break') 
        self.start.setText('Continuar')

        self.timer.pause()

    def _restartChronometer(self):
        self._orderBtn('init')
        self.start.setText('Iniciar')
        self.restart.setEnabled(False)
        
        self._restartView(self.POMODORO)
        
    def _skipChronometer(self):
        self._orderBtn('init')
        self.start.setText('Iniciar')
        self.restart.setEnabled(False)

        self.count += 1
        self._restartView(self.POMODORO)

    def _updateChronometerView(self,minute,second):
        self.min.setText(str(minute))
        self.sec.setText(str(second))
        logging.info(f'{minute}:{second}')
    
    # future callback
    def _chronometerFinish(self,p):
        if p.result():
            self.count += p.result()

            if self.count%2 != 0:
                self.pomoCount += 1
                self.counter.setText(str(self.pomoCount))

            minute = self._minuteQuantity() 
            self._restartView(minute)

            self._orderBtn('init')            
            self.start.setText('Iniciar')
            self.restart.setEnabled(False)

            '''Esta condicional es para que el descanso se active
            automaticamente'''    
            if not self._isPomodoro(): self._startChronometer()

        logging.info(f'Numero de Cronometros: {self.count}')
        logging.info(f'Numero de Pomodoros: {self.pomoCount}')

    # "Usual" methods    
    def _isPomodoro(self):
        if self.count%2 == 0: return True
        else: return False
    
    def _minuteQuantity(self):
        if self._isPomodoro(): return self.POMODORO
        else: 
            if self.pomoCount%4 == 0: return self.LONG_BREAK
            else: return self.SHORT_BREAK

    def _restartView(self, minutes):
        self.timer.restart(minutes)
        self._updateChronometerView(minutes,0)
    
    def _orderBtn(self, order):
        if order == 'init': # btn en el orden inicial
            self.start.setVisible(True)
            self.pause.setVisible(False)
            self.restart.setVisible(True)
            self.skip.setVisible(False)
        elif order == 'run': # btn cuando el contador este corriendo
            self.start.setVisible(False)
            self.pause.setVisible(True)
            self.restart.setVisible(True)
            self.skip.setVisible(False)
        elif order == 'auto': # btn inicio automatico
            self.start.setVisible(False)
            self.pause.setVisible(True)
            self.restart.setVisible(False)
            self.skip.setVisible(True)
        elif order == 'break':  # btn pause en el descanso
            self.start.setVisible(True)
            self.pause.setVisible(False)
            self.restart.setVisible(False)
            self.skip.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
