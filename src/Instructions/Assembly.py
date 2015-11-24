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

    
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        value = memory.getDir(self.absoluteDataPosition(pcb,mmu,self.relativePositionFrom))
        
        memory.putDir(self.absoluteDataPosition(pcb, mmu, self.relativePositionWhereToMove), value)
        print "Escribi", value," en la posicion ", self.absoluteDataPosition(pcb, mmu, self.relativePositionWhereToMove)

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
    

    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        value = self.literalValue
        memory.putDir(self.absoluteDataPosition(pcb, mmu, self.relativePositionWhereToMove), value)
        #self.logger.log("Escribi "+str(value)+" en la posicion "+str(self.absolutePosition+self.relativePositionWhereToMove))
        

        
class Add(InstCPU):
    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "Add")
        self.logger = FileLogger("../../log/cpu_log")
     

        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToSum = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionFrom))
        anotherValueToSum = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToSum+anotherValueToSum)
        
                

class Mul(InstCPU):
    def __init__(self, relativePositionWhereToMove, relativePositionFrom):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.relativePositionFrom = relativePositionFrom
        InstCPU.__init__(self, "MUL")
        self.logger = FileLogger("../../log/cpu_log")
     
    
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToMul = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionFrom))
        anotherValueToMul = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToMul*anotherValueToMul)
        #self.logger.log("Escribi "+str(valueToMul*anotherValueToMul)+" en la posicion"+str(self.absolutePosition+self.relativePositionWhereToMove))


        
class AddLiteral(InstCPU):
    
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "AddLiteral")
        self.logger = FileLogger("../../log/assembly_log")

    
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToSum = self.literalValue
        anotherValueToSum = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToSum+anotherValueToSum)
        #self.logger.log("Escribi "+str(valueToSum+anotherValueToSum)+" en la posicion"+str(self.absolutePosition+self.relativePositionWhereToMove))
        


class MulLiteral(InstCPU):
    
    def __init__(self, relativePositionWhereToMove, literalValue):
        self.relativePositionWhereToMove = relativePositionWhereToMove
        self.literalValue = literalValue
        InstCPU.__init__(self, "MulLiteral")
        self.logger = FileLogger("../../log/cpu_log")
    
    
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToMul = self.literalValue
        anotherValueToMul = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove))
        memory.putDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionWhereToMove), valueToMul*anotherValueToMul)
        #self.logger.log("Escribi "+str(valueToMul*anotherValueToMul)+" en la posicion"+str(self.absolutePosition+self.relativePositionWhereToMove))

        
class Jmp(InstCPU):
    def __init__(self, relativePositionWhereToMove):
        self.relativePositionWhereToMove=relativePositionWhereToMove
        InstCPU.__init__(self, "JMP")
        self.logger = FileLogger("../../log/cpu_log")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        pcb.pc = self.relativePositionWhereToMove

        


class Cmp(InstCPU):
    def __init__(self, relativePositionToCompare, relativePositionToCompare2):
        self.relativePositionToCompare = relativePositionToCompare
        self.relativePositionToCompare2 = relativePositionToCompare2
        InstCPU.__init__(self, "CMP")
        self.logger = FileLogger("../../log/cpu_log")

        
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
    def __init__(self, relativePositionToCompare,valueLiteral):
        self.relativePositionToCompare=relativePositionToCompare
        self.valueLiteral=valueLiteral
        InstCPU.__init__(self, "CMP")
        self.logger = FileLogger("../../log/assembly_log")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        valueToCompare = memory.getDir(self.absoluteDataPosition(pcb, mmu,self.relativePositionToCompare))
        res = valueToCompare - self.valueLiteral        
        if(res == 0):
            pcb.flagZ = True
        if(res < 0):
            pcb.flagS = True


        
class Je(InstCPU):
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JE")
        self.logger = FileLogger("../../log/assembly_log")
        
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if pcb.getFlagZ():
            pcb.pc = pcb.pc+self.displacement

class Jne(InstCPU):
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JE")
        self.logger = FileLogger("../../log/assembly_log")
        
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if not pcb.getFlagZ():
            pcb.pc = pcb.pc+self.displacement
            
class Jl(InstCPU):
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JL")
        self.logger = FileLogger("../../log/assembly_log")
        
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if pcb.getFlagS():
            pcb.pc = pcb.pc+self.displacement
            
            
class Jle(InstCPU):
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JLE")
        self.logger = FileLogger("../../log/assembly_log")
        
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if pcb.getFlagS() or pcb.getFlagZ():
            pcb.pc = pcb.pc+self.displacement
            
class Jnl(InstCPU):
    def __init__(self, displacement):
        self.displacement=displacement
        InstCPU.__init__(self, "JNL")
        self.logger = FileLogger("../../log/assembly_log")
        
    def run(self,pcb,memory,mmu):
        InstCPU.run(self,pcb,memory,mmu)
        if not pcb.getFlagS():
            pcb.pc = pcb.pc+self.displacement

        


class ScreenPrint(InstIO):
    
    def __init__(self, message):
        self.message = message
        #self.logger = FileLogger("../../log/Printer")
    
    def run(self):
        # self.logger.log("Ejecutando desde impresora...")
        print "-.-.-.-.Executin from Printer.-.-.-.-"        
        #self.logger.log(self.message)
