import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when

from threading import *

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
        self.memory = RAM(65535)

        self.scheduler = Mock()
        self.hdd = Mock()
        self.queue = Mock()
        #self.aPcb = Mock()
        self.interruptor = Mock()
        self.interruptor2 = Mock()
        self.interruptor = Mock()

        self.semaphore = RLock()

        self.cpu = CPU(self.memory,self.interruptor, self.semaphore)
        #self.cpu2= CPU(self.memoria,self.inMan2)
        self.clock = Clock(self.cpu)

        self.instruction1 = InstCPU("Matar a Flanders")
        self.Instruction2 = InstCPU("Y Tambien A Selma")
        self.instructionIO = InstIO("Soy de IO",0)

        self.memory.putDir(0, self.instruction1)
        self.memory.putDir(1, self.Instruction2)
        self.memory.putDir(2, self.instructionIO)
        self.aPcb = PCB(0,0,3,4)
        

    def test_when_fetch_then_instruction_valid(self):
        self.expected = self.instruction1 #Arrange

        self.value = self.cpu.fetch() #Act

        self.assertEquals(self.value , self.expected) #Assert

    def test_when_fetching_third_intruction_then_IO_interruption(self):
        self.aPcb.runing()
        self.cpu.setPCB(self.aPcb) 
        self.data = [self.aPcb , self.instructionIO] 
        self.cod = 0 #Arrange

        self.cpu.tick()
        self.cpu.tick() #Act
        self.cpu.tick()

        verify(self.interruptor).ioQueue(self.data,self.cod) #Assert

    def test_when_fetching_last_instruction_then_pcbEnd_interruption(self):
        self.anotherPcb = PCB(0,0,2,4) #The difference with aPcb, are their sizes... Arrange
        self.anotherPcb.runing()
        self.cpu.setPCB(self.anotherPcb)

        self.cpu.tick() #Act
        self.cpu.tick()

        verify(self.interruptor).kill(self.anotherPcb) #Assert
