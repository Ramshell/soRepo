
import unittest
from RAM import RAM
from Assembly import Mov
from Instructions.Assembly import MovLiteral
class Test(unittest.TestCase):


    def setUp(self):
        self.memory = RAM(65535)
        self.memory.putDir(0, 4)
        self.memory.putDir(1, 5)
        self.instruction1 = Mov("this is my very first instruction",0,1)
        self.instruction2= MovLiteral("this is my very first instruction",0,78)
        
    def test_when_move_the_value_from_1_to_0_then_the_cell_0_has_the_value_of_the_cell_1(self):
        self.instruction1.setCurrentPosition(0, self.memory)
        self.instruction1.run()
        self.assertEqual(self.memory.getDir(0), self.memory.getDir(1))
        
        
    def test_when_move_a_literal_value_to_a_cell_then_the_cell_has_that_value(self):
        self.instruction2.setCurrentPosition(0, self.memory)
        self.instruction2.run()
        self.assertEqual(self.memory.getDir(0), 78)
        

