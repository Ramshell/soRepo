'''
Created on 13 de oct. de 2015

@author: ramshell
'''

class TableOfPCB(object):

    def __init__(self):
        self.table = []
        
    def delete(self, pcb):
        self.table.remove(pcb)
        
    def addPCB(self, pcb):
        self.table.append(pcb)
        
    def contains(self,pcb):
        return self.table.count(pcb)> 0
        
    def getPS(self):
        for pcb in self.table:
            #print(pcb.getPid(),"",pcb.getState(),"",pcb.getPC()," This is the priority",pcb.getPriority())
            print "Pid: {} PC: {} Priority: {} State: {} ".format(pcb.getPid(), pcb.getPc(), pcb.getPriority(), pcb.getState())
        