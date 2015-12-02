'''
Created on 10 de nov. de 2015

@author: ramshell
'''
from threading import *
import unittest

from mainHardwareModules import CPU.CPU
from Instructions.Assembly import *
from Instructions.InstIO import InstIO
from Manual import Manual
from PCB import PCB
from Program import Program
from storage import RAM.RAM
from clock import Clock
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
from memoryManagement.MMU import MMU


class Test(unittest.TestCase):
    
    
    
    def setUp(self):
        self.factorial = Program("factorial")
        
        self.instFactorial1 = MovLiteral(1, 1)
        self.instFactorial2 = MovLiteral(2, 1)
        self.instFactorial3 = CmpLiteral(0, 1)
        self.instFactorial4 = Jle(4)
        self.instFactorial5 = Mul(1, 2)
        self.instFactorial6 = AddLiteral(2, 1)
        self.instFactorial7 = AddLiteral(0, -1)
        self.instFactorial8 = Jmp(2)
        self.instFactorial9 = InstCPU("aca deberia imprimir el resultado")
        
        self.factorial.addInstruction(self.instFactorial1)
        self.factorial.addInstruction(self.instFactorial2)
        self.factorial.addInstruction(self.instFactorial3)
        self.factorial.addInstruction(self.instFactorial4)
        self.factorial.addInstruction(self.instFactorial5)
        self.factorial.addInstruction(self.instFactorial6)
        self.factorial.addInstruction(self.instFactorial7)
        self.factorial.addInstruction(self.instFactorial8)
        self.factorial.addInstruction(self.instFactorial9)
        
        self.memory = RAM(65535)
        self.mmu = MMU(11,self.memory)
        self.memory.putDir(0,self.instFactorial1)
        self.memory.putDir(1,self.instFactorial2)
        self.memory.putDir(2,self.instFactorial3)
        self.memory.putDir(3,self.instFactorial4)
        self.memory.putDir(4,self.instFactorial5)
        self.memory.putDir(5,self.instFactorial6)
        self.memory.putDir(6,self.instFactorial7)
        self.memory.putDir(7,self.instFactorial8)
        self.memory.putDir(8,self.instFactorial9)
        self.memory.putDir(11,5)
        self.pcb = PCB(0,[0],self.factorial.size(),0,11,[1])
        self.pcb.runing()
        
        self.interruptor = Mock()

        self.semaphore = RLock()


        self.cpu = CPU(self.memory,self.interruptor, self.semaphore,self.mmu)


    def test_factorial_gives_the_correct_value(self):
        self.cpu.setPCB(self.pcb)
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.cpu.tick()
        self.assertEqual(self.memory.getDir(8),self.instFactorial9 )
        self.assertEqual(self.memory.getDir(12),24 )

        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
