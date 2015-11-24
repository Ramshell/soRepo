'''
Created on 23/10/2015

@author: exilio
'''
import unittest
from Device import Device
from Instructions.InstIO import InstIO
from Queue import Queue
from mockito import Mock
from mockito.inorder import verify
import time

class Test(unittest.TestCase):


    def setUp(self):
        self.pcb1 = Mock()
        self.pcb2 = Mock()
        self.interruptor = Mock()
        self.printLine1 = InstIO("Impresion 1", 0)
        self.printLine2 = InstIO("Impresion 2", 0)
        self.queue = Queue()
        self.device = Device("Printer", self.interruptor, self.queue)  # 0 equals to the device cod printer
        
        
    def test_when_process_is_called_the_instruccion_runs_and_ioDone_is_sent(self):
        self.packageOne = [self.pcb1, self.printLine1]
        self.device.proccess(self.packageOne)  # arrange
        
        verify(self.interruptor).ioDone(self.pcb1)  # assert
    
#     def test_when_nothing_to_process_then_waits_2_seconds(self):
#         self.device.start()
#           
#     def test_has_two_instructions_to_process_then_process_them(self):
#         self.packageOne = [self.pcb1,self.printLine1]
#         self.packageTwo = [self.pcb2,self.printLine2]
#         self.queue.put(self.packageOne)
#         self.queue.put(self.packageTwo)
#           
#         self.device.start()
#         time.sleep(10)
#         self.device.stop()

