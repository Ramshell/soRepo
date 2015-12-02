from programs.TerminatedPCB import PcbState
class RuningPCB(PcbState):

    def incrementarPC(self, unPCB):
        unPCB.pc = unPCB.pc + 1

    def name(self):
        return "runing"
