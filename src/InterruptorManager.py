from threading import Thread
from multiprocessing import Queue

class InterruptorManager(Thread):
         
    def __init__(self,memory=None,scheduler=None,hdd=None,ioDelivery=None): #ioDelivery
        #AgregarProgramLoader
        self.memory = memory
        self.schPCB = scheduler
        self.io = ioDelivery
        self.hdd = hdd
    
    
    #
    # SET DE INTERRUPCIONES  
    #
    
    #
    # Provenientes de Operaciones de CPU 
    #    
    def ioQueue(self,data,cod): #CHIZU dijo, cambiarle los nombres
        #packageData <-- es una tupla /pcb,instr/ , codDevice
        data[0].toWaiting()
        self.io.putInQueue(data,cod)
        self.schPCB.setPcbToCPU()
         
    def kill(self,pcb):
        self.memory.clean(pcb)
        self.schPCB.setPcbToCPU()
        
    def timeOut(self,pcb):
        pcb.toReady()
        self.schPCB.add(pcb)
        self.schPCB.setPcbToCPU()
    
    
    #
    # Provenientes por I/0 
    #
    def ioDone(self,pcb): #Esto no detiene estado del CPU, esto tampoco mantiene estado de quien dispare esta interrupcion
        pcb.toReady()
        self.schPCB.add(pcb)
    
    def new(self,program):
        pass
        #ACA iria self.programLoader.loadProcess(program)    
    
    def setMemory(self, memory):
        self.memory = memory
    
    def setScheduler(self, scheduler):
        self.schPCB = scheduler
        
    def setDisk(self, disk):
        self.hdd = disk
        
    def setIODelivery(self, iodelivery):
        self.io = iodelivery