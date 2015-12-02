from Instructions.Assembly import MovLiteral
from util.FileLogger import FileLogger


class Program:
    """
    @summary: Object that represents a program to be executed
    
    @author: Nicolas Leutwyler
    @author: Lucas Sandoval
    @author: Jesus Laime
    """
    
    def __init__ (self, name, manual=None, variableSize=0):
        """
        Constructor of the program
        
        @param name: Name of the program
        @param manual: Manual of use for the program 
        @param variableSize: Size of the variables that the program use  
        """
        self.instructions = []
        self.name = name
        self.manual = manual
        self.variableSize = variableSize
        self.logger = FileLogger("../log/progLoader_log")

    def initializePreValues(self, args):
        """
        Sets arguments that the program need for execution
        
        @param args: Arguments for the program 
        """
        index = 0
        for arg in args:
            self.logger.log("Setting value " +arg+ " at position:")
            self.instructions.insert(index, MovLiteral(index, int(arg)))
            index = index + 1
        self.variableSize = self.variableSize + index
        
    def size(self):
        """
        @return: How many instructions the program has
        """
        return len(self.instructions)
    
    def addInstruction(self, instruction):
        """
        Insert a new instruction to the program
        
        @param instruction: Instruction to be inserted 
        """
        self.instructions.append(instruction)
        
    def addManual(self, manual):
        self.manual = manual
        
    def getManual(self):
        return self.manual
    
    def getInstructions(self):
        return self.instructions
    
    def getName(self):
        return self.name
    
