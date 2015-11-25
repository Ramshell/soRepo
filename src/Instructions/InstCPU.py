from Instruction import Instruction
from util.FileLogger import FileLogger


class InstCPU(Instruction):
    
    def __init__(self, name):
        Instruction.__init__(self, name)
        #self.logger = FileLogger("../../log/cpu_log")
    
    def isIO(self):
        return False
    
    
    
    def absoluteInstructionPosition(self,pcb,mmu,position):
        return mmu.fromPageToAbsolutePosition(pcb.getCurrentPage(position))+ (position % mmu.getFrameSize())
    
    def run(self,pcb, mmu,memory):
        #self.logger.log(self.value) 
        print self.value  
