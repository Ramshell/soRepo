from programs.ReadyPCB import *
from programs.RuningPCB import *
from programs.WaitingPCB import *


class PCB:

    #este lo crea el loader
    def __init__(self, idP, pages, size, priority=0, frameSize=1,dataScope=[]):
        self.pc = 0
        self.pid = idP
        self.pages = pages
        self.size = size
        self.state = ReadyPCB()
        
        # The scheduler change this value
        self.burst = -1
        self.priority = priority
        self.frameSize = frameSize
        self.dataScope= dataScope
        self.flagZ=False
        self.flagS=False

    def incrementPc(self):
        self.state.incrementarPC(self)
        
    def getCurrentPage(self):
        return self.pages[self.pc / self.frameSize]
    
    def getDataPage(self,relativePosition):
        return self.dataScope[relativePosition / self.frameSize]
        
    def getFlagZ(self):
        return self.flagZ
    
    def getFlagS(self):
        return self.flagS
        
    def getPages(self):
        return self.pages

    def getPc(self):
        return self.pc

    def getSize(self):
        return self.size
    
    def getBurst(self):
        return self.burst

    def finished(self):
        return self.pc >= self.size
    
    def getPid(self):
        return self.pid
    
    def getState(self):
        return self.state.name()
    
    def toReady(self):
        self.state = ReadyPCB()
        
    def toWaiting(self):
        self.state = WaitingPCB()
                
    def runing(self):
        self.state = RuningPCB()

    def assignBurst(self, burst):
        self.burst = burst
        
    def rafagaIsOver(self):
        return self.burst == 0
    
    def getPriority(self):
        return self.priority
    
    def decrementPriority(self):
        if(self.priority > 0):
            self.priority = (self.priority - 1)
            
    def decrementQuantum(self):
        self.burst = self.burst - 1
        

        
