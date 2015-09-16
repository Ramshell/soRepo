
class Program:
    

    def __init__(self, instructions):
        self.instructions = instructions
        
        
    def size(self):
        return len(self.instructions)
    
    def getInstructions(self):
        return self.instructions
    
    def addInstruction(self, instruction):
        self.instructions.add(instruction)
    
    
        
