from Program import Program
from InstIO import InstIO
from InstCPU import InstCPU
from HardDisk import HardDisk
from Manual import Manual
from Instructions.Assembly import *

class diskFactory(object):
    


    def __init__(self):
        pass
    
    def basicHDD(self):
        self.manSublime = Manual("sublimeText", "make something in I/O")
        self.sbl = Program("sublimeText")
        self.instr1 = InstIO("ioDePrinter",1)
        self.instr10 = InstIO("io De screen",0)
        self.instr01 = InstIO("io De screen",0)
        self.instr111 = InstIO("ioDePrinter",1)
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
        self.vim = Program("vim",self.manVim)
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
        
        self.manFibbo = Manual("fibbo", "fibo(n)")
        self.fibbo =Program("fibbo",self.manFibbo)
        #the relative position 0 has the n
        self.instrFibbo1 = MovLiteral(1,1)
        self.instrFibbo2 = MovLiteral(2,2)
        self.instrFibbo3 = CmpLiteral(0,1)
        self.instrFibbo4 = Jle(5)
        self.instrFibbo5 = Mul(1,2)
        self.instrFibbo6 = AddLiteral(2,1)
        self.instrFibbo7 = AddLiteral(0,-1)
        self.instrFibbo8 = Jmp(3)
        self.instrFibbo9 = InstIO("printeando el resultado",0)
        
        self.fibbo.addInstruction(self.instrFibbo1)
        self.fibbo.addInstruction(self.instrFibbo2)
        self.fibbo.addInstruction(self.instrFibbo3)
        self.fibbo.addInstruction(self.instrFibbo4)
        self.fibbo.addInstruction(self.instrFibbo5)
        self.fibbo.addInstruction(self.instrFibbo6)
        self.fibbo.addInstruction(self.instrFibbo7)
        self.fibbo.addInstruction(self.instrFibbo8)
        self.fibbo.addInstruction(self.instrFibbo9)
        
        
        
        self.sumatoryManual = Manual("sumatory", "sumatory(n)")
        self.sumatory =Program("sumatory",self.sumatoryManual)
        self.sumatory.addInstruction(MovLiteral(1,0))
        self.sumatory.addInstruction(MovLiteral(2,2))
        self.sumatory.addInstruction(CmpLiteral(0,1))
        self.sumatory.addInstruction(Jle(5))
        self.sumatory.addInstruction(Add(1,2))
        self.sumatory.addInstruction(AddLiteral(2,1))
        self.sumatory.addInstruction(AddLiteral(0,-1))
        self.sumatory.addInstruction(Jmp(3))
        self.sumatory.addInstruction(InstIO("printeando el resultado",0))
        
        self.hdd = HardDisk()
        self.hdd.setProgram(self.vim)
        self.hdd.setProgram(self.sbl)
        self.hdd.setProgram(self.fibbo)
        self.hdd.setProgram(self.sumatory)
        
        return self.hdd
        