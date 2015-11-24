from PCB import PCB
from TableOfPcb import TableOfPCB


class ProgramLoader:



    def __init__(self, memory, hdd, processQueue):
        self.memory = memory
        self.hdd = hdd
        self.pids = 0
        self.processQueue = processQueue
        self.pcbTable = TableOfPCB()
        
    def manual(self, programName):
        return self.hdd.getProgram(programName)
        
    def in_disk(self, program_name):
        return program_name in self.hdd.programs
        
    def loadProcessWithNoPriority(self, program, args=[]):
        return self.loadProcessWithPriority(program, 0, args)

    
    def loadProcessWithPriority(self, program, priority, args=[]):
        self.myProgram = self.hdd.getProgram(program)
        self.myProgram.initializePreValues(args)
        self.direc = self.memory.getMemoryScope(self.myProgram.size())
        self.miPCB = PCB(self.getNextId(), self.direc, self.myProgram.size(), priority)
        for inst in self.myProgram.getInstructions():
            self.memory.putDir(self.direc, inst.instructionInstance(self.memory, self.miPCB))
            self.direc = self.direc + 1
        self.memory.reserve(self.myProgram.variableSize)
        self.miPCB.toReady()
        self.processQueue.put(self.miPCB)
        self.pcbTable.addPCB(self.miPCB)
        return self.pids
    
    def getPcbTable(self):
        return self.pcbTable
    
    
    def getNextId(self):
        self.pids = self.pids + 1
        return self.pids
