from threading import Thread
from Manual import Manual

class Shell(Thread):
    
    __slots__ = ["buildIn"]


    def __init__(self,kernel=None, manuals=None):
        Thread.__init__(self)
        self.buildIn = ["execute","ps","kill", "man"]
        self.kernel=kernel
        self.chargeManuals()
        
    def run(self):
        while(True):
            inst = raw_input("|: ")
            self.parse(inst)
            
        
    def setKernel(self,kernel):
        self.kernel = kernel
        
    def execute(self,programName,priority=0,args=[]):
        self.pid = self.kernel.run(programName,priority,args)
        print "successful execution with pid: ", self.pid

        
    def kill(self,pid):
        self.kernel.kill(pid)
    
    def ps(self):
        self.kernel.ps()
    
    def parse(self,inst):
        self.aux = inst.split(' ')
        if(self.aux[0]=='?'):
            print self.buildIn
            return
        if self.aux[0] in self.buildIn:
            self.execBuildIn(self.aux)
        else:
            print "syntax error ", inst, " is not a command"
            
    def execBuildIn(self,inst):
        if inst[0] == "execute":
            if len(inst) > 3:
                self.execute(inst[1],int(inst[2]),inst[3:])
                return
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
        if inst[0] == "man":
            if len(inst) == 1:
                print "what manual page do you want?"
                return
            for man in self.manuals:
                if inst[1] == man.name:
                    man.printManual()
                    return
            print "No manual entry for", inst[1]
            return    
            #self.printProgramManual(inst[1])
        else:
            self.kill(inst[1])
    
    def setManuals(self,manuals):
        self.manuals = manuals
        
    def chargeManuals(self):
        self.manuals = []
        manexe = Manual("execute", "run a program", ["a program"])
        manps = Manual("ps", "see the pcb information like pid, state and pc")
        mankill = Manual("kill", "close a program", ["a process"])
        manman = Manual("man", "see the manual of a program, utility or function",["a program","an important function","a system's command"])
        self.manuals.append(manexe)
        self.manuals.append(manps)
        self.manuals.append(mankill)
        self.manuals.append(manman)
        
    def printProgramManual(self,programName):
        self.kernel.manual(programName).printManual()
        
if __name__ == '__main__':
    shell = Shell()
    shell.start()
        
        