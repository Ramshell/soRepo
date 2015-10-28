from threading import Thread


class Shell(Thread):
    
    __slots__ = ["buildIn"]


    def __init__(self,kernel=None):
        Thread.__init__(self)
        self.buildIn = ["execute","ps","kill"]
        self.kernel=kernel
        
        
    def run(self):
        while(True):
            inst = raw_input("|: ")
            print inst
            self.parse(inst)
            
        
    def setKernel(self,kernel):
        self.kernel = kernel
        
    def execute(self,programName):
        self.pid = self.kernel.run(programName)
        print "successful execution with pid: ", self.pid

        
    def kill(self,pid):
        print "killing: ", pid
    
    def ps(self):
        self.kernel.ps()
    
    def parse(self,inst):
        self.aux = inst.split(' ')
        print self.aux
        if self.aux[0] in self.buildIn:
            self.execBuildIn(self.aux)
        else:
            print "syntax error ", inst, " is not a command"
            
    def execBuildIn(self,inst):
        if inst[0] == "execute":
            self.execute(inst[1])
            return
        if inst[0] == "pid":
            self.pid(inst[1])
            return
        if inst[0] == "ps":
            self.ps()
            return
        else:
            self.kill(inst[1])
            

if __name__ == '__main__':
    shell = Shell()
    shell.start()
        
        