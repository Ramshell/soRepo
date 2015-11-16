from RAM import RAM
from Program import Program
import unittest 
from mockito.mocking import Mock
from ProgramLoader import ProgramLoader
from mockito.mockito import when
from Instructions.InstCPU import InstCPU
from Instructions.InstIO import InstIO


class ProgramLoaderTest(unittest.TestCase):


    def setUp(self):
        self.disco = Mock()
        self.coladeprocesos = Mock()
        self.ram = RAM(10)
        
        self.progLoader = ProgramLoader(self.ram,self.disco,self.coladeprocesos)
        
        #Preparando un programa de dos (2) instrucciones
        self.instruccion1 = InstCPU("2+2")
        self.instruccion2 = InstIO("Leer de teclado",2)
        
        self.program = Program("prog")
        self.program.addInstruction(self.instruccion1)
        self.program.addInstruction(self.instruccion2)
        
    def test_load_a_program_pcb_creation(self):
        when(self.disco).getProgram("programa").thenReturn(self.program)
        
        self.progLoader.loadProcessWithNoPriority("programa")
        
        self.assertEquals(self.progLoader.getNextId() , 2)


if __name__ == "__main__":
    unittest.main()        
