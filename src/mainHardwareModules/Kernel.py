from devices.Device import Device


class Kernel(object):
    '''
    @summary: the abstraction of the operative system
    '''


    def __init__(self, clock,programLoader,imanager,delivery,devices=[]):
        self.clock = clock
        self.programLoader = programLoader
        self.delivery = delivery
        self.imanager = imanager
        self.devices = devices
        
    def startUp(self):
        self.clock.start()
        for device in self.devices:
            device.start()
        
    def run(self,programName,priority=0,args=[]):
        self.pid = self.programLoader.loadProcess(programName,priority,args)
        return self.pid
    
    def ps(self):
        return self.programLoader.getPcbTable().getPS()
    
    def kill(self,pid):
        self.imanager.kill(pid)
    
    def installNewDevice(self,deviceName,deviceLogger):
        self.device = Device(deviceName,self.imanager)
        self.device.setLogger(deviceLogger)
        self.delivery.newDevice(self.device)
        self.devices.append(self.device)
        
    def manual(self,programName):
        return self.programLoader.manual(programName)
        
    def in_disk(self, programName):
        return self.programLoader.in_disk(programName)
        

        

        
        