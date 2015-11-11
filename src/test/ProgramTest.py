'''
Created on 10 de nov. de 2015

@author: ramshell
'''
import unittest
from Program import Program
from Instructions.Assembly import *
from Manual import Manual
from InstIO import InstIO
from RAM import RAM
from PCB import PCB
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
from threading import *
from CPU import CPU
from clock import Clock


class Test(unittest.TestCase):
    
    
    
    def setUp(self):
        self.fibbo = Program("fibbo")
        #the relative position 0 has the n
        self.instrFibbo1 = MovLiteral(1,1)
        self.instrFibbo2 = MovLiteral(2,1)
        self.instrFibbo3 = CmpLiteral(0,1)
        self.instrFibbo4 = Jle(5)
        self.instrFibbo5 = Mul(1,2)
        self.instrFibbo6 = AddLiteral(2,1)
        self.instrFibbo7 = AddLiteral(0,-1)
        self.instrFibbo8 = Jmp(2)
        self.instrFibbo9 = InstIO("printeando el resultado",0)
        
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
        self.memory.putDir(0,self.instrFibbo1)
        self.memory.putDir(1,self.instrFibbo2)
        self.memory.putDir(2,self.instrFibbo3)
        self.memory.putDir(3,self.instrFibbo4)
        self.memory.putDir(4,self.instrFibbo5)
        self.memory.putDir(5,self.instrFibbo6)
        self.memory.putDir(6,self.instrFibbo7)
        self.memory.putDir(7,self.instrFibbo8)
        self.memory.putDir(8,self.instrFibbo9)
        self.memory.putDir(9,5)
        self.pcb = PCB(0,0,self.fibbo.size())
        self.pcb.runing()
        self.instrFibbo1.setCurrentPosition(9, self.memory)
        self.instrFibbo2.setCurrentPosition(9, self.memory)
        self.instrFibbo3.setCurrentPosition(9, self.memory,self.pcb)
        self.instrFibbo4.setCurrentPosition(9, self.pcb)
        self.instrFibbo5.setCurrentPosition(9, self.memory)
        self.instrFibbo6.setCurrentPosition(9, self.memory)
        self.instrFibbo7.setCurrentPosition(9, self.memory)
        self.instrFibbo8.setCurrentPosition(9, self.pcb)
        
        self.interruptor = Mock()

        self.semaphore = RLock()

        self.cpu = CPU(self.memory,self.interruptor, self.semaphore)
        self.clock = Clock(self.cpu)

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
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()