

class InterruptorManager:
  
    
    def __init__(self, cpu):
        self.cpu = cpu  # lo estoy observando
        
    def run(self, pcb):
        # Caso base termino programa
        if(pcb.getSize() == pcb.getPc()):
            
        # Caso base cpu decide terminar de ejecutar este programa.
            
            self.execute(self.memory.getDir(pcb.getBaseDir() + pcb.getPc()))
            pcb.incrementarPc()
            # caso recursivo
            self.run(pcb)
            
        
    
