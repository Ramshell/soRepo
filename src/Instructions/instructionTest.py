
import unittest
from RAM import RAM
from Assembly import *
from PCB import PCB
class Test(unittest.TestCase):


    def setUp(self):
        self.memory = RAM(65535)
        self.pcbAuxiliar = PCB(123,0,14)
        self.memory.putDir(0, 4)
        self.memory.putDir(1, 5)
        self.memory.putDir(2, 5)
        self.mov = Mov(0,1)
        self.movLiteral= MovLiteral(0,78)
        self.add = Add(0,1)
        self.addLiteral = AddLiteral(0,67)
        self.jump = Jmp(0)
        self.cmpEqual = Cmp(1,2)
        self.cmpLess = Cmp(0,1)
        self.cmpLiteralEqual=CmpLiteral(0,4)
        self.cmpLiteralLess=CmpLiteral(2,7)
        self.je = Je(3)
        self.jl = Jl(3)
        
    def test_when_move_the_value_from_1_to_0_then_the_cell_0_has_the_value_of_the_cell_1(self):
        self.mov.setCurrentPosition(0, self.memory)
        self.mov.run()
        self.assertEqual(self.memory.getDir(0), self.memory.getDir(1))
        
        
    def test_when_move_a_literal_value_to_a_cell_then_the_cell_has_that_value(self):
        self.movLiteral.setCurrentPosition(0, self.memory)
        self.movLiteral.run()
        self.assertEqual(self.memory.getDir(0), 78)
        
    def test_when_add_a_literal_value_to_a_cell_then_the_cell_has_that_value_plus_the_value_of_the_cell(self):
        self.add.setCurrentPosition(0, self.memory)
        self.add.run()
        self.assertEqual(self.memory.getDir(0), 9)
        
    def test_when_add_the_value_from_1_to_0_then_the_cell_0_has_the_value_of_the_cell_1_plus_the_value_of_the_cell_0(self):
        self.addLiteral.setCurrentPosition(0, self.memory)
        self.addLiteral.run()
        self.assertEqual(self.memory.getDir(0), 71)
        
    def test_when_the_instruction_jump_runs_then_the_pcb_asociated_changes_his_pc_to_the_relative_value(self):
        self.pcbAuxiliar.runing()
        self.pcbAuxiliar.incrementPc()
        self.pcbAuxiliar.incrementPc()
        self.jump.setCurrentPosition(123, self.pcbAuxiliar)#the absolute position doesn't matter
        self.jump.run()
        self.assertEquals(self.pcbAuxiliar.getPc(), 0)
        
        
    def test_when_cmp_2_equal_values_then_it_sets_the_pcb_flagZ_as_True(self):
        self.cmpEqual.setCurrentPosition(0, self.memory, self.pcbAuxiliar)
        self.cmpEqual.run()
        self.assertTrue(self.pcbAuxiliar.getFlagZ())
        self.assertFalse(self.pcbAuxiliar.getFlagS())
        
    def test_when_cmpLiteral_2_equal_values_then_it_sets_the_pcb_flagZ_as_True(self):
        self.cmpLiteralEqual.setCurrentPosition(0, self.memory, self.pcbAuxiliar)
        self.cmpLiteralEqual.run()
        self.assertTrue(self.pcbAuxiliar.getFlagZ())
        self.assertFalse(self.pcbAuxiliar.getFlagS())
        
    def test_when_cmp_a_number_A_lesser_than_a_number_B_then_it_sets_the_pcb_flagS_as_True(self):
        self.cmpLess.setCurrentPosition(0, self.memory, self.pcbAuxiliar)
        self.cmpLess.run()
        self.assertFalse(self.pcbAuxiliar.getFlagZ())
        self.assertTrue(self.pcbAuxiliar.getFlagS())
        
    def test_when_cmpLiteral_a_number_A_lesser_than_a_number_B_then_it_sets_the_pcb_flagS_as_True(self):
        self.cmpLiteralLess.setCurrentPosition(0, self.memory, self.pcbAuxiliar)
        self.cmpLiteralLess.run()
        self.assertFalse(self.pcbAuxiliar.getFlagZ())
        self.assertTrue(self.pcbAuxiliar.getFlagS())
        
    def test_when_JE_a_pcb_with_the_flagZ_on_then_it_makes_the_displacement(self):
        self.pcbAuxiliar.flagZ=True
        self.je.setCurrentPosition(12341, self.pcbAuxiliar)
        self.je.run()
        self.assertEquals(3, self.pcbAuxiliar.getPc())
        
    def test_when_JL_a_pcb_with_the_flagS_ON_then_it_makes_the_displacement(self):
        self.pcbAuxiliar.flagS=True
        self.jl.setCurrentPosition(12341, self.pcbAuxiliar)
        self.jl.run()
        self.assertEquals(3, self.pcbAuxiliar.getPc())
        
        
        

