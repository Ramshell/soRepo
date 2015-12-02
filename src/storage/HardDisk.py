    
    

class HardDisk(object):
    """
    @summary  it represents the abstraction of a hardware component called "Hard Disk Drive", which has the responsibility of save and maintain programs and data
    """
    

    def __init__(self):
        """
        Constructor
        """
        self.programs = {}
    
    def getProgram(self, name):
        '''
        @param name: the name of the program to try to fetch 
        @return: it return None if name is not found else it return program called name
        '''
        if not name in self.programs:
            #raise Exception('ProgramTest not found')
            return None
        return self.programs[name]
    
    def setProgram(self, program):
        """
        @param program: should be a new program to add 
        """
        self.programs[program.name] = program

    def deleteProgram(self, name):
        """
        @param name: it should be the name of the program to delete
        """
        del self.programs[name]
    
    