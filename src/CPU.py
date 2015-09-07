
class CPU:

    def __init__(self, memory):
        self.memory = memory
        
    def run(self, pcb):
        #Caso base termino programa
        if(pcb.getSize()== pcb.getPc()):
            
        #Caso base cpu decide terminar de ejecutar este programa.
            
            self.execute(self.memory.getDir(pcb.getBaseDir()+pcb.getPc()))
            pcb.incrementarPc()
            #caso recursivo
            self.run(pcb)
            
    def __execute(self,instruction):
        instruction.run()

           