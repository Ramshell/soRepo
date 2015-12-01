from threading import Thread
import time
from CPU import CPU

class Clock(Thread):
    '''
    Object that manages how to redirect data packages to all devices installed on OS.
    
    @author: Nicolas Leutwyler
    @author: Lucas Sandoval
    @author: Jesus Laime
    '''

    def __init__(self, cpu):
        '''
        Constructor del reloj
        
        @param cpu: CPU asociada, con quien va a interactuar
        '''
        Thread.__init__(self)
        self.cpu = cpu


    def run(self):
        '''
        Interaccion con la cpu, cada cierto tiempo seteado, impulsa el ciclo de ejecucion
        '''
        while(True):
            self.cpu.tick()
            time.sleep(1)
