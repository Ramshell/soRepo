from Instruction import Instruction
from util.FileLogger import FileLogger


class InstCPU(Instruction):
    
    """
    Constructor for Class InstCPU
    Also creates him a logger.
    
    """
    def __init__(self, name):
        Instruction.__init__(self, name)
        #self.logger = FileLogger("../log/cpu_log")
    
    """
    Return True if the instruction is of I/O, False otherwise
    
    @return: False, this instructions are not for I/O
    """
    def isIO(self):
        return False
    
    
    """
    
    """
    def absoluteInstructionPosition(self,pcb,mmu,position):
        return mmu.fromPageToAbsolutePosition(pcb.getCurrentPage(position))+ (position % mmu.getFrameSize())
    
    """
    Executes the instruction
    
    """
    def run(self,pcb,memory,mmu):
        pass
