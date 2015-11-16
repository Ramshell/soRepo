from InstCPU import InstCPU

class Mov(InstCPU):
    
    '''
    @note: the goal of this instruction is replace the value allocated in a direction
           of the ram with another value allocated in the ram.   
    '''

    def __init__(self, relativePositionWhereToMove,relativePositionFrom):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.relativePositionFrom=relativePositionFrom
        InstCPU.__init__(self, "Mov")
     
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Mov(self.relativePositionWhereToMove,self.relativePositionFrom)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        value = self.ram.getDir(self.absolutePosition+self.relativePositionFrom)
        
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, value)
        print "escribi ",value, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove
        
class MovLiteral(InstCPU):
    

    '''
    @note: the goal of this instruction is replace the value allocated in a direction of the ram
           with another value  
    '''
    
    def __init__(self, relativePositionWhereToMove,literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue=literalValue
        InstCPU.__init__(self, "MovLiteral")
    
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self,memory,pcb):
        insToReturn = MovLiteral(self.relativePositionWhereToMove,self.literalValue)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
    
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
     
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Add(self.relativePositionWhereToMove,self.relativePositionFrom)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        valueToSum = self.ram.getDir(self.absolutePosition+self.relativePositionFrom)
        anotherValueToSum = self.ram.getDir(self.absolutePosition+self.relativePositionWhereToMove)
        
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valueToSum+anotherValueToSum)
        print "escribi ",valueToSum+anotherValueToSum, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove
        

class Mul(InstCPU):
    def __init__(self, relativePositionWhereToMove,relativePositionFrom):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.relativePositionFrom=relativePositionFrom
        InstCPU.__init__(self, "MUL")
     
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Mul(self.relativePositionWhereToMove,self.relativePositionFrom)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        valueToMul = self.ram.getDir(self.absolutePosition+self.relativePositionFrom)
        anotherValueToMul = self.ram.getDir(self.absolutePosition+self.relativePositionWhereToMove)
        
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valueToMul*anotherValueToMul)
        print "escribi ",valueToMul*anotherValueToMul, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove

        
class AddLiteral(InstCPU):
    
    def __init__(self,relativePositionWhereToMove,literalValue):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.literalValue=literalValue
        InstCPU.__init__(self, "AddLiteral")
    
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self,memory,pcb):
        insToReturn = AddLiteral(self.relativePositionWhereToMove,self.literalValue)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
    
    def run(self):
        InstCPU.run(self)
        valueToSum = self.literalValue
        anotherValueToSum = self.ram.getDir(self.absolutePosition+self.relativePositionWhereToMove)
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valueToSum+anotherValueToSum)
        print "escribi ",valueToSum+anotherValueToSum, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove
        

class MulLiteral(InstCPU):
    
    def __init__(self,relativePositionWhereToMove,literalValue):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.literalValue=literalValue
        InstCPU.__init__(self, "MulLiteral")
    
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self,memory,pcb):
        insToReturn = MulLiteral(self.relativePositionWhereToMove,self.literalValue)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
    
    def run(self):
        InstCPU.run(self)
        valueToMul = self.literalValue
        anotherValueToMul = self.ram.getDir(self.absolutePosition+self.relativePositionWhereToMove)
        self.ram.putDir(self.absolutePosition+self.relativePositionWhereToMove, valueToMul*anotherValueToMul)
        print "escribi ",valueToMul*anotherValueToMul, " en la posicion", self.absolutePosition+self.relativePositionWhereToMove

        
class Jmp(InstCPU):
    def __init__(self, relativePositionWhereToMove,pcb=None):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        self.pcb=pcb
        InstCPU.__init__(self, "JMP")
        
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Jmp(self.relativePositionWhereToMove)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        self.pcb.pc = self.relativePositionWhereToMove
        


class Cmp(InstCPU):
    def __init__(self, relativePositionToCompare,relativePositionToCompare2):
        self.relativePositionToCompare=relativePositionToCompare
        self.relativePositionToCompare2=relativePositionToCompare2
        InstCPU.__init__(self, "CMP")
     
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Cmp(self.relativePositionToCompare,self.relativePositionToCompare2)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
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
     
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = CmpLiteral(self.relativePositionToCompare,self.valueLiteral)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
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
        
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Je(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        if self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc+self.displacement

class Jne(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JE")
        
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Jne(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        if not self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc+self.displacement
            
class Jl(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JL")
        
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Jl(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        if self.pcb.getFlagS():
            self.pcb.pc = self.pcb.pc+self.displacement
            
            
class Jle(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JLE")
        
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Jle(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        if self.pcb.getFlagS() or self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc+self.displacement
            
class Jnl(InstCPU):
    def __init__(self, displacement,pcb=None):
        self.displacement=displacement
        self.pcb=pcb
        InstCPU.__init__(self, "JNL")
        
    def setCurrentPosition(self,pcb,memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self,memory,pcb):
        insToReturn = Jnl(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        InstCPU.run(self)
        if not self.pcb.getFlagS():
            self.pcb.pc = self.pcb.pc+self.displacement
    
