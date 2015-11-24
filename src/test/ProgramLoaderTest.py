import unittest 

from Instructions.InstCPU import InstCPU
from Instructions.InstIO import InstIO
from Program import Program
from ProgramLoader import ProgramLoader
from RAM import RAM
from mockito.mocking import Mock
from mockito.mockito import when


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
