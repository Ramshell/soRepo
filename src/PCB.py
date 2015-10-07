

class PCB:


    def __init__(self, idP, base, size):
        self.pc = 0
        self.pid = idP
        self.baseDir = base
        self.size = size

    def incrementPc(self):
        self.pc = self.pc + 1

    def getBaseDir(self):
        return self.baseDir

    def getPc(self):
        return self.pc

    def getSize(self):
        return self.size

    def finished(self):
        return self.getPc() == self.getSize()
