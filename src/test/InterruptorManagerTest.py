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
        
        self.imanager = InterruptorManager(self.ram,self.scheduler,self.disco,self.iodelivery)
    
    def test_when_signal_ioQueue_then_IM_puts_the_pcb_in_the_ioQueue (self):
        self.imanager.ioQueue(self.data,self.cod)

        verify(self.iodelivery).putInQueue(self.data,self.cod)
        verify(self.scheduler).setPcbToCPU()
    
    def test_when_kill_signal_then_cleans_the_memory(self):
        self.imanager.kill(self.aPCB)
        
        verify(self.ram).clean(self.aPCB)
        verify(self.scheduler).setPcbToCPU()
         
    def test_when_timeout_signal_then_the_pcb_is_added_to_the_readyQueue_again(self):
        self.imanager.timeOut(self.aPCB)
        
        verify(self.scheduler).setPcbToCPU()
        verify(self.scheduler).add(self.aPCB)
        
