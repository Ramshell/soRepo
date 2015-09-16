from PCB import PCB

class MyClass(object):



    def __init__(self, memory,hdd,processQueue):
        self.memory = memory
        self.hdd = hdd
        self.processQueue = processQueue
        self.tableIdPcb = []
        
    def loadProcess(self,program):
        myProgram = self.hdd.getProgram(program)
        direc = self.memory.getMemoryScope(myProgram.size())
        miPCB = PCB(self.getNextId(),direc,myProgram.size())
        self.tableIdPcb.add(miPCB)
        for inst in myProgram.getInstruccions():
            self.memory.put(direc,inst)
            direc = direc + 1
    
    
    def getNextId(self):
        return len(self.tableIdPcb)    