from InterruptorManager import InterruptorManager
from threading import *
from PCB import PCB

class CPU:

    def __init__(self, memory, interruptorManager, semaphore):

        self.memory = memory
        self.interruptorManager = interruptorManager
        #Modo usuario, modo
        self.isEnabled = False #True is enabled to work, user mode only, False kernel mode
        self.pcb = PCB(0,0,0) 
        self.semaphore = semaphore

    def setPCB(self,pcb):
        self.pcb = pcb
        self.enable()


    def tick(self):
        #REGISTROS DEL CPU
        self.flagOfIoInstruction = False
        self.flagOfPCBEnding = False
    
        if(self.isEnabled):
            self.semaphore.acquire()
            self.inst = self.fetch()
            if(self.inst.isIO()):
                self.flagOfIoInstruction = True
            else:
                self.execute(self.inst)
                if(self.pcb.finished()):
                    self.flagOfPCBEnding = True
            self.semaphore.release()
            
            #VERIFICACION DE LOS REGISTROS AL FINAL
            if (self.flagOfIoInstruction):
                self.interruptorManager.ioQueue(self.pcb)
                return
            if (self.flagOfPCBEnding):
                self.interruptorManager.pcbEnd(self.pcb)
                return

    def fetch(self):
        return self.memory.getDir(self.pcb.getBaseDir() + self.pcb.getPc())

    def execute(self, instruction):
        instruction.run()
        self.pcb.incrementPc()

    def enable(self):
        self.isEnabled=True

    def disable(self):
        self.isEnabled=False
