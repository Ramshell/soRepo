import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
import os, sys
src_path = os.path.abspath(os.path.join('..'))
sys.path.append(src_path)
from PCB import PCB

class MyClass(unittest.TestCase):

        
    def test_when_baseDir_is_N_getBaseDir_returns_N(self):
        self.sut = PCB(0,0,1)
        self.assertEqual(0, self.sut.getBaseDir())
        
    def test_when_baseDir_is_N_incrementPc_plus_getBaseDir_returns_N_Because_PCBReady_shuldnt_increment_pc(self):
        self.sut = PCB(0,0,1)
        self.sut.incrementPc()
        self.assertEqual(0, self.sut.getBaseDir())
    
        