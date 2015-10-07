from InterruptorManager import InterruptorManager
from threading import *

class CPU:

    def __init__(self, memory, interruptorManager, semaphore):

        self.memory = memory
        self.interruptorManager = interruptorManager
        self.flag = False
        self.semaphore = semaphore

    def setPCB(self,pcb):
        self.pcb = pcb
        self.flag = True

    def tick(self):

        if(self.flag):
            self.semaphore.acquire()
            inst = self.fetch()
            if(inst.isIO()):
                self.interruptorManager.ioQueue(self.pcb)
                return

            self.execute(inst)
            if(self.pcb.finished()):
                self.interruptorManager.pcbEnd(self.pcb)
            self.semaphore.release()


    def fetch(self):
        return self.memory.getDir(self.pcb.getBaseDir() + self.pcb.getPc())

    def execute(self, instruction):
        instruction.run()
        self.pcb.incrementPc()
