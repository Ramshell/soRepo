from Instruction import Instruction


class InstIO(Instruction):

		
	def __init__(self, valor, cod):
		self.codDevice = cod
		Instruction.__init__(self, valor)
		
	def isIO(self):
		return True
	
	
	def deviceCod(self):
		return self.codDevice
	
	def run(self):
		pass
		
	def setValue(self,pcb,memory,mmu):
		pass
