from PCB import PCB

class ProgramLoader:



    def __init__(self, memory,hdd,processQueue):
        self.memory = memory
        self.hdd = hdd
        self.processQueue = processQueue
        self.tableIdPcb = []
        
    def loadProcess(self,program):
        self.myProgram = self.hdd.getProgram(program)
        self.direc = self.memory.getMemoryScope(self.myProgram.size())
        self.miPCB = PCB(self.getNextId(),self.direc,self.myProgram.size())
        self.processQueue.add(self.miPCB)
        self.tableIdPcb.append(self.miPCB)
        for inst in self.myProgram.getInstructions():
            self.memory.putDir(self.direc,inst)
            self.direc = self.direc + 1
    
    
    def getNextId(self):
        return len(self.tableIdPcb)    