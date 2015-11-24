from threading import Thread
import time

from CPU import CPU


class Clock(Thread):

    def __init__(self, cpu):
        Thread.__init__(self)
        self.cpu = cpu


    def run(self):
        while(True):
            self.cpu.tick()
            time.sleep(0.5)
