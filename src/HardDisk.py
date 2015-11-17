

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
        #return self.programs.get(name)
        if self.no_exists(name):
            #raise Exception('ProgramTest not founded')
            return None
        return self.programs[name]
    
    def setProgram(self,program):
        self.programs[program.name] = program
        
    def no_exists(self,name):
        self.prog = self.programs.get(name)
        return self.prog is None
    
    def deleteProgram(self, name):
        del self.programs[name]
    