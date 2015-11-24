from threading import Thread

from Manual import Manual


class Shell(Thread):
    
    __slots__ = ["buildIn"]


    def __init__(self,kernel=None, manuals=None):
        Thread.__init__(self)
        self.buildIn = {'execute' : self.execute, '?' : self.help, 'ps' : self.ps, 'kill' : self.kill, 'man' : self.manual}
        self.kernel=kernel
        self.manuals = self.createManuals()
        
    def run(self):
        while(True):
            inst = raw_input("|: ")
            self.parse(inst)
            
        
    def setKernel(self,kernel):
        self.kernel = kernel
        
    def execute(self,command):
        args = len(command)
        if args == 1:
            print "Give me some program to execute"
            return
        else:
            program = command.pop(0)[0]
            #i need to fix it
            #poss_args = program.max_args(command)
            if args > 3:
                self.real_execute(program,int(command[2]),command[3:])
                return
            if args > 2:
                self.real_execute(program,int(command[2]))
            else:
                self.real_execute(program)

    def real_execute(self,program_name,priority=0,args=[]):        
        self.pid = self.kernel.run(program_name,priority,args)
        print "successful execution with pid: ", self.pid
        
    def kill(self,args):
        #si le pones args deberia tirar error o te olvias de los args?                
        self.kernel.kill(args[1])
    
    def help(self, args):
        #si le pones args deberia tirar error o te olvias de los args?
        print "NSN bash, version 0.0.0(1)-release shortly in linux-windows-mac-os"
        print "These shell commands are defined internally. Type `help' to see this list."
        print "Type help 'name' to find out more about the function 'name'"
        print "Use 'info bash' to find out more about the shell in general."
        print "Use `man -k' or `info' to find out more about commands not in this list."
        self.my_real_help()
    
    def my_real_help(self):
        print "i don't have anything"
        
    def ps(self, args):
        self.kernel.ps()
    
    def pid(self, args):
        pass
    
    def parse(self, command_line):
        command = command_line.split(' ')
        program = command[0]
        
        if(program in self.buildIn):
            self.buildIn[program](command)
        else:
            self.dir_print("syntax error " + command_line + " is not a command")
        
    def manual(self, command):
        args = len(command)
        #no params
        if args == 1:
            self.dir_print("what manual page do you want?")
            return
        #just 1 param
        if args == 2:
            self.print_manual(command[1])
        #show the manual for each command
        if args > 2:
            command.pop(0)
            for arg in command:
                self.print_manual(arg)

    def print_manual(self, man):
        if man in self.manuals:
            self.manuals[man].printManual()
        else:
            in_disk_manual = self.fetch_man_in_disk(man)
            if in_disk_manual is not None:
                in_disk_manual.getManual().printManual()
            else:
                self.no_exist_manual(man)
            
    def fetch_man_in_disk(self, man):
        return self.kernel.manual(man)
        
    def no_exist_manual(self, arg):
        self.dir_print("No manual entry for " + arg)
                
    def createManuals(self):
        #creating manuals
        manexe = Manual("execute", "run a program", ["a program"])
        manps = Manual("ps", "displays information about a selection of the active processes.")
        mankill = Manual("kill", "Terminate process with given signal, send a signal to a process", ["a process"])
        manman = Manual("man", "see the manual of a program, utility or function",["a program","an important function","a system's command"])        
        #my manual
        manuals = {manexe.name : manexe, manps.name : manps, mankill.name : mankill, manman.name : manman}
        
        return manuals
        
    def printProgramManual(self,programName):
        self.kernel.manual(programName).printManual()
    
    def dir_print(self, to_print, impressor=None):
        print to_print
        
if __name__ == '__main__':
    shell = Shell()
    shell.start()
        
        