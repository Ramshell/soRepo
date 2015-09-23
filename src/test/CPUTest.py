import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
import os, sys
from ProgramLoader import ProgramLoader
src_path = os.path.abspath(os.path.join('..'))
sys.path.append(src_path)
from RAM import RAM
from InterruptorManager import InterruptorManager
from InstIO import InstIO
from InstCPU import InstCPU
from Instruction import Instruction
from Program import Program
from CPU import CPU
from PCB import PCB

class CPUTest(unittest.TestCase):

    def setUp(self):
        self.memoria = RAM(65535)
        self.sche = Mock()
        self.disco = Mock()
        self.cola = Mock()
        self.thePcb = Mock()
        self.inMan2 = Mock()
        
        self.inMan = InterruptorManager(self.memoria,self.sche,self.disco,self.cola)
        self.cpu = CPU(self.memoria,self.inMan)
        self.cpu2= CPU(self.memoria,self.inMan2)
        
        self.inst1 = InstCPU("Matar a Flanders")
        self.inst2 = InstCPU("Y Tambien A Selma")
        self.instIO = InstIO("Soy de IO")
        self.memoria.putDir(0, self.inst1)
        self.memoria.putDir(1, self.inst2)
        self.memoria.putDir(2, self.instIO)

        self.unPcb = PCB(0,0,2)
        
    def test_de_un_fetch(self):
        
        self.expected = self.cpu.fetch(self.unPcb)
        
        self.assertEquals(self.expected , self.inst1)
        
    def test_of_a_run_with_pcb_finished(self):
        
        when(self.thePcb).finished().thenReturn(True)
        when(self.thePcb).getBaseDir().thenReturn(0)
        when(self.thePcb).getPc().thenReturn(1)
        self.cpu2.run(self.thePcb,2)
        
        verify(self.inMan2).pcbEnd(self.thePcb)
        
   # def test_of_a_run_with_IO_exception(self):    
  #      
   #     when(self.thePcb).finished().thenReturn(True)
      #  when(self.thePcb).getBaseDir().thenReturn(0)
      #  when(self.thePcb).getPc().thenReturn(1)
     #   self.cpu2.run(self.thePcb,2)