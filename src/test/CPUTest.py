import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from storage.RAM import RAM
from threading import RLock
from Instructions.InstIO import InstIO
from Instructions.InstCPU import InstCPU
from mainHardwareModules.CPU import CPU
from programs.PCB import PCB
from mainHardwareModules.clock import Clock
from memoryManagement.MMU import MMU, Page

'''
@author Laime Jesus
@author Leutwyler Nicolas
@author Sandoval Lucas
'''



class CPUTest(unittest.TestCase):

    def setUp(self):
        self.memory = RAM(65535)
        self.mmu = MMU(1,self.memory)

        self.scheduler = Mock()
        self.hdd = Mock()
        self.queue = Mock()
        self.interruptor2 = Mock()
        self.interruptor = Mock()
        self.logger = Mock()

        self.semaphore = RLock()

        self.cpu = CPU(self.memory,self.interruptor, self.semaphore,self.mmu)
        self.cpu.setLogger(self.logger)
        self.clock = Clock(self.cpu)

        self.mov = InstCPU("Matar a Flanders")
        self.Instruction2 = InstCPU("Y Tambien A Selma")
        self.instructionIO = InstIO("Soy de IO", 0)

        self.memory.putDir(0, self.mov)
        self.memory.putDir(1, self.Instruction2)
        self.memory.putDir(2, self.instructionIO)
        page0 = Page(0)
        page1 = Page(1)
        page2 = Page(2)
        page0.changeMemoryFlag()
        page1.changeMemoryFlag()
        page2.changeMemoryFlag()
        self.aPcb = PCB(0,[page0,page1,page2],3,4,1,[Page(123)])
        

    def test_when_fetch_then_instruction_valid(self):
        self.expected = self.mov  # Arrange
        self.cpu.setPCB(self.aPcb)

        self.value = self.cpu.fetch()  # Act

        self.assertEquals(self.value , self.expected)  # Assert

    def test_when_fetching_third_intruction_then_IO_interruption(self):
        self.aPcb.runing()
        self.cpu.setPCB(self.aPcb) 
        self.data = [self.aPcb , self.instructionIO] 
        self.cod = 0  # Arrange

        self.cpu.tick()
        self.cpu.tick()  # Act
        self.cpu.tick()

        verify(self.interruptor).ioQueue(self.data, self.cod)  # Assert

    def test_when_fetching_last_instruction_then_pcbEnd_interruption(self):
        page0 = Page(0)
        page1 = Page(1)
        page0.changeMemoryFlag()
        page1.changeMemoryFlag()
        self.anotherPcb = PCB(0,[page0,page1],2,4,1,[123]) #The difference with aPcb, are their sizes... Arrange
        self.anotherPcb.runing()
        self.cpu.setPCB(self.anotherPcb)

        self.cpu.tick()  # Act
        self.cpu.tick()
        self.cpu.tick()

        verify(self.interruptor, 1).kill(self.anotherPcb.getPid())  # Assert
