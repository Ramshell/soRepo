

class HardDisk(object):
    '''
    @summary: it represents the abstraction of a hardware component called "Hard Disk Drive", which has the responsibility of save and maintain programs and data
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.programs = {}
    
    def getProgram(self, name):
        
        if self.exists(name):
            raise Exception('ProgramTest not founded')
        self.prog = self.programs[name]
        return self.prog
    
    def setProgram(self,program):
        self.programs[program.name] = program
        
    def exists(self,name):
        self.prog = self.programs[name]
        return self.prog is None
    
    def deleteProgram(self, name):
        del self.programs[name]
    