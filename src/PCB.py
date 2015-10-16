from ReadyPCB import *
from RuningPCB import *
from WaitingPCB import *

class PCB:

    #este lo crea el loader
    def __init__(self, idP, base, size, priority):
        self.pc = 0
        self.pid = idP
        self.baseDir = base
        self.size = size
        self.state = ReadyPCB()
        #esto lo cambia scheduler
        self.rafaga = -1
        self.priority = priority
    #
    # Metodos comunes!!!! 
    #
    def incrementPc(self):
        self.state.incrementarPC(self)

        
    def getBaseDir(self):
        return self.baseDir

    def getPc(self):
        return self.pc

    def getSize(self):
        return self.size

    def finished(self):
        return self.pc >= self.size
    
    
    def getPid(self):
        return self.pid
    
    def getState(self):
        return self.state.name()
    
    #
    # Cambios de state 
    #
    def toReady(self):
        self.state = ReadyPCB()
        
    def toWaiting(self):
        self.state = WaitingPCB()
                
    def runing(self):
        self.state = RuningPCB()
    
    #asignacion de rafaga
    def assignRafaga(self, countRafagaPerPCB):
        self.rafaga = countRafagaPerPCB
        
    def rafagaIsOver(self):
        return self.rafaga == 0
    
    #prioridades
    
    def getPriority(self):
        return self.priority
    
    def desincrementPriority(self):
        if(self.priority > 0):
            self.priority = self.priority - 1
        

        