from programs.PCB import PCB
from programs.TableOfPcb import TableOfPCB


class ProgramLoader:



    def __init__(self, memory,hdd,processQueue,mmu):
        """
        Constructor it requires a memory, a hard disk, a process queue and a memory management unity
        """
        
        self.memory = memory
        self.mmu = mmu
        self.hdd = hdd
        self.pids = 0
        self.processQueue = processQueue
        self.pcbTable = TableOfPCB()
        
    def manual(self, programName):
        """
        @param programName: the name of a program
        @return the manual of a program called programName
        """
        return self.hdd.getProgram(programName)
        
    def in_disk(self, program_name):
        """
        @param program_name: the program's name to looking for
        @return it tells if a program_name is in disk
        """
        return program_name in self.hdd.programs
        
    def loadProcess(self, program, priority=0,args=[]):
        """
        @note: this method load a program into the ram
        
        @param program: the next program to load
               priority: the priority of the program
               args: the program will be loaded with this args
        @return: the program id
        """
        
        self.myProgram = self.hdd.getProgram(program)
        self.myProgram.initializePreValues(args)
        self.scope = self.mmu.getMemoryScope(self.myProgram)
        self.pages = self.scope.getListInstructionPages()
        self.dataScope = self.scope.getListDataPages()
        self.miPCB = PCB(self.getNextId(),self.pages,self.myProgram.size(), priority,self.mmu.getFrameSize(),self.dataScope)
        self.instructions = self.myProgram.getInstructions()
        current = 0
        for slipping in xrange(self.mmu.getFrameSize()):
            if current >= len(self.instructions): break
            self.memory.putDir(self.mmu.fromPageToAbsolutePosition(self.pages[0].getPageNumber()) + slipping, self.instructions[current])
            current = current+1
        self.pages[0].changeMemoryFlag()
        self.miPCB.toReady()
        self.processQueue.put(self.miPCB)
        self.pcbTable.addPCB(self.miPCB,self.myProgram.getName())
        return self.pids
    
    
    
    def getPcbTable(self):
        return self.pcbTable
    
    
    def getNextId(self):
        self.pids = self.pids + 1
        return self.pids
    
    def storeNeededPage(self,pcb):
        '''
        @invariant: the pcb's pc is in the beginning of a page not in memory RAM.
        '''
        currentValue = pcb.getCurrentLogicPage() * self.mmu.getFrameSize()
        programName = self.pcbTable.getProgramName(pcb.getPid())
        instructions = self.hdd.getProgram(programName).getInstructions()
        for slipping in xrange(self.mmu.getFrameSize()):
            if currentValue >= len(instructions): break
            self.memory.putDir(self.mmu.fromPageToAbsolutePosition(pcb.getCurrentPage().getPageNumber()) + slipping, instructions[currentValue])
            currentValue = currentValue + 1
        pcb.getCurrentPage().changeMemoryFlag()
