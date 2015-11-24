import unittest 

from Instructions.InstCPU import InstCPU
from Instructions.InstIO import InstIO

from Program import Program
from ProgramLoader import ProgramLoader
from RAM import RAM
from mockito.mocking import Mock
from mockito.mockito import when
from mockito.mockito import verify
from memoryManagement.MMU import MMU, Scope



class ProgramLoaderTest(unittest.TestCase):


    def setUp(self):
        self.disco = Mock()
        self.mmu = Mock()
        
        self.coladeprocesos = Mock()
        self.ram = RAM(65534)
        self.mmuReal= MMU(1,self.ram)
        self.mmuReal2= MMU(2,self.ram)
        

        self.progLoader = ProgramLoader(self.ram,self.disco,self.coladeprocesos,self.mmu)
        self.progLoader2 = ProgramLoader(self.ram,self.disco,self.coladeprocesos,self.mmuReal)
        self.progLoader3 = ProgramLoader(self.ram,self.disco,self.coladeprocesos,self.mmuReal2)

        
        # Preparando un programa de dos (2) instrucciones
        self.instruccion1 = InstCPU("2+2")
        self.instruccion2 = InstIO("Leer de teclado", 2)
        
        self.program = Program("prog")
        self.program.addInstruction(self.instruccion1)
        self.program.addInstruction(self.instruccion2)
        
    def test_load_a_program_pcb_creation(self):
        when(self.disco).getProgram("programa").thenReturn(self.program)
        when(self.mmu).getFrameSize().thenReturn(1)
        self.scope = Scope([0,23],[123])
        when(self.mmu).getMemoryScope(self.program).thenReturn(self.scope)
        when(self.mmu).fromPageToAbsolutePosition(0).thenReturn(0)
        when(self.mmu).fromPageToAbsolutePosition(23).thenReturn(23)
        when(self.disco).getProgram("programa").thenReturn(self.program)
        
        
        self.progLoader.loadProcessWithNoPriority("programa")
        
        self.assertEquals(self.progLoader.getNextId() , 2)
        verify(self.mmu,1).getMemoryScope(self.program)
        self.assertEquals(self.ram.getDir(0) , self.instruccion1)
        self.assertEquals(self.ram.getDir(23) , self.instruccion2)
        
    def test_load_a_program_pcb_creation_with_1_page(self):
        when(self.disco).getProgram("programa").thenReturn(self.program)
        when(self.mmu).getFrameSize().thenReturn(2)
        self.scope = Scope([23],[45])
        when(self.mmu).getMemoryScope(self.program).thenReturn(self.scope)
        when(self.mmu).fromPageToAbsolutePosition(23).thenReturn(46)
        when(self.disco).getProgram("programa").thenReturn(self.program)
        
        
        self.progLoader.loadProcessWithNoPriority("programa")
        
        self.assertEquals(self.progLoader.getNextId() , 2)
        verify(self.mmu,1).getMemoryScope(self.program)
        self.assertEquals(self.ram.getDir(46) , self.instruccion1)
        self.assertEquals(self.ram.getDir(47) , self.instruccion2)
        
    def test_load_a_program_pcb_creation_with_a_real_mmu(self):
        when(self.disco).getProgram("programa").thenReturn(self.program)
        when(self.disco).getProgram("programa").thenReturn(self.program)
        
        
        self.progLoader2.loadProcessWithNoPriority("programa")
        
        self.assertEquals(self.progLoader.getNextId() , 1)
        self.assertEquals(self.ram.getDir(0) , self.instruccion1)
        self.assertEquals(self.ram.getDir(1) , self.instruccion2)

if __name__ == "__main__":
    unittest.main()        
