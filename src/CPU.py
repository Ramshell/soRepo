from InterruptorManager import InterruptorManager
from threading import *

class CPU:

    def __init__(self, memory, interruptorManager, semaphore):

        self.memory = memory
        self.interruptorManager = interruptorManager

        #Modo usuario, modo
        self.isEnabled = False #True is enabled to work, user mode only, False kernel mode

        self.semaphore = semaphore

    def setPCB(self,pcb):
        self.pcb = pcb
        self.enable

    def tick(self):
        if(self.isEnabled):
            self.semaphore.acquire()
            inst = self.fetch()
            if(inst.isIO()):
                self.interruptorManager.ioQueue(self.pcb)
                #FLagg en false
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

    def enable(self):
        self.isEnabled=True

    def disable(self):
        self.isEnabled=False
