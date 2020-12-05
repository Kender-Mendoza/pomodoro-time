from threading import Timer
from time import sleep

class Chronometer():
    def __init__(self, minutes):
        self.MINUTES = minutes
        self.SECOND = 59

        self.min = 0
        self.sec = 0


    def start(self, callback):
        minutes = self.MINUTES
        seconds = 0
        
        print(minutes,seconds)
        while minutes >= 0:
            while seconds >= 0:
                callback(minutes, seconds)
                sleep(1)

                seconds -= 1

            minutes -= 1
            seconds = self.SECOND

        return 1
