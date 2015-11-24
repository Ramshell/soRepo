'''
Created on 10 de nov. de 2015

@author: ramshell
'''
from threading import *
import unittest

from CPU import CPU
from Instructions.Assembly import *
from Instructions.InstIO import InstIO
from Manual import Manual
from PCB import PCB
from Program import Program
from RAM import RAM
from clock import Clock
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
from memoryManagement.MMU import MMU


class Test(unittest.TestCase):
    
    
    
    def setUp(self):
        self.fibbo = Program("fibbo")
        # the relative position 0 has the n
        self.instrFibbo1 = MovLiteral(1, 1)
        self.instrFibbo2 = MovLiteral(2, 1)
        self.instrFibbo3 = CmpLiteral(0, 1)
        self.instrFibbo4 = Jle(5)
        self.instrFibbo5 = Mul(1, 2)
        self.instrFibbo6 = AddLiteral(2, 1)
        self.instrFibbo7 = AddLiteral(0, -1)
        self.instrFibbo8 = Jmp(2)
        self.instrFibbo9 = ScreenPrint("printeando el resultado")
        
        self.fibbo.addInstruction(self.instrFibbo1)
        self.fibbo.addInstruction(self.instrFibbo2)
        self.fibbo.addInstruction(self.instrFibbo3)
        self.fibbo.addInstruction(self.instrFibbo4)
        self.fibbo.addInstruction(self.instrFibbo5)
        self.fibbo.addInstruction(self.instrFibbo6)
        self.fibbo.addInstruction(self.instrFibbo7)
        self.fibbo.addInstruction(self.instrFibbo8)
        self.fibbo.addInstruction(self.instrFibbo9)
        
        self.memory = RAM(65535)
        self.mmu = MMU(10,self.memory)
        self.memory.putDir(0,self.instrFibbo1)
        self.memory.putDir(1,self.instrFibbo2)
        self.memory.putDir(2,self.instrFibbo3)
        self.memory.putDir(3,self.instrFibbo4)
        self.memory.putDir(4,self.instrFibbo5)
        self.memory.putDir(5,self.instrFibbo6)
        self.memory.putDir(6,self.instrFibbo7)
        self.memory.putDir(7,self.instrFibbo8)
        self.memory.putDir(8,self.instrFibbo9)
        self.memory.putDir(10,5)
        self.pcb = PCB(0,[0],self.fibbo.size(),0,10,[1])
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

        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
