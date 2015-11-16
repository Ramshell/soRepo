from Instruction import Instruction
from util.FileLogger import FileLogger

class InstCPU(Instruction):
    
    def __init__(self,name):
        Instruction.__init__(self, name)
        self.logger = FileLogger("../../log/cpu_log")
    
    def isIO(self):
        return False
    
    def run(self):
        pass