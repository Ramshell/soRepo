from storage.HardDisk import HardDisk
from Instructions.Assembly import *
from Instructions.InstCPU import InstCPU
from Instructions.InstIO import InstIO
from programs.Manual import Manual
from programs.Program import Program


class diskFactory(object):
    


    def __init__(self):
        pass
    
    def basicHDD(self):
        '''
        @return: an HDD with 4 programs, 2 simple programs, and 2 "real programs", factorial n and summatory n
        '''
        self.manSublime = Manual("sublimeText", "make something in I/O")
        self.sbl = Program("sublimeText")
        self.instr1 = InstIO("ioDePrinter", 1)
        self.instr10 = InstIO("io De screen", 0)
        self.instr01 = InstIO("io De screen", 0)
        self.instr111 = InstIO("ioDePrinter", 1)
        self.instr2 = InstCPU("sblm cpu")
        self.sbl.addInstruction(self.instr1)
        self.sbl.addInstruction(self.instr2)
        self.sbl.addInstruction(self.instr1)
        self.sbl.addInstruction(self.instr1)
        self.sbl.addInstruction(self.instr10)
        self.sbl.addInstruction(self.instr01)
        self.sbl.addInstruction(self.instr1)
        self.sbl.addInstruction(self.instr111)
        self.sbl.addManual(self.manSublime)
        
        self.manVim = Manual("vim", "have too many instructions")
        self.vim = Program("vim", self.manVim)
        self.instrVim1 = InstCPU("vim 1")
        self.instrVim2 = InstCPU("vim 2")
        self.instrVim3 = InstCPU("vim 3")
        self.instrVim4 = InstCPU("vim 4")
        self.instrVim5 = InstCPU("vim 5")
        self.instrVim6 = InstCPU("vim 6")
        self.vim.addInstruction(self.instrVim1)
        self.vim.addInstruction(self.instrVim2)
        self.vim.addInstruction(self.instrVim3)
        self.vim.addInstruction(self.instrVim4)
        self.vim.addInstruction(self.instrVim5)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instr111)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instr111)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        
        self.manMultiplatory = Manual("factorial", "factorial(n)")
        self.multiplatory = Program("factorial", self.manMultiplatory)
        self.multiplatory.variableSize = 3
        # the relative position 0 has the n
        self.multiplatory.addInstruction(MovLiteral(1, 1))
        self.multiplatory.addInstruction(MovLiteral(2, 2))
        self.multiplatory.addInstruction(CmpLiteral(0, 1))
        self.multiplatory.addInstruction(Jle(4))
        self.multiplatory.addInstruction(Mul(1, 2))
        self.multiplatory.addInstruction(AddLiteral(2, 1))
        self.multiplatory.addInstruction(AddLiteral(0, -1))
        self.multiplatory.addInstruction(Jmp(3))
        self.multiplatory.addInstruction(ScreenPrintValue(1))
        
        
        
        self.sumatoryManual = Manual("summatory", "summatory(n)")
        self.sumatory = Program("summatory", self.sumatoryManual)
        self.sumatory.variableSize = 3
        self.sumatory.addInstruction(MovLiteral(1, 0))
        self.sumatory.addInstruction(MovLiteral(2, 1))
        self.sumatory.addInstruction(CmpLiteral(0, 0))
        self.sumatory.addInstruction(Jle(4))
        self.sumatory.addInstruction(Add(1, 2))
        self.sumatory.addInstruction(AddLiteral(2, 1))
        self.sumatory.addInstruction(AddLiteral(0, -1))
        self.sumatory.addInstruction(Jmp(3))
        self.sumatory.addInstruction(ScreenPrintValue(1))
        
        self.hdd = HardDisk()
        self.hdd.setProgram(self.vim)
        self.hdd.setProgram(self.sbl)
        self.hdd.setProgram(self.multiplatory)
        self.hdd.setProgram(self.sumatory)
        
        return self.hdd
        
