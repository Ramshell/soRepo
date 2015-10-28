from multiprocessing.connection import deliver_challenge

class Kernel(object):
    '''
    @summary: the abstraction of the operative system
    '''


    def __init__(self, clock,programLoader,delivery,imanager):
        self.clock = clock
        self.programLoader = programLoader
        self.delivery = delivery
        self.imanager = imanager
        
    def estart(self):
        self.clock.start()
        
    def newDevice(self,device):
        self.delivery.newDevice(device)
        
    def run(self,programName):
        self.pid = self.programLoader.loadProcessWithNoPriority(programName)
        return self.pid
    
    def ps(self):
        self.programLoader.getPcbTable().getPS()
    
    def kill(self,pid):
        self.imanager.kill(pid)
        
        