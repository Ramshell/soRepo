from InstCPU import InstCPU
from Instructions.InstIO import InstIO
from util.FileLogger import FileLogger


class Mov(InstCPU):
    
    '''
    @note: the goal of this instruction is replace the value allocated in a direction
           of the ram with another value allocated in the ram.   
    '''

    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "Mov")
        self.logger = FileLogger("../../log/cpu_log")
     
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Mov(self.relativePositionWhereToMove, self.relativePositionFrom)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        value = self.ram.getDir(self.absolutePosition + self.relativePositionFrom)
        
        self.ram.putDir(self.absolutePosition + self.relativePositionWhereToMove, value)
        # self.logger.log("Escribi "+str(value)+" en la posicion "+(str(self.absolutePosition+self.relativePositionWhereToMove)))
        print "MOV--- " , str(value) , " at position " , (str(self.absolutePosition + self.relativePositionWhereToMove))
        
class MovLiteral(InstCPU):
    

    '''
    @note: the goal of this instruction is replace the value allocated in a direction of the ram
           with another value  
    '''
    
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "MovLiteral")
        self.logger = FileLogger("../../log/cpu_log")
    
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self, memory, pcb):
        insToReturn = MovLiteral(self.relativePositionWhereToMove, self.literalValue)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
    
    def run(self):
        value = self.literalValue
        self.ram.putDir(self.absolutePosition + self.relativePositionWhereToMove, value)
        # self.logger.log("Escribi "+str(value)+" en la posicion "+str(self.absolutePosition+self.relativePositionWhereToMove))
        print "MOV LITERAL--- " , str(value) , " at position " , str(self.absolutePosition + self.relativePositionWhereToMove)
        
class Add(InstCPU):
    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "Add")
        self.logger = FileLogger("../../log/cpu_log")
     
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Add(self.relativePositionWhereToMove, self.relativePositionFrom)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        valueToSum = self.ram.getDir(self.absolutePosition + self.relativePositionFrom)
        anotherValueToSum = self.ram.getDir(self.absolutePosition + self.relativePositionWhereToMove)
        
        self.ram.putDir(self.absolutePosition + self.relativePositionWhereToMove, valueToSum + anotherValueToSum)
        # self.logger.log("Escribi "+str(valueToSum+anotherValueToSum)+" en la posicion "+str(self.absolutePosition+self.relativePositionWhereToMove))
        print "ADD--- " , str(valueToSum + anotherValueToSum) , " at position " , str(self.absolutePosition + self.relativePositionWhereToMove)

class Mul(InstCPU):
    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "MUL")
        self.logger = FileLogger("../../log/cpu_log")
     
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Mul(self.relativePositionWhereToMove, self.relativePositionFrom)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        valueToMul = self.ram.getDir(self.absolutePosition + self.relativePositionFrom)
        anotherValueToMul = self.ram.getDir(self.absolutePosition + self.relativePositionWhereToMove)
        
        self.ram.putDir(self.absolutePosition + self.relativePositionWhereToMove, valueToMul * anotherValueToMul)
        # self.logger.log("Escribi "+str(valueToMul*anotherValueToMul)+" en la posicion "+str(self.absolutePosition+self.relativePositionWhereToMove))
        print "MUL--- " , str(valueToMul * anotherValueToMul) , " at position " , str(self.absolutePosition + self.relativePositionWhereToMove)

        
class AddLiteral(InstCPU):
    
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "AddLiteral")
        self.logger = FileLogger("../../log/cpu_log")
    
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self, memory, pcb):
        insToReturn = AddLiteral(self.relativePositionWhereToMove, self.literalValue)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
    
    def run(self):
        valueToSum = self.literalValue
        anotherValueToSum = self.ram.getDir(self.absolutePosition + self.relativePositionWhereToMove)
        self.ram.putDir(self.absolutePosition + self.relativePositionWhereToMove, valueToSum + anotherValueToSum)
        # self.logger.log("Escribi "+str(valueToSum+anotherValueToSum)+" en la posicion"+str(self.absolutePosition+self.relativePositionWhereToMove))
        print "ADD LITERAL--- " , str(valueToSum + anotherValueToSum) , " at position " , str(self.absolutePosition + self.relativePositionWhereToMove)


class MulLiteral(InstCPU):
    
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "MulLiteral")
        self.logger = FileLogger("../../log/cpu_log")
    
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        
    def instructionInstance(self, memory, pcb):
        insToReturn = MulLiteral(self.relativePositionWhereToMove, self.literalValue)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
    
    def run(self):
        valueToMul = self.literalValue
        anotherValueToMul = self.ram.getDir(self.absolutePosition + self.relativePositionWhereToMove)
        self.ram.putDir(self.absolutePosition + self.relativePositionWhereToMove, valueToMul * anotherValueToMul)
        # self.logger.log("Escribi "+str(valueToMul*anotherValueToMul)+" en la posicion"+str(self.absolutePosition+self.relativePositionWhereToMove))
        print "MUL LITERAL--- " , str(valueToMul * anotherValueToMul) , " at position " , str(self.absolutePosition + self.relativePositionWhereToMove)

        
class Jmp(InstCPU):
    def __init__(self, relativePositionWhereToMove, pcb=None):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.pcb = pcb
        InstCPU.__init__(self, "JMP")
        self.logger = FileLogger("../../log/cpu_log")
        
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Jmp(self.relativePositionWhereToMove)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        self.pcb.pc = self.relativePositionWhereToMove
        


class Cmp(InstCPU):
    def __init__(self, relativePositionToCompare, relativePositionToCompare2):
        self.relativePositionToCompare = relativePositionToCompare
        self.relativePositionToCompare2 = relativePositionToCompare2
        InstCPU.__init__(self, "CMP")
        self.logger = FileLogger("../../log/cpu_log")
     
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Cmp(self.relativePositionToCompare, self.relativePositionToCompare2)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        valueToCompare = self.ram.getDir(self.absolutePosition + self.relativePositionToCompare)
        anotherValueToCompare = self.ram.getDir(self.absolutePosition + self.relativePositionToCompare2)
        res = valueToCompare - anotherValueToCompare
        if(res == 0):
            self.pcb.flagZ = True
        if(res < 0):
            self.pcb.flagS = True
            
            
class CmpLiteral(InstCPU):
    def __init__(self, relativePositionToCompare, valueLiteral, pcb=None):
        self.relativePositionToCompare = relativePositionToCompare
        self.valueLiteral = valueLiteral
        self.pcb = pcb
        InstCPU.__init__(self, "CMP")
        self.logger = FileLogger("../../log/cpu_log")
     
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = CmpLiteral(self.relativePositionToCompare, self.valueLiteral)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        valueToCompare = self.ram.getDir(self.absolutePosition + self.relativePositionToCompare)
        res = valueToCompare - self.valueLiteral        
        if(res == 0):
            self.pcb.flagZ = True
        if(res < 0):
            self.pcb.flagS = True


        
class Je(InstCPU):
    def __init__(self, displacement, pcb=None):
        self.displacement = displacement
        self.pcb = pcb
        InstCPU.__init__(self, "JE")
        self.logger = FileLogger("../../log/assembly_log")
        
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Je(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        if self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc + self.displacement

class Jne(InstCPU):
    def __init__(self, displacement, pcb=None):
        self.displacement = displacement
        self.pcb = pcb
        InstCPU.__init__(self, "JE")
        self.logger = FileLogger("../../log/assembly_log")
        
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Jne(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        if not self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc + self.displacement
            
class Jl(InstCPU):
    def __init__(self, displacement, pcb=None):
        self.displacement = displacement
        self.pcb = pcb
        InstCPU.__init__(self, "JL")
        self.logger = FileLogger("../../log/assembly_log")
        
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Jl(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        if self.pcb.getFlagS():
            self.pcb.pc = self.pcb.pc + self.displacement
            
            
class Jle(InstCPU):
    def __init__(self, displacement, pcb=None):
        self.displacement = displacement
        self.pcb = pcb
        InstCPU.__init__(self, "JLE")
        self.logger = FileLogger("../../log/assembly_log")
        
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Jle(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        if self.pcb.getFlagS() or self.pcb.getFlagZ():
            self.pcb.pc = self.pcb.pc + self.displacement
            
class Jnl(InstCPU):
    def __init__(self, displacement, pcb=None):
        self.displacement = displacement
        self.pcb = pcb
        InstCPU.__init__(self, "JNL")
        self.logger = FileLogger("../../log/assembly_log")
        
    def setCurrentPosition(self, pcb, memory):
        self.absolutePosition = pcb.getBaseDir() + pcb.size
        self.ram = memory
        self.pcb = pcb
        
    def instructionInstance(self, memory, pcb):
        insToReturn = Jnl(self.displacement)
        insToReturn.setCurrentPosition(pcb, memory)
        return insToReturn
        
    def run(self):
        if not self.pcb.getFlagS():
            self.pcb.pc = self.pcb.pc + self.displacement

class ScreenPrint(InstIO):
    
    def __init__(self, message):
        self.message = message
        self.logger = FileLogger("../../log/Printer")
    
    def run(self):
        # self.logger.log("Ejecutando desde impresora...")
        print "-.-.-.-.Executin from Printer.-.-.-.-"        
        self.logger.log(self.message)
