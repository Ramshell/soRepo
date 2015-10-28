from Program import Program
from InstIO import InstIO
from InstCPU import InstCPU
from HardDisk import HardDisk


class diskFactory(object):
    


    def __init__(self):
        pass
    
    def basicHDD(self):
        self.sbl = Program("sublimeText")
        self.instr1 = InstIO("io",1)
        self.instr2 = InstCPU("sblm cpu")
        self.sbl.addInstruction(self.instr1)
        self.sbl.addInstruction(self.instr2)
        
        self.vim = Program("vim")
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
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        self.vim.addInstruction(self.instrVim6)
        
        self.hdd = HardDisk()
        self.hdd.setProgram(self.vim)
        self.hdd.setProgram(self.sbl)
        
        return self.hdd
        