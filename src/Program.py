from Instructions.Assembly import MovLiteral
from util.FileLogger import FileLogger


class Program:
    
    def __init__ (self,name,manual=None,variableSize=0):
        self.instructions = []
        self.name = name
        self.manual = manual
        self.variableSize = variableSize
        self.logger = FileLogger("../../log/progLoader_log")

    def initializePreValues(self,args):
        index = 0
        for arg in args:
            print "Setting value ", arg, " at position:", 0
            #self.logger.log("Seteando valor "+str(arg)+" en posicion 0")
            self.instructions.insert(index, MovLiteral(index,int(arg)))
            index = index +1
        
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
    
    