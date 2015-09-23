import os, sys
src_path = os.path.abspath(os.path.join('..'))
sys.path.append(src_path)

from RAM import RAM
from InstCPU import InstCPU
from InstIO import InstIO
from Program import Program
import unittest 
from mockito.mocking import Mock
from ProgramLoader import ProgramLoader
from mockito.mockito import when


class ProgramLoaderTest(unittest.TestCase):


    def setUp(self):
        self.disco = Mock()
        self.coladeprocesos = Mock()
        self.ram = RAM(10)
        
        self.progLoader = ProgramLoader(self.ram,self.disco,self.coladeprocesos)
        
        #Preparando un programa de dos (2) instrucciones
        self.instruccion1 = InstCPU("2+2")
        self.instruccion2 = InstIO("Leer de teclado")
        
        self.program = Program("prog")
        self.program.addInstruction(self.instruccion1)
        self.program.addInstruction(self.instruccion2)
        
    def test_load_a_program_pcb_creation(self):
        when(self.disco).getProgram("programa").thenReturn(self.program)
        
        self.progLoader.loadProcess("programa")
        
        self.assertEquals(self.progLoader.getNextId() , 1)


if __name__ == "__main__":
    unittest.main()        