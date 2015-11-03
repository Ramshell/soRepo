from InstCPU import InstCPU

class Mov(InstCPU):
    


    def __init__(self, name,relativePositionWhereToMove,relativePositionFrom):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.relativePositionFrom=relativePositionFrom
        InstCPU.__init__(self, name)
     
    def setCurrentPosition(self,absolutePosition,ram):
        self.absolutePosition = absolutePosition
        self.ram = ram
        
    def run(self):
        valor = self.ram.getDir(self.absolutePosition+self.relativePositionFrom)
        
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valor)
        print "escribi ",valor, " en ", self.absolutePosition+self.relativePositionWhereToMove
        
class MovLiteral(InstCPU):
    
    def __init__(self, name,relativePositionWhereToMove,literalValue):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.literalValue=literalValue
        InstCPU.__init__(self, name)
    
    def setCurrentPosition(self,absolutePosition,ram):
        self.absolutePosition = absolutePosition
        self.ram = ram
    
    def run(self):
        valor = self.literalValue
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valor)
        print "escribi ",valor, " en ", self.absolutePosition+self.relativePositionWhereToMove