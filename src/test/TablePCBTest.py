from StringIO import StringIO
import os, sys
import unittest

from programs.PCB import PCB
from programs.TableOfPcb import TableOfPCB
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when


class TablePCBTest(unittest.TestCase):


    def setUp(self):
        self.pcb1 = PCB(1, 1, 1, 8)
        self.pcb2 = PCB(2, 4, 3, 9)
        self.pcb3 = PCB(3, 7, 6, 13)
        self.pcb4 = PCB(4, 9, 8, 17)
        
    def test_when_delete_a_pcb_then_pcb_is_no_longer_in_the_table(self):
        self.sut = TableOfPCB()
        self.sut.addPCB(self.pcb1)
        self.sut.delete(self.pcb1)
        self.assertTrue(not self.sut.contains(self.pcb1))
        
    def test_getPS_prints_the_correct_values(self):
        
        self.sut = TableOfPCB()
        self.sut.addPCB(self.pcb1)
        self.sut.addPCB(self.pcb2)
        self.sut.addPCB(self.pcb3)
        self.sut.addPCB(self.pcb4)
        self.saved_stdout = sys.stdout
        self.out = StringIO()
        sys.stdout = self.out
        self.sut.getPS()
        self.output = self.out.getvalue().strip()
        self.assertEquals(self.output, 'Pid: 1 PC: 0 Priority: 8 State: ready \nPid: 2 PC: 0 Priority: 9 State: ready \nPid: 3 PC: 0 Priority: 13 State: ready \nPid: 4 PC: 0 Priority: 17 State: ready')

        
