from threading import Thread
from multiprocessing import Queue

class InterruptorManager(Thread):
  
    
    def __init__(self,memory,scheduler,hdd,ioQueue):
        #AgregarProgramLoader
        self.memory = memory
        self.schPCB = scheduler
        self.io = ioQueue
        self.hdd = hdd
    
    
    #
    # SET DE INTERRUPCIONES  
    #
    
    #
    # Provenientes de Operaciones de CPU 
    #    
    def ioQueue(self,pcb): #CHIZU dijo, cambiarle los nombres
        pcb.toWaiting()
        self.io.put(pcb)
        self.schPCB.setPcbToCPU()
        
    def kill(self,pcb):
        pcb.terminated()#este seria el kill
        self.memory.clean()
        self.schPCB.setPcbToCPU()
        
    def timeOut(self,pcb):
        pcb.toReady()
        self.schPCB.add(pcb)
        self.schPCB.setPcbToCPU()
    
    
    #
    # Provenientes por I/0 
    #
    def ioEnd(self,pcb): #Esto no detiene estado del CPU, esto tampoco mantiene estado de quien dispare esta interrupcion
        pcb.toReady()
        self.schPCB.add(pcb)
    
    def new(self,program):
        pass
        #ACA iria self.programLoader.loadProcess(program)    
    
