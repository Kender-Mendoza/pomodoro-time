from threading import Timer

class Chronometer():
    def __init__(self, minute, labelMin, labelSec):
        self.minute = minute
        self.second = 0
        self.labelMin = labelMin
        self.labelSec = labelSec
        self.timer = 0

        # Initializing the chronometer of interface
        self.labelMin.setText(("0"+ str(minute)) if minute < 10 else str(minute))
        self.labelSec.setText("00")

        # Number of seconds
        self.SECONDS = 59
            
    def start(self, minute, second):
        if minute >= 0: 
            def updateView():
                if second > 0:
                    self.start(minute, second - 1)
                    self.minute = minute
                    self.second = second             
                    self.labelSec.setText(("0"+ str(second)) if second < 10 else str(second))
                    self.labelMin.setText(("0"+ str(minute)) if minute < 10 else str(minute))
                    #print(("0"+ str(minute)) if minute < 10 else str(minute), ("0"+ str(second)) if second < 10 else str(second))

                else:
                    self.start(minute - 1, self.SECONDS)
                    self.minute = minute
                    self.second = second         
                    self.labelMin.setText(("0"+ str(minute)) if minute < 10 else str(minute))
                    self.labelSec.setText(("0"+ str(second)) if second < 10 else str(second))
                    #print(("0"+ str(minute)) if minute < 10 else str(minute), ("0"+ str(second)) if second < 10 else str(second))

            self.timer = Timer(1, updateView)
            self.timer.start()
        else:
            self.timer.cancel()
            return 1 # this is for indicate that one pomodoro is finishing

    def pause(self):
        self.timer.cancel()
        #print(self.minute, self.second)
    
    def init(self):
        if self.second == -1 : 
            self.second = 0
        elif self.second == 0 : 
            self.second = self.SECONDS
            self.minute = self.minute - 1
        else : 
            self.second = self.second - 1

        self.start(self.minute, self.second)
            

