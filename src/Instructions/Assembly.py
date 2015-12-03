from InstCPU import InstCPU
from Instructions.InstIO import InstIO
from util.FileLogger import FileLogger


class Mov(InstCPU):
    
    '''
    @note: the goal of this instruction is to replace the value allocated in a direction
           of the ram with another value allocated in the ram.   
    '''

    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "Mov")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        value = memory.getDir(self.absoluteDataPosition(pcb,mmu,self.relativePositionFrom))
        memory.putDir(self.absoluteDataPosition(pcb, mmu, self.relativePositionWhereToMove), value)

class MovLiteral(InstCPU):
    '''
    @note: the goal of this instruction is to replace the value allocated in a direction of the ram
           with another value  
    '''
    
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "MovLiteral")

    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        value = self.literalValue
        memory.putDir(self.absoluteDataPosition(pcb, mmu, self.relativePositionWhereToMove), value)
        
class Add(InstCPU):
    '''
    @note: the goal of this instruction is to sum the values allocated in two directions of the memory ram
    '''
    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "Add")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToSum = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionFrom))
        anotherValueToSum = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToSum+anotherValueToSum) 

class Mul(InstCPU):
    '''
    @note: the goal of this instruction is to multiply the values allocated in two directions of the memory ram
    '''
    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "MUL")
    
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToMul = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionFrom))
        anotherValueToMul = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToMul*anotherValueToMul)
            
class AddLiteral(InstCPU):
    '''
    @note: the goal of this instruction is to sum the values allocated in a direction of the memory ram with a literal value
    '''
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "AddLiteral")

    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToSum = self.literalValue
        anotherValueToSum = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToSum+anotherValueToSum)

class MulLiteral(InstCPU):
    '''
    @note: the goal of this instruction is to multiply the values allocated in a direction of the memory ram with a literal value
    '''
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "MulLiteral")
    
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToMul = self.literalValue
        anotherValueToMul = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToMul*anotherValueToMul)
        
class Jmp(InstCPU):
    '''
    @note: the goal of this instruction is to jump to a relative position of the logic memory no matter what
    '''
    def __init__(self, relativePositionWhereToMove):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        InstCPU.__init__(self, "JMP")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        pcb.pc = self.relativePositionWhereToMove

class Cmp(InstCPU):
    '''
    @note: the goal of this instruction is to modify the pcb flags, based on a subtraction between two specified memory values compared against 0
    '''
    def __init__(self, relativePositionToCompare, relativePositionToCompare2):
        self.relativePositionToCompare = relativePositionToCompare
        self.relativePositionToCompare2 = relativePositionToCompare2
        InstCPU.__init__(self, "CMP")

    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToCompare = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionToCompare))
        anotherValueToCompare = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionToCompare2))
        res = valueToCompare - anotherValueToCompare
        if(res == 0):
            pcb.flagZ = True
        if(res < 0):
            pcb.flagS = True
                 
class CmpLiteral(InstCPU):
    '''
    @note: the goal of this instruction is to modify the pcb flags, based on a subtraction between a specified memory value and a literal value compared against 0
    '''
    def __init__(self, relativePositionToCompare,valueLiteral):
        self.relativePositionToCompare=relativePositionToCompare
        self.valueLiteral=valueLiteral
        InstCPU.__init__(self, "CMP")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToCompare = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionToCompare))
        res = valueToCompare - self.valueLiteral        
        if(res == 0):
            pcb.flagZ = True
        if(res < 0):
            pcb.flagS = True

class Je(InstCPU):
    '''
    @note: the goal of this instruction is to increase the pcb's pc, if and only if (iif) the pcb's flagZ is True
    '''
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JE")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if pcb.getFlagZ():
            pcb.pc = pcb.pc+self.displacement

class Jne(InstCPU):
    '''
    @note: the goal of this instruction is to increase the pcb's pc, if and only if (iif) the pcb's flagZ is False
    '''
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JE")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self)
        if not pcb.getFlagZ():
            pcb.pc = pcb.pc+self.displacement
            
class Jl(InstCPU):
    '''
    @note: the goal of this instruction is to increase the pcb's pc, if and only if (iif) the pcb's flagS is True
    '''
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JL")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if pcb.getFlagS():
            pcb.pc = pcb.pc+self.displacement
            
class Jle(InstCPU):
    '''
    @note: the goal of this instruction is to increase the pcb's pc, if and only if (iif) the pcb's flagZ is True or the pcb's flagS is True
    '''
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JLE")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if pcb.getFlagS() or pcb.getFlagZ():
            pcb.pc = pcb.pc+self.displacement
            
class Jnl(InstCPU):
    '''
    @note: the goal of this instruction is to increase the pcb's pc, if and only if (iif) the pcb's flagS is False
    '''
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JNL")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if not pcb.getFlagS():
            pcb.pc = pcb.pc+self.displacement
        
class ScreenPrintValue(InstIO):
    '''
    @note: the goal of this instruction is to print the value allocated in a specified logic memory position into the standard device
    '''
    
    def __init__(self, relativePositionWhereTheValueIs):
        InstIO.__init__(self, "Print Screen",0)
        self.relativePositionWhereTheValueIs = relativePositionWhereTheValueIs
        
    def setValue(self,pcb,memory,mmu):
        self.value = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereTheValueIs))
    
    def run(self):
        pass
