from ReadyPCB import *
from RuningPCB import *
from WaitingPCB import *

class PCB:


    def __init__(self, idP, base, size):
        self.pc = 0
        self.pid = idP
        self.baseDir = base
        self.size = size
        self.estado = ReadyPCB()
    
    #
    # Metodos comunes!!!! 
    #
    def incrementPc(self):
        self.estado.incrementarPC(self)

        
    def getBaseDir(self):
        return self.baseDir

    def getPc(self):
        return self.pc

    def getSize(self):
        return self.size

    def finished(self):
        return self.pc > self.size
    
    
    
    #
    # Cambios de estado 
    #
    def toReady(self):
        self.estado = ReadyPCB()
        
    def toWaiting(self):
        self.estado = WaitingPCB()
                
    def runing(self):
        self.estado = RuningPCB()
    
    
    
    
