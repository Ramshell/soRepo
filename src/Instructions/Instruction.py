from abc import abstractmethod


class Instruction:

    def __init__(self, valor):
        self.value = valor
    
    def absoluteDataPosition(self,pcb,mmu,position):
        return mmu.fromPageToAbsolutePosition(pcb.getDataPage(position))+ (position % mmu.getFrameSize())
        
    def run(self):
        pass
        
    def instructionInstance(self, memory=None, pcb=None):
        return self
    
    @abstractmethod
    def isIO(self):
        pass
