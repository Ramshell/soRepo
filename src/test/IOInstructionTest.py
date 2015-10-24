import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when

from InstIO import InstIO

class IOInstructionTest(unittest.TestCase):
	
		def setUp(self):
			self.ioInst = InstIO("Instruccion de impresora",0)
			
		def test_when_create_an_io_instruction_then_inheritance_works(self):
			self.instruction = self.ioInst #ARRANGE
			
			self.expected = 0 #ACT
			
			self.assertEquals(self.instruction.codDevice , self.expected) #ASSERT
		