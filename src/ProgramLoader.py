from PCB import PCB
from TableOfPcb import TableOfPCB

class ProgramLoader:



    def __init__(self, memory,hdd,processQueue):
        self.memory = memory
        self.hdd = hdd
        self.pids = 0
        self.processQueue = processQueue
        self.pcbTable = TableOfPCB()
        
    def loadProcessWithNoPriority(self,program):
        self.loadProcessWithPriority(program,0)
    
    def loadProcessWithPriority(self,program, priority):
        self.myProgram = self.hdd.getProgram(program)
        self.direc = self.memory.getMemoryScope(self.myProgram.size())
        self.miPCB = PCB(self.getNextId(),self.direc,self.myProgram.size(), priority)
        self.miPCB.toReady() #POSIBLEMENTE CAMBIE, medio al pedo el estado new en PCB
        self.processQueue.put(self.miPCB)
        self.pcbTable.addPCB(self.miPCB)
        for inst in self.myProgram.getInstructions():
            self.memory.putDir(self.direc,inst)
            self.direc = self.direc + 1
    
    def getPcbTable(self):
        return self.pcbTable
    
    
    def getNextId(self):
        return self.pids +1  
