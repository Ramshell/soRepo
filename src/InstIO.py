from Instruction import Instruction

class InstIO(Instruction):

		
	def __init__(self,valor,cod):
		Instruction.__init__(valor)
		self.codDevice = cod
        
	def isIO(self):
		return True
		
