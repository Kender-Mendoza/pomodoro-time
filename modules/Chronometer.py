from threading import Timer

class Chronometer():
    def __init__(self, minute, labelMin, labelSec):
        self.minute = minute
        self.second = 0
        self.timer = 0
        self.count = 0

        self.labelMin = labelMin
        self.labelSec = labelSec
        
        # Initializing the chronometer of interface
        self._initView()

        # Number of seconds
        self.SECONDS = 2
        self.MINUTES = minute
            
    def _start(self, minute, second, callback):
        if minute >= 0: 
            def updateView():
                if second > 0:
                    self._start(minute, second - 1, callback)
                    self.minute = minute
                    self.second = second  

                    self.labelSec.setText(("0"+ str(second)) if second < 10 else str(second))
                    self.labelMin.setText(("0"+ str(minute)) if minute < 10 else str(minute))
                    print(("0"+ str(minute)) if minute < 10 else str(minute), ("0"+ str(second)) if second < 10 else str(second))

                else:
                    self._start(minute - 1, self.SECONDS, callback)
                    self.minute = minute
                    self.second = second         
                    
                    self.labelMin.setText(("0"+ str(minute)) if minute < 10 else str(minute))
                    self.labelSec.setText(("0"+ str(second)) if second < 10 else str(second))
                    print(("0"+ str(minute)) if minute < 10 else str(minute), ("0"+ str(second)) if second < 10 else str(second))

            self.timer = Timer(1, updateView)
            self.timer.start()
        else:
            self.timer.cancel()
            self.count += 1
            print(self.count) 
            callback(self.count)
            return

    def _initView(self):
        self.labelMin.setText(("0"+ str(self.minute)) if self.minute < 10 else str(self.minute))
        self.labelSec.setText(("0"+ str(self.second)) if self.second < 10 else str(self.second))

    def init(self, callback):
        if self.second == -1 : 
            self.second = 0
        elif self.second == 0 : 
            self.second = self.SECONDS
            self.minute = self.minute - 1
        else : 
            self.second = self.second - 1

        self._start(self.minute, self.second, callback)

    def pause(self):
        self.timer.cancel()
        #print(self.minute, self.second)

    def restart(self):
        self.pause() # para el timer actual.
        self.second = 0 
        self.minute = self.MINUTES 
        # Reinitialize the chronometer's view
        self._initView()   