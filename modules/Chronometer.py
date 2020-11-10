from threading import Timer

class Chronometer():
    def __init__(self, minute, labelMin, labelSec):
        self.minute = minute
        self.second = 0
        self.labelMin = labelMin
        self.labelSec = labelSec
        self.timer = 0
        self.labelMin.setText(("0"+ str(minute)) if minute < 10 else str(minute))
        self.labelSec.setText("00")

        self.start(self.minute, self.second)
            
    def start(self, minute, second):
        if second >= 0:
            def updateView():
                self.second = second             
                self.labelSec.setText(("0"+ str(second)) if second < 10 else str(second))
                self.start(minute, second - 1)

            self.timer = Timer(1, updateView)
            self.timer.start()
        elif minute >= 0:
            self.minute = minute
            self.labelMin.setText(("0"+ str(minute)) if minute < 10 else str(minute))
            self.start(minute - 1, 59)
        else:
            return 1 # this is for indicate that one pomodoro is finishing

    def pause(self):
        self.timer.cancel()
        print("info", self.minute, self.second)
            