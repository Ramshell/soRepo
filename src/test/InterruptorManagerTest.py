import os, sys
src_path = os.path.abspath(os.path.join('..'))
sys.path.append(src_path)

from InterruptorManager import InterruptorManager
import unittest 
from mockito.mocking import Mock
from mockito.mockito import verify

class InterruptorManagerTest(unittest.TestCase):


    def setUp(self):
        self.scheduler = Mock()
        self.disco = Mock()
        self.coladeio = Mock()
        self.ram = Mock()
        self.aPCB = Mock()
        
        self.im = InterruptorManager(self.ram,self.scheduler,self.disco,self.coladeio)
    
    def test_signal_io_pcb (self):
        self.im.ioQueue(self.aPCB)
        
        print("Test 1")
        verify(self.coladeio).put(self.aPCB)
        verify(self.scheduler).setPcbToCPU()
    
    def test_signal_of_pcb_end(self):
        self.im.kill(self.aPCB)
        
        print("Test 2")
        verify(self.ram).clean()
        verify(self.scheduler).setPcbToCPU()
         
    def test_signal_of_timeout(self):
        self.im.pcbQueue(self.aPCB)
        
        verify(self.scheduler).setPcbToCPU()
        verify(self.scheduler).add(self.aPCB)
        
