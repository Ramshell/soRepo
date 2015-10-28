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
            self.parse(inst)
            
        
    def setKernel(self,kernel):
        self.kernel = kernel
        
    def execute(self,programName,priority=0):
        self.pid = self.kernel.run(programName,priority)
        print "successful execution with pid: ", self.pid

        
    def kill(self,pid):
        self.kernel.kill(pid)
    
    def ps(self):
        self.kernel.ps()
    
    def parse(self,inst):
        self.aux = inst.split(' ')
        if self.aux[0] in self.buildIn:
            self.execBuildIn(self.aux)
        else:
            print "syntax error ", inst, " is not a command"
            
    def execBuildIn(self,inst):
        if inst[0] == "execute":
            if len(inst) > 2:
                self.execute(inst[1],int(inst[2]))
            else:
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
        
        