from __future__ import print_function
from threading import Thread
from programs.Manual import Manual
from Exceptions.InvalidProgramException import InvalidProgramException
from Consoles.MainConsoleThread import MainConsoleThread
from sys import stdin

class Shell(Thread):
    
    __slots__ = ["buildIn"]


    def __init__(self,console, kernel=None, manuals=None):
        """
        @note: Shell work together a Kernel and have default manuals, and initialize a thread
        Constructor a kernel and manuals
        """       
        
        Thread.__init__(self)
        self.buildIn = {'execute' : self.execute, '?' : self.help, 'ps' : self.ps, 'kill' : self.kill, 'man' : self.manual}
        self.kernel=kernel
        self.manuals = self.createManuals()
        self.console = console
        
    def run(self):
        """
        @note: this method start the shell
        """
        while(True):
            inst = raw_input("|: ")
            self.parse(inst)
            
        
    def setKernel(self, kernel):
        """
        @param kernel: its the new kernel for this shell
        """
        self.kernel = kernel
    #shell function                
    def execute(self, command):
        """
        @note: it's a shell build-in function.
        @param command: it's a program to run.
        @note: run the program in command
        """
        
        command.pop(0) #This is from Shell, we don't need this
        
        if len(command) == 0:
            #raise InvalidProgramException("No Program to Run")
            print ("No program to run",file=self.console)
            return
        programToExecute = command.pop(0)
        if(not self.kernel.in_disk(programToExecute)):
            #raise InvalidProgramException(programToExecute + " does not exist")
            print (programToExecute + " doesn't exist",file=self.console)
            return
        
        if len(command) == 0:
            self.real_execute(programToExecute,0, command)
        else:
            assignedPriority = int(command.pop(0))
            print (assignedPriority,file=self.console)
            self.real_execute(programToExecute, assignedPriority , command)

    def real_execute(self, program_name, priority=0, args=[]): 
        self.pid = self.kernel.run(program_name, priority, args)
        self.dir_print("Successful execution with pid: "+str(self.pid))
        
    #shell function        
    def kill(self, args):
        """
        @summary: it's a shell built-in command.
        @param args: these are program's pid.
        @note: terminate the programs asociated at pids in args.
        """
        if len(args) == 1:
            self.dir_print("Give me some pid to kill")
            return
        #first argument for args is not used
        args.pop(0)
        
        #pidtokill = args[0]
        for arg in args:
            try:
                self.kernel.kill(int(arg))
                
            except:
                self.dir_print("Error you can't kill " + arg + " please give me a pid number")
            
        #for arg in args:
        #    try:
        #        int(arg)
        #        self.kernel.kill(arg)
        #    except: raise Exception("invalid argument")
        
    
    #shell function    
    def help(self, args):
        """
        @note:  args: not used
        @summary: it's a shell built-in command
        @note: show a help provided for the system
        """
        
        print ("NSN bash, version 0.0.0(1)-release shortly in linux-windows-mac-os",file=self.console)
        print ("These shell commands are defined internally. Type `help' to see this list.",file=self.console)
        print ("Type help 'name' to find out more about the function 'name'",file=self.console)
        print ("Use 'info bash' to find out more about the shell in general.",file=self.console)
        print ("Use `man -k' or `info' to find out more about commands not in this list.",file=self.console)
        self.my_real_help()
    
    def my_real_help(self):
        """
        @note: this method just help the shell's help command
        """
        
        building_commands = self.buildIn.keys()
        self.dir_print("This are the usable commands: ")
        for command in building_commands:
            self.dir_print(command)
        
    #shell function        
    def ps(self, args):
        """
        @note: args are not used
        @note: it's a shell built-in command
        @note: show the current process in the system
        """
        print (self.kernel.ps(),file=self.console)
        

    def parse(self, command_line):
        """
        @note: read and parse the shell's input
        @param command_line: is the input to read
        """
        
        
        command = command_line.split(' ')
        program = command[0]
        if(len(program) == 0):
            return
        if(program in self.buildIn):
            self.buildIn[program](command)
        else:
            self.dir_print("syntax error " + command_line + " is not a command")
    
    #shell function    
    def manual(self, command):
        """
        @note: it's a shell built-in command
        @param command: the manuals to show
        @note: show the manuals in command
        """
        
        command.pop(0)
        args = len(command)
        if args == 0:
            self.dir_print("what manual page do you want?")
            return
        #just 1 param
        if args == 1:
            self.print_manual(command[0])
            return
        #show the manual for each command
        if args > 1:
            for arg in command:
                self.dir_print(self.print_manual(arg))

    #fetch man in mymanuals and disk manuals and then print it if found it
    def print_manual(self, man):
        """
        @note: just to help manual built-in function
        @param man: a manual to fetch and print
        """
        
        if man in self.manuals:
            self.dir_print(self.manuals[man].printManual())
        else:
            manual = self.fetch_man_in_disk(man)
            if manual is not None:
                self.dir_print(manual.getManual().printManual())
            else:
                self.no_exist_manual(man)
            
    def fetch_man_in_disk(self, man):
        """
        @note: just to help manual built-in function
        @param man: a manual to fetch
        """
        return self.kernel.manual(man)
        
    def no_exist_manual(self, arg):
        """
        @note: just to help manual built-in function
        @param arg: arg not found 
        """
        self.dir_print("No manual entry for " + arg)
                
    def createManuals(self):
        """
        @note: it initialize the manuals for the shell's built-in functions
        """
        
        #creating manuals
        manexe = Manual("execute", "run a program", ["a program"])
        manps = Manual("ps", "displays information about a selection of the active processes.")
        mankill = Manual("kill", "Terminate process with given signal, send a signal to a process", ["a process"])
        manman = Manual("man", "see the manual of a program, utility or function",["a program","an important function","a system's command"])        
        #my manual
        manuals = {manexe.name : manexe, manps.name : manps, mankill.name : mankill, manman.name : manman}
        
        return manuals
        
    def dir_print(self, to_print, impressor=None):
        print (to_print,file=self.console)
        
if __name__ == '__main__':
    shell = Shell()
    shell.start()
        
        
