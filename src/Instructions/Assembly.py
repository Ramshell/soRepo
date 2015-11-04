from InstCPU import InstCPU

class Mov(InstCPU):
    


    def __init__(self, relativePositionWhereToMove,relativePositionFrom):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.relativePositionFrom=relativePositionFrom
        InstCPU.__init__(self, "Mov")
     
    def setCurrentPosition(self,absolutePosition,ram):
        self.absolutePosition = absolutePosition
        self.ram = ram
        
    def run(self):
        InstCPU.run(self)
        value = self.ram.getDir(self.absolutePosition+self.relativePositionFrom)
        
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, value)
        print "escribi ",value, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove
        
class MovLiteral(InstCPU):
    
    def __init__(self, relativePositionWhereToMove,literalValue):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.literalValue=literalValue
        InstCPU.__init__(self, "MovLiteral")
    
    def setCurrentPosition(self,absolutePosition,ram):
        self.absolutePosition = absolutePosition
        self.ram = ram
    
    def run(self):
        InstCPU.run(self)
        value = self.literalValue
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, value)
        print "escribi ",value, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove
        
        
class Add(InstCPU):
    def __init__(self, relativePositionWhereToMove,relativePositionFrom):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.relativePositionFrom=relativePositionFrom
        InstCPU.__init__(self, "Add")
     
    def setCurrentPosition(self,absolutePosition,ram):
        self.absolutePosition = absolutePosition
        self.ram = ram
        
    def run(self):
        InstCPU.run(self)
        valueToSum = self.ram.getDir(self.absolutePosition+self.relativePositionFrom)
        anotherValueToSum = self.ram.getDir(self.absolutePosition+self.relativePositionWhereToMove)
        
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valueToSum+anotherValueToSum)
        print "escribi ",valueToSum+anotherValueToSum, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove

        
class AddLiteral(InstCPU):
    
    def __init__(self,relativePositionWhereToMove,literalValue):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.literalValue=literalValue
        InstCPU.__init__(self, "AddLiteral")
    
    def setCurrentPosition(self,absolutePosition,ram):
        self.absolutePosition = absolutePosition
        self.ram = ram
    
    def run(self):
        InstCPU.run(self)
        valueToSum = self.literalValue
        anotherValueToSum = self.ram.getDir(self.absolutePosition+self.relativePositionWhereToMove)
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valueToSum+anotherValueToSum)
        print "escribi ",valueToSum+anotherValueToSum, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove
        
class Jmp(InstCPU):
    def __init__(self, relativePositionWhereToMove,pcb=None):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.pcb=pcb
        InstCPU.__init__(self, "JMP")
        
    def setCurrentPosition(self,absolutePosition,pcb):
        self.absolutePosition = absolutePosition
        self.pcb = pcb
        
    def run(self):
        InstCPU.run(self)
        self.pcb.pc = self.relativePositionWhereToMove
        


class Cmp(InstCPU):
    def __init__(self, relativePositionToCompare,relativePositionToCompare2,pcb=None):
        self.relativePositionToCompare=relativePositionToCompare
        self.relativePositionToCompare2=relativePositionToCompare2
        self.pcb = pcb
        InstCPU.__init__(self, "CMP")
     
    def setCurrentPosition(self,absolutePosition,ram,pcb):
        self.absolutePosition = absolutePosition
        self.ram = ram
        self.pcb = pcb
        
    def run(self):
        InstCPU.run(self)
        valueToCompare = self.ram.getDir(self.absolutePosition+self.relativePositionToCompare)
        anotherValueToCompare = self.ram.getDir(self.absolutePosition+self.relativePositionToCompare2)
        res = valueToCompare - anotherValueToCompare
        
        if(res == 0):
            self.pcb.flagZ = True
        if(res < 0):
            self.pcb.flagS = True
            
            
class CmpLiteral(InstCPU):
    def __init__(self, relativePositionToCompare,valueLiteral,pcb=None):
        self.relativePositionToCompare=relativePositionToCompare
        self.valueLiteral=valueLiteral
        self.pcb = pcb
        InstCPU.__init__(self, "CMP")
     
    def setCurrentPosition(self,absolutePosition,ram,pcb):
        self.absolutePosition = absolutePosition
        self.ram = ram
        self.pcb=pcb
        
    def run(self):
        InstCPU.run(self)
        valueToCompare = self.ram.getDir(self.absolutePosition+self.relativePositionToCompare)
        res = valueToCompare - self.valueLiteral        
        if(res == 0):
            self.pcb.flagZ = True
        if(res < 0):
            self.pcb.flagS = True


        
class Je(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JE")
        
    def setCurrentPosition(self,absolutePosition,pcb):
        self.absolutePosition = absolutePosition
        self.pcb = pcb
        
    def run(self):
        InstCPU.run(self)
        if self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc+self.displacement

class Jne(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JE")
        
    def setCurrentPosition(self,absolutePosition,pcb):
        self.absolutePosition = absolutePosition
        self.pcb = pcb
        
    def run(self):
        InstCPU.run(self)
        if not self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc+self.displacement
            
class Jl(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JE")
        
    def setCurrentPosition(self,absolutePosition,pcb):
        self.absolutePosition = absolutePosition
        self.pcb = pcb
        
    def run(self):
        InstCPU.run(self)
        if self.pcb.getFlagS():
            self.pcb.pc = self.pcb.pc+self.displacement
            
class Jnl(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JE")
        
    def setCurrentPosition(self,absolutePosition,pcb):
        self.absolutePosition = absolutePosition
        self.pcb = pcb
        
    def run(self):
        InstCPU.run(self)
        if not self.pcb.getFlagS():
            self.pcb.pc = self.pcb.pc+self.displacement
    