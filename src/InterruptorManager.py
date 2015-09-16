

class InterruptorManager:
  
    
    def __init__(self,memory,scheduler,hdd,ioQueue):
        self.memory = memory
        self.schPCB = scheduler
        self.io = ioQueue
        self.hdd = hdd
        
    def ioQueue(self,pcb):
        self.io.add(pcb)
        self.schPCB.freeCpu()
        
    def pcbEnd(self,pcb):
        self.memory.clean()
        self.schPCB.freeCpu()
        
    def pcbQueue(self,pcb):
        self.schPCB.add(pcb)
        self.schPCB.freeCpu()
    
    
#im = InterruptorManager    
#im.register(self, "#KILL", new KillHandler() ):
#im.register(self, "#IO", new IOHandler() ):
    
# cpu = new CPU (im)           
#    im.interrupt("#KILL", pcb) 
    
 #   
#    KillHandle.handle(pcb)  
#      //hace lo que sabe hacer
            
        
    
