import unittest 

from mainHardwareModules.InterruptorManager import InterruptorManager
from mockito.mocking import Mock
from mockito.mockito import verify, when


class InterruptorManagerTest(unittest.TestCase):


    def setUp(self):
        self.scheduler = Mock()
        self.cpu = Mock()
        self.disco = Mock()
        self.condition = Mock()
        self.pcbTable = Mock()
        
        self.iodelivery = Mock()
        self.ram = Mock()
        self.aPCB = Mock()
        when(self.pcbTable).getPCB(0).thenReturn(self.aPCB)
        self.cod = 4
        self.data = [self.aPCB, self.cod]
        
        self.imanager = InterruptorManager(self.ram, self.scheduler, self.disco, self.iodelivery, self.condition, self.pcbTable)
    
    def test_when_signal_ioQueue_then_IM_puts_the_pcb_in_the_ioQueue (self):
        self.imanager.ioQueue(self.data, self.cod)

        verify(self.iodelivery).putInQueue(self.data, self.cod)
        verify(self.scheduler).setPcbToCPU()
    
    def test_when_kill_signal_then_cleans_the_memory(self):
        when(self.cpu).enable().thenReturn(None)
        when(self.scheduler).getCpu().thenReturn(self.cpu)
        self.imanager.kill(0)
        verify(self.pcbTable).delete(self.aPCB)
        verify(self.ram).clean(self.aPCB)
         
    def test_when_timeout_signal_then_the_pcb_is_added_to_the_readyQueue_again(self):
        self.imanager.timeOut(self.aPCB)
        
        verify(self.scheduler).expropiate()
        verify(self.scheduler).setPcbToCPU()
        verify(self.scheduler).put(self.aPCB)
        
