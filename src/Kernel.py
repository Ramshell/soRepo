from multiprocessing.connection import deliver_challenge
from Device import Device


class Kernel(object):
    '''
    @summary: the abstraction of the operative system
    '''


    def __init__(self, clock,programLoader,imanager,delivery):
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
    
    def installNewDevice(self,deviceName):
        self.device = Device(deviceName,self.imanager)
        self.delivery.newDevice(self.device)
        
        

        

        
        