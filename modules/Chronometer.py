from threading import Timer
from time import sleep

class Chronometer():
    def __init__(self, minutes):
        self.SECOND = 0

        self.min = minutes
        self.sec = 0

        self.flag = False

    def start(self, callback):
        self.flag = False

        minutes = self.min
        seconds = self.sec
        
        while minutes >= 0:
            while seconds >= 0:
                
                if self.flag: return 0

                self.min = minutes
                self.sec = seconds                

                callback(minutes, seconds)
                sleep(1)

                seconds -= 1

            minutes -= 1
            seconds = self.SECOND

        return 1

    def pause(self):
        self.flag = True
        print(self.min,self.sec)

    def restart(self, minutes):
        self.flag = True
        self.min = minutes
        self.sec = 0
