
from InterruptorManager import InterruptorManager 
from RAM import RAM
from CPU import CPU
from PCB import PCB
import unittest 

class Test(unittest.TestCase):


    def setUp(self):
        pcb = PCB(1,1,2)
        coladeprocesos = [pcb]
        ram = RAM(65535)#16bit
        ram.getMemoryScope()
        im = InterruptorManager()
        cpu = CPU(RAM, im)
        

        
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()