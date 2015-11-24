class TableOfPCB(object):

    def __init__(self):
        self.table = []
        
    def delete(self, pcb):
        self.table.remove(pcb)
        
    def addPCB(self, pcb):
        self.table.append(pcb)
        
    def contains(self, pcb):
        return self.table.count(pcb) > 0
    
    def getPCB(self, pid):
        for pcb in self.table:
            if pcb.getPid() == pid:
                return pcb
        return None
        
    def getPS(self):
        for pcb in self.table:
            # print(pcb.getPid(),"",pcb.getState(),"",pcb.getPC()," This is the priority",pcb.getPriority())
            print "Pid: {} PC: {} Priority: {} State: {} ".format(pcb.getPid(), pcb.getPc(), pcb.getPriority(), pcb.getState())

    def countActiveProcess(self):
        return len(self.table)
    
        
