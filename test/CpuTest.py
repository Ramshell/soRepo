from mockito import *
import unittest
import os, sys
src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from CPU import CPU
from InterruptorManager import InterruptorManager
from RAM import RAM

from PCB import PCB
class CPUTest(unittest.TestCase):


    def setUp(self):
        self.memoryMock = mock()
        self.intmMock = mock()
        self.cpu = CPU(self.memoryMock, self.intmMock)

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