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
        
        self.manMultiplatory = Manual("multiplatory", "multiplatory(n)")
        self.multiplatory = Program("multiplatory", self.manMultiplatory)
        # the relative position 0 has the n
        self.instrMultiplatory1 = MovLiteral(1, 1)
        self.instrMultiplatory2 = MovLiteral(2, 1)
        self.instrMultiplatory3 = CmpLiteral(0, 0)
        self.instrMultiplatory4 = Jle(4)
        self.instrMultiplatory5 = Mul(1, 2)
        self.instrMultiplatory6 = AddLiteral(2, 1)
        self.instrMultiplatory7 = AddLiteral(0, -1)
        self.instrMultiplatory8 = Jmp(3)
        self.instrMultiplatory9 = ScreenPrintValue(1)
        
        self.multiplatory.addInstruction(self.instrMultiplatory1)
        self.multiplatory.addInstruction(self.instrMultiplatory2)
        self.multiplatory.addInstruction(self.instrMultiplatory3)
        self.multiplatory.addInstruction(self.instrMultiplatory4)
        self.multiplatory.addInstruction(self.instrMultiplatory5)
        self.multiplatory.addInstruction(self.instrMultiplatory6)
        self.multiplatory.addInstruction(self.instrMultiplatory7)
        self.multiplatory.addInstruction(self.instrMultiplatory8)
        self.multiplatory.addInstruction(self.instrMultiplatory9)
        
        
        
        self.sumatoryManual = Manual("sumatory", "sumatory(n)")
        self.sumatory = Program("sumatory", self.sumatoryManual)
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
        
