

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
        if not name in self.programs:
            #raise Exception('ProgramTest not found')
            return None
        return self.programs[name]
    
    def setProgram(self, program):
        self.programs[program.name] = program

    def deleteProgram(self, name):
        del self.programs[name]
    
    