from PCB import PCB
from TableOfPcb import TableOfPCB

class ProgramLoader:



    def __init__(self, memory,hdd,processQueue,mmu):
        self.memory = memory
        self.mmu = mmu
        self.hdd = hdd
        self.pids = 0
        self.processQueue = processQueue
        self.pcbTable = TableOfPCB()
        
    def manual(self,programName):
        print self.hdd.getProgram(programName).getManual()
        return self.hdd.getProgram(programName).getManual()
        
    def loadProcessWithNoPriority(self,program,args=[]):
        return self.loadProcessWithPriority(program,0,args)

    
    def loadProcessWithPriority(self,program, priority,args=[]):
        self.myProgram = self.hdd.getProgram(program)
        self.myProgram.initializePreValues(args)
        self.pages = self.mmu.getMemoryScope(self.myProgram)
        self.miPCB = PCB(self.getNextId(),self.pages,self.myProgram.size(), priority,self.mmu.getFrameSize())
        self.instructions = self.myProgram.getInstructions()
        current = 0
        for i in self.pages:
            for j in xrange(self.mmu.getFrameSize()):
                self.memory.putDir(self.mmu.fromPageToAbsolutePosition(i) + j, self.instructions[current].instructionInstance(self.memory,self.miPCB))
                current = current+1
        self.miPCB.toReady()
        self.processQueue.put(self.miPCB)
        self.pcbTable.addPCB(self.miPCB)
        return self.pids
    
    def getPcbTable(self):
        return self.pcbTable
    
    
    def getNextId(self):
        self.pids = self.pids +1
        return self.pids
