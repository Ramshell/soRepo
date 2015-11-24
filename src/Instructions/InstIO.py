from Instruction import Instruction
from util.FileLogger import FileLogger

class InstIO(Instruction):

		
	def __init__(self,valor,cod):
		self.codDevice = cod
		Instruction.__init__(self,valor)
		self.logger = FileLogger("../../log/cpu_log")
		
	def isIO(self):
		return True
	
	def deviceCod(self):
		return self.codDevice
	
	def run(self):
		#self.logger.log(self.value)
		print self.value