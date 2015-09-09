from InterruptorManager import InterruptorManager

class CPU:

    def __init__(self, memory,interruptionManager,execTimes):
        self.memory = memory
        self.interruptionManager = interruptionManager
        
    def run(self, pcb, times):
        
        
        instruction = self.fetch(pcb)
        if(instruction.isIO()):
            self.interruptorManager.ioQueue(pcb)
            #CPU OCIOSA que avisa que espera pcb
        
        #SI LLEGO ACA ES DE CPU
        self.execute(instruction)
        pcb.incrementPc()
        
        times = times -1
        
        if(pcb.finished()):
            #SI EL PROGRAMA TERMINO
            self.interruptionManager.pcbEnd(pcb)
            #CPU OCIOSA que avisa que espera pcb
            
        if (times<=0):
            self.interruptionManager.pcbQueue(pcb)
            #CPU OCIOSA que avisa que espera pcb
            
        self.run(pcb,times)    
            
    def __fetch(self,pcb):
        return self.memory.getDir(pcb.getBaseDir() + pcb.getPc())
            
    def __execute(self, instruction):
        instruction.run()

           
