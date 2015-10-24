import unittest 
from mockito.mocking import Mock
from mockito.mockito import verify, when
from InterruptorManager import InterruptorManager
from twisted.internet.test.test_serialport import DoNothing

class InterruptorManagerTest(unittest.TestCase):


    def setUp(self):
        self.scheduler = Mock()
        self.disco = Mock()
        self.iodelivery = Mock()
        self.ram = Mock()
        self.aPCB = Mock()
        self.cod = 4
        self.data = [self.aPCB,self.cod]
        
        self.im = InterruptorManager(self.ram,self.scheduler,self.disco,self.iodelivery)
    
    def test_signal_io_pcb (self):
        self.im.ioQueue(self.data,self.cod)

        verify(self.iodelivery).putInQueue(self.data,self.cod)
        verify(self.scheduler).setPcbToCPU()
    
    def test_signal_of_pcb_end(self):
        self.im.kill(self.aPCB)
        
        verify(self.ram).clean()
        verify(self.scheduler).setPcbToCPU()
         
    def test_signal_of_timeout(self):
        self.im.timeOut(self.aPCB)
        
        verify(self.scheduler).setPcbToCPU()
        verify(self.scheduler).add(self.aPCB)
        
