
class Program:
    
    def __init__ (self,name,manual=None):
        self.instructions = []
        self.name = name
        self.manual = manual

        
        
    def size(self):
        return len(self.instructions)
    
    def getInstructions(self):
        return self.instructions
    
    def addManual(self,manual):
        self.manual = manual
        
    def getManual(self):
        return self.manual
    
    def addInstruction(self, instruction):
        self.instructions.append(instruction)
    
    