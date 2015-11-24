from threading import Thread
from Manual import Manual
from Exceptions.InvalidProgramException import InvalidProgramException

class Shell(Thread):
    
    __slots__ = ["buildIn"]


    def __init__(self, kernel=None, manuals=None):
        Thread.__init__(self)
        self.buildIn = ["?", "execute", "ps", "pid", "kill", "man"]
        self.kernel = kernel
        self.manuals = self.chargeManuals()
        
    def run(self):
        while(True):
            inst = raw_input("|: ")
            self.parse(inst)
            
        
    def setKernel(self, kernel):
        self.kernel = kernel
                
    def execute(self, command):
        print command
        programaBuiltIn = command.pop(0) #This is from Shell, we don't need this
        
        if len(command) == 0:
            raise InvalidProgramException("No Program to Run")
        
        programToExecute = command.pop(0)
        
        if len(command) == 0:
            self.real_execute(programToExecute,0, command)
        else:
            assignedPriority = int(command.pop(0))
            print assignedPriority
            self.real_execute(programToExecute, assignedPriority , command)

    def real_execute(self, program_name, priority=0, args=[]): 
        self.pid = self.kernel.run(program_name, priority, args)
        print "successful execution with pid: ", self.pid
        
    def kill(self, args):
        # si le pones args deberia tirar error o te olvias de los args?                
        self.kernel.kill(args[1])
    
    def help(self, args):
        # si le pones args deberia tirar error o te olvias de los args?
        print "NSN bash, version 0.0.0(1)-release shortly in linux-windows-mac-os"
        print "These shell commands are defined internally. Type `help' to see this list."
        print "Type help 'name' to find out more about the function 'name'"
        print "Use 'info bash' to find out more about the shell in general."
        print "Use `man -k' or `info' to find out more about commands not in this list."
        self.my_real_help()
    
    def my_real_help(self):
        print "i don't have anything"
        
    def ps(self, args):
        # si le pones args deberia tirar error o te olvias de los args?
        self.kernel.ps()
    
    def pid(self, args):
        # como le pido el pid???
        pass
    
    def parse(self, command_line):
        command = command_line.split(' ')
        # that command exist?
        exist = self.buildIn.count(command[0])
        if(exist != 0):
            # index of that program
            inst_index = self.buildIn.index(command[0])
            # trying to exec that command
            self.execBuildIn(inst_index, command)
        else:
            print "syntax error ", command_line, " is not a command"
            
    def execBuildIn(self, inst_index, command):
        # "?","execute","ps","pid","kill", "man"
        if inst_index == 0:
            self.help(command)
        if inst_index == 1:
            
            try:
                self.execute(command)
            except InvalidProgramException as e:
                print e
                
        if inst_index == 2:
            self.ps(command)
            return
        if inst_index == 3:
            self.pid(command)
            return
        if inst_index == 4:
            self.kill(command)
            return
        if inst_index == 5:
            self.manual(command)
            return
        
    def manual(self, command):
        args = len(command)
        if args == 1:
            self.dir_print("what manual page do you want?")
            return
        if args == 2:
            self.print_manual(command[1])
        if args > 2:
            command.pop(0)
            for arg in command:
                self.print_manual(arg)

    def print_manual(self, man):
        exist = self.exist_manual(man)
        if exist >= 0:
            self.manuals[exist].printManual()
        else:
            in_disk_manual = self.fetch_man_in_disk(man)
            if in_disk_manual is not None:
                in_disk_manual.getManual().printManual()
            else:
                self.no_exist_manual(man)
            
    def fetch_man_in_disk(self, man):
        return self.kernel.manual(man)
        
    def no_exist_manual(self, arg):
        print "No manual entry for", arg
    
    def exist_manual(self, name):
        i = 0
        for manual in self.manuals:
            if manual.name == name:
                return i
            i = i + 1
        return -1
            
    def chargeManuals(self):
        self.manuals = []
        manexe = Manual("execute", "run a program", ["a program"])
        manps = Manual("ps", "displays information about a selection of the active processes.")
        mankill = Manual("kill", "Terminate process with given signal, send a signal to a process", ["a process"])
        manman = Manual("man", "see the manual of a program, utility or function", ["a program", "an important function", "a system's command"])
        self.manuals.append(manexe)
        self.manuals.append(manps)
        self.manuals.append(mankill)
        self.manuals.append(manman)
        return self.manuals
        
    def printProgramManual(self, programName):
        self.kernel.manual(programName).printManual()
    
    def dir_print(self, to_print, impressor=None):
        print to_print
        
if __name__ == '__main__':
    shell = Shell()
    shell.start()
        
        
