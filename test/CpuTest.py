import unittest
from CPU import CPU
from InterruptorManager import InterruptorManager
from RAM import RAM
from mock import Mock
from PCB import PCB
class CPUTest(unittest.TestCase):


    def setUp(self):
        self.memoryMock = Mock()
        self.intmMock = Mock()
        self.cpu = CPU(self.memoryMock, self.intmMock, 1)

    def testProbarRunWithOneInstruction(self):
        #Sabemos que el pc empieza en la instruccion 1 y termina en la 
        #instruccion 2 dado que su length es 1
        self.pcb = PCB(1,1,1)
        self.cpu.run(self.pcb, 10)
        
    
    
    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()