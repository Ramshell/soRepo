from threading import Thread
from CPU import CPU
import time

class Clock(Thread):

    def __init__(self,cpu):
        Thread.__init__(self)
        self.cpu = cpu


    def run(self):
        while(True):
            self.cpu.tick()
            time.sleep(1)
            print("espere 1 segundo")
