from abc import abstractmethod

class PcbState:
    def __init__(self):
        pass
    
    def incrementarPC(self, unPCB):
        pass
    
    @abstractmethod
    def name(self):
        pass
    
    def isTerminated(self):
        return False



class TerminatedPCB(PcbState):
    '''
    it represents a finished pcb
    '''

    
    def name(self):
        return "terminated"
    
    def isTerminated(self):
        return True
        