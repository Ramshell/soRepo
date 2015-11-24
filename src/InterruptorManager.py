from multiprocessing import Queue
from threading import Thread


class InterruptorManager(Thread):
         

    def __init__(self,mmu=None,scheduler=None,hdd=None,ioDelivery=None,semaphore=None,pcbTable=None):
        self.mmu = mmu
        self.schPCB = scheduler
        self.io = ioDelivery
        self.hdd = hdd
        self.semaphore = semaphore
        self.pcbTable = pcbTable
    
    
    #
    # SET DE INTERRUPCIONES  
    #
    
    #
    # Provenientes de Operaciones de CPU 
    #    
    def ioQueue(self, data, cod):
        data[0].toWaiting()
        self.io.putInQueue(data, cod)
        self.schPCB.setPcbToCPU()
         
    def kill(self, pid):
        self.pcb = self.pcbTable.getPCB(pid)
        self.pcbTable.delete(self.pcb)
        self.mmu.clean(self.pcb)
        self.schPCB.setPcbToCPU()
        
    def timeOut(self, pcb):
        pcb.toReady()
        self.schPCB.put(pcb)
        self.schPCB.setPcbToCPU()
    
    
    #
    # Provenientes por I/0 
    #
    def ioDone(self, pcb):  # Esto no detiene estado del CPU, esto tampoco mantiene estado de quien dispare esta interrupcion
        pcb.toReady()
        self.schPCB.put(pcb)
    
    def idleCPU(self):
        self.schPCB.setPcbToCPU()
    
    def setMmu(self, mmu):
        self.mmu = mmu
    
    def setScheduler(self, scheduler):
        self.schPCB = scheduler
        
    def setDisk(self, disk):
        self.hdd = disk
        
    def setIODelivery(self, iodelivery):
        self.io = iodelivery
        
    def setSemaphore(self, semaphore):
        self.semaphore = semaphore
        
    def setPcbTable(self, pcbTable):
        self.pcbTable = pcbTable
