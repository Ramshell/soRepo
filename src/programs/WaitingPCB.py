from programs.TerminatedPCB import PcbState
class WaitingPCB(PcbState):
    '''
    One of the diferent states of a PCB
    
    @author: Nicolas Leutwyler
    @author: Lucas Sandoval
    @author: Jesus Laime
    '''
    
    def name(self):
        return "waiting"
