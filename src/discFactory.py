from Program import Program
from InstIO import InstIO
from InstCPU import InstCPU
from HardDisk import HardDisk


class diskFactory(object):
    


    def __init__(self):
        pass
    
    def basicHDD(self):
        self.sbl = Program("sublimeText")
        self.instr1 = InstIO("io",0)
        self.instr2 = InstCPU("sblm cpu")
        self.sbl.addInstruction(self.instr1)
        self.sbl.addInstruction(self.instr2)
        
        self.vim = Program("vim")
        self.instrVim1 = InstCPU("vim")
        self.instrVim2 = InstCPU("vim cpu")
        self.instrVim3 = InstCPU("vim cpu")
        self.instrVim4 = InstCPU("vim cpu")
        self.instrVim5 = InstCPU("vim cpu")
        self.instrVim6 = InstCPU("vim cpu")
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
        