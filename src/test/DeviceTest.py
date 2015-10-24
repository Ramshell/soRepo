'''
Created on 23/10/2015

@author: exilio
'''
import unittest
from Device import Device
from InstIO import InstIO
from Queue import Queue
from mockito import Mock
from mockito.inorder import verify

class Test(unittest.TestCase):


    def setUp(self):
        self.pcb1 = Mock()
        self.pcb2 = Mock()
        self.interruptor = Mock()
        self.printLine1 = InstIO("Impresion 1",0)
        self.printLine2 = InstIO("Impresion 2",0)
        self.queue = Queue()
        self.device = Device("Printer",self.queue,self.interruptor) #0 equals to the device cod printer
    
    def test_when_nothing_to_process_then_waits_2_seconds(self):
        self.device.run()
        self.device.stop()
        
    def test_has_two_instructions_to_process_then_process_them(self):
        self.packageOne = [self.pcb1,self.printLine1]
        self.packageTwo = [self.pcb2,self.printLine2]
        self.queue.put(self.packageOne)
        self.queue.put(self.packageTwo)
        
        self.device.run()