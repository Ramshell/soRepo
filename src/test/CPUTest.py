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

'''
@author Laime Jesus
@author Leutwyler Nicolas
@author Sandoval Lucas
'''
class CPUTest(unittest.TestCase):

    def setUp(self):
        self.memoria = RAM(65535)

        self.scheduler = Mock()
        self.hdd = Mock()
        self.queue = Mock()
        #self.aPcb = Mock()
        self.interruptor = Mock()
        self.interruptor2 = Mock()
        self.interruptor = InterruptorManager(self.memory,self.scheduler,self.hdd,self.queue)

        self.semaphore = RLock()

        self.cpu = CPU(self.memory,self.interruptor, self.semaphore)
        #self.cpu2= CPU(self.memoria,self.inMan2)
        self.clock = Clock(self.cpu)

        self.instruction1 = InstCPU("Matar a Flanders")
        self.Instruction2 = InstCPU("Y Tambien A Selma")
        self.instructionIO = InstIO("Soy de IO")

        self.memory.putDir(0, self.instruction1)
        self.memory.putDir(1, self.Instruction2)
        self.memory.putDir(2, self.instructionIO)
        self.aPcb = PCB(0,0,3)
        self.cpu.setPCB(self.aPcb)

    def test_when_fetch_then_instruction_valid(self):
        self.expected = self.instruction1 #Arrange

        self.value = self.cpu.fetch(self.aPcb) #Act

        self.assertEquals(self.value , self.expected) #Assert

    def test_when_fetching_third_intruction_then_IO_interruption(self):
        self.expected = self.instructionIO #Arrange

        self.cpu.fetch(self.aPcb)
        self.cpu.fetch(self.aPcb) #Act
        self.cpu.fetch(self.aPcb)

        verify(self.interruptor).ioQueue(aPcb) #Assert

    def test_when_fetching_last_instruction_then_pcbEnd_interruption(self):
        self.anotherPcb = PCB(0,0,2) #The difference with aPcb, is their sizes... Arrange

        self.cpu.fetch(self.anotherPcb) #Act
        self.cpu.fetch(self.anotherPcb)

        verify(self.interruptor).pcbEnd(anotherPcb) #Assert
