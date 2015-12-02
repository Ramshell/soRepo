class TableOfPCB:

    def __init__(self):
        self.table = []
        
    def delete(self, pcb):
        self.removePcb(pcb)
        
    def addPCB(self, pcb,name):
        self.table.append(PcbWithName(pcb,name))
        
    def contains(self, pcb):
        return self.table.count(pcb) > 0
    
    def getPCB(self, pid):
        res = None
        for pcbWithName in self.table:
            if pcbWithName.pcb.getPid() == int(pid):
                res = pcbWithName.pcb
        return res
        
    def getPS(self):
        for pcbWithName in self.table:
            pcbWithName.getInfo()
            
    def countActiveProcess(self):
        return len(self.table)
    
    def getProgramName(self,pid):
        res = None
        for pcbWithName in self.table:
            if pcbWithName.pcb.getPid() == pid:
                res = pcbWithName
        if res is None:
            return res
        else:
            return res.getName()
        
    def removePcb(self,pcb):
        for pcbWithName in self.table:
            if pcbWithName.getPid() == pcb.getPid():
                self.table.remove(pcbWithName)
                break
    
        
class PcbWithName:
    def __init__(self,pcb,name):
        self.pcb = pcb
        self.name = name
        
    def getName(self):
        return self.name
    
    def getPid(self):
        return self.pcb.getPid()
        
    def getInfo(self):
        print "Program: {} Pid: {} PC: {} Priority: {} State: {} ".format(self.name ,self.pcb.getPid(), self.pcb.getPc(), self.pcb.getPriority(), self.pcb.getState())
    
    