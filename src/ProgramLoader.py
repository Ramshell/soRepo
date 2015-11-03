from PCB import PCB
from TableOfPcb import TableOfPCB

class ProgramLoader:



    def __init__(self, memory,hdd,processQueue):
        self.memory = memory
        self.hdd = hdd
        self.pids = 0
        self.processQueue = processQueue
        self.pcbTable = TableOfPCB()
        
    def manual(self,programName):
        print self.hdd.getProgram(programName).getManual()
        return self.hdd.getProgram(programName).getManual()
        
    def loadProcessWithNoPriority(self,program):
        return self.loadProcessWithPriority(program,0)

    
    def loadProcessWithPriority(self,program, priority):
        self.myProgram = self.hdd.getProgram(program)
        self.direc = self.memory.getMemoryScope(self.myProgram.size())
        self.miPCB = PCB(self.getNextId(),self.direc,self.myProgram.size(), priority)
        self.miPCB.toReady()
        self.processQueue.put(self.miPCB)
        self.pcbTable.addPCB(self.miPCB)
        for inst in self.myProgram.getInstructions():
            self.memory.putDir(self.direc,inst)
            self.direc = self.direc + 1
        return self.pids
    
    def getPcbTable(self):
        return self.pcbTable
    
    
    def getNextId(self):
        self.pids = self.pids +1
        return self.pids
