
import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
from Scheduler import *
from PCB import *
from threading import RLock

class Test(unittest.TestCase):

    def setUp(self):
        
        self.semaphore = RLock()
        self.myCpu = Mock()
        self.myScheduler = Scheduler(self.myCpu,self.semaphore)
        self.myScheduler.setPriorityAndRoundRobin(1)
        self.highPriorityPCB = PCB( 1, 1, 5, 10)
        self.higherPriorityPCB = PCB( 1, 1, 5, 15)  
        self.lowPriorityPCB = PCB( 2, 6, 5, 1)
        self.myScheduler.addPcb(self.highPriorityPCB)
        self.myScheduler.addPcb(self.higherPriorityPCB)
        self.myScheduler.addPcb(self.lowPriorityPCB)
                
                
    def test_when_the_cpu_is_free_then_the_scheduler_set_the_pcb_with_the_higher_priority(self):
        self.myScheduler.setPcbToCPU()
        verify(self.myCpu).setPCB(self.higherPriorityPCB)
        
        
    def testOtra(self):
        print("testOtra")
        
    def testRealmenteOtra(self):
        print("testRealmenteOtra")


