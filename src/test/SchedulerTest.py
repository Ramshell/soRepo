
import unittest
import itertools
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
from Scheduler import *
from PCB import *
from threading import Condition
from OwnHeap import OwnHeap

class TestSchedulerPriorityRoundRobin(unittest.TestCase):
    
    def repeat(self, f, N):
        for _ in itertools.repeat(None, N): f()

    def setUp(self):
        
        
        self.comparator = lambda pcb1, pcb2: pcb1.getPriority() > pcb2.getPriority()  # the greater, the better
        self.semaphore = Mock()
        self.myCpu = Mock()
        self.queue = OwnHeap(self.semaphore, self.comparator)
        self.myScheduler = Scheduler(self.myCpu, self.queue, 1, self.semaphore)  # Priority Round Robin
        self.highPriorityPCB = PCB(1, 1, 5, 10)
        self.higherPriorityPCB = PCB(1, 1, 5, 15)  
        self.lowPriorityPCB = PCB(2, 6, 5, 1)
        self.queue.put(self.highPriorityPCB)
        self.queue.put(self.higherPriorityPCB)
        self.queue.put(self.lowPriorityPCB)
                
                
    def test_when_the_cpu_is_free_then_the_scheduler_set_the_pcb_with_the_higher_priority(self):
        self.myScheduler.setPcbToCPU()
        verify(self.myCpu).setPCB(self.higherPriorityPCB)
        
        
    def test_when_a_pcb_is_assingned_the_burst_is_assigned_too(self):
        self.myScheduler.setPcbToCPU()
        self.burstExpected = self.higherPriorityPCB.getBurst()
        self.assertEqual(1, self.burstExpected)
        
    def test_when_the_queue_is_empty_it_waits_until_it_is_refilled(self):
        try:
            self.repeat(self.myScheduler.setPcbToCPU, 3)
            self.myScheduler.setPcbToCPU()
            verify(self.semaphore).wait()
        except Exception:
            pass
        else:
            self.fail("unsexpected exception")

            
        
        


