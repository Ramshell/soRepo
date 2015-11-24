import unittest
import itertools
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when

from PCB import PCB

class PCBTest(unittest.TestCase):
    
    def repeat(self,f, N):
        for _ in itertools.repeat(None, N): f()

        
    def test_when_baseDir_is_N_getBaseDir_returns_N(self):
        self.sut = PCB(0,[0],1,0,1,[1])
        self.assertEqual(0, self.sut.getCurrentPage())
        
    def test_when_baseDir_is_N_incrementPc_plus_getPC_returns_N_Because_PCBReady_shuldnt_increment_pc(self):
        self.sut = PCB(0,[0],1)
        self.sut.incrementPc()
        self.assertEqual(0, self.sut.getPc())
        
    def test_when_PCB_isRuning_incrementPC_sums_one_to_the_pc(self):
        self.sut = PCB(0,[0],1)
        self.sut.runing()
        self.sut.incrementPc()
        self.assertEqual(1, self.sut.getPc())
        
    def test_when_PCB_has_size_N_getSize_returns_N(self):
        self.sut = PCB(0,[0],5)
        self.assertEqual(5, self.sut.getSize())
        
    def test_when_size_isEquals_to_pc_then_it_is_Finished(self):
        self.sut = PCB(0,[0],5)
        self.sut.runing()
        self.repeat(self.sut.incrementPc,6)
        self.assertTrue(self.sut.finished())
        
        
        
        
        