import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
import os, sys
from threading import *

src_path = os.path.abspath(os.path.join('..'))
sys.path.append(src_path)
from ProgramLoader import ProgramLoader
from RAM import RAM
from InterruptorManager import InterruptorManager
from InstIO import InstIO
from InstCPU import InstCPU
from Instruction import Instruction
from Program import Program
from CPU import CPU
from PCB import PCB
from clock import Clock


class CPUTest(unittest.TestCase):

    def setUp(self):
        self.memoria = RAM(65535)

        self.sche = Mock()
        self.disco = Mock()
        self.cola = Mock()
        self.thePcb = Mock()
        self.inMan2 = Mock()
        self.inManMock = Mock() 
        self.inMan = InterruptorManager(self.memoria,self.sche,self.disco,self.cola)
        
        self.semaphore = RLock()
        
        self.cpu = CPU(self.memoria,self.inManMock, self.semaphore)
        #self.cpu2= CPU(self.memoria,self.inMan2)
        self.clock = Clock(self.cpu)
        
        self.inst1 = InstCPU("Matar a Flanders")
        self.inst2 = InstCPU("Y Tambien A Selma")
        self.instIO = InstIO("Soy de IO")
        
        self.memoria.putDir(0, self.inst1)
        self.memoria.putDir(1, self.inst2)
        self.memoria.putDir(2, self.instIO)
        self.unPcb = PCB(0,0,2)
        self.cpu.setPCB(self.unPcb)


    def test_clock_working_with_two_instructions(self):
        self.clock.run()
        #assert de que termino el pcb en uestion
        #when(self.inManMock).pcbEnd().then(self.clock)


   # def test_of_a_run_with_IO_exception(self):
  #
   #     when(self.thePcb).finished().thenReturn(True)
      #  when(self.thePcb).getBaseDir().thenReturn(0)
      #  when(self.thePcb).getPc().thenReturn(1)
     #   self.cpu2.run(self.thePcb,2)
