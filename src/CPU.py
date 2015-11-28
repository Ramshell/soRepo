from threading import *

from InterruptorManager import InterruptorManager
from PCB import PCB
from util.FileLogger import FileLogger


class CPU:

    def __init__(self, memory, interruptorManager, semaphore,mmu):

        self.memory = memory
        self.interruptorManager = interruptorManager
        # Modo usuario, modo
        self.isEnabled = False  # True is enabled to work, user mode only, False kernel mode
        self.pcb = None
        self.semaphore = semaphore
        self.mmu = mmu
        
        self.logger = FileLogger("../log/cpu_log")
        

    def setPCB(self, pcb):
        self.pcb = pcb
        self.enable()


    def tick(self):
        # REGISTROS DEL CPU
        self.flagOfIoInstruction = False
        self.flagOfPCBEnding = False
        self.flagOfRafagaOfPCB = False
        
        if self.pcb is None:
            self.interruptorManager.idleCPU()
        
        if(self.isEnabled):
            if(self.pcb.finished()):  # PREGUNTAR ANTES DE EJECUTAR
                self.flagOfPCBEnding = True
            else:
                self.semaphore.acquire()
                self.inst = self.fetch()
                if(self.inst.isIO()):
                    self.flagOfIoInstruction = True
                    self.inst.setValue(self.pcb,self.memory,self.mmu)
                    self.package = [self.pcb, self.inst]
                    self.codDevice = self.inst.deviceCod()
                else:
                    self.execute(self.inst)
                    if(self.pcb.rafagaIsOver()):
                        self.flagOfRafagaOfPCB = True
                            
                self.semaphore.release()
            
            # VERIFICACION DE LOS REGISTROS AL FINAL
            if (self.flagOfIoInstruction):
                self.logger.log("I/O Signal")
                self.disable()
                self.interruptorManager.ioQueue(self.package, self.codDevice)
                return
            if (self.flagOfPCBEnding):
                self.logger.log("Kill Signal")
                self.interruptorManager.kill(self.pcb.getPid())
                return
            if(self.flagOfRafagaOfPCB):
                self.logger.log("TimeOut Signal")
                self.interruptorManager.timeOut(self.pcb)
                return
            
    def fetch(self):
        self.logger.log("Fetching instruction "+ str(self.mmu.fromPageToAbsolutePosition(self.pcb.getCurrentPage()) + self.pcb.getPc() % self.mmu.getFrameSize()))
        self.inst = self.memory.getDir(self.mmu.fromPageToAbsolutePosition(self.pcb.getCurrentPage()) + self.pcb.getPc() % self.mmu.getFrameSize())
        self.pcb.incrementPc()
        self.pcb.decrementQuantum()
        return self.inst  # ANTE CADA FETCH SE INCREMENTA EL PC DEL PCB

    def execute(self, instruction):
        instruction.run(self.pcb, self.memory,self.mmu)
        self.pcb.decrementPriority()

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False
