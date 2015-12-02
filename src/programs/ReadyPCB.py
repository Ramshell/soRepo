'''
One of the diferent states of a PCB

@author: Nicolas Leutwyler
@author: Lucas Sandoval
@author: Jesus Laime
'''
from programs.TerminatedPCB import PcbState
class ReadyPCB(PcbState):
    
    def name(self):
        return "ready"
