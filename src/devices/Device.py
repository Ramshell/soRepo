from threading import Thread
import time
from util.FileLogger import FileLogger

class Device(Thread):
	'''
    Object that represents a hardware device.
    
    @author: Nicolas Leutwyler
    @author: Lucas Sandoval
    @author: Jesus Laime
    '''

	def __init__(self, devName, interruptorM, queueAsoc=None):
		'''
		Constructor of the device
		
		@param devName: Name of the new device
		@param interruptorM: Interruptor Manager associated for interactions
		@param queueAsoc: Data Structure associated   
		'''
		Thread.__init__(self)
		self.interruptor = interruptorM
		self.switch = True
		self.name = devName
		self.queue = queueAsoc
		self.logger = None
		
	def newqueue(self, queue):
		'''
		Sets a new structure where data will be placed
		
		@param queue: The new structure 
		'''
		self.queue = queue
		

	def run(self):
		'''
		Interaction with its data structure, where in loop, reads data and executes requests
		'''
		while (self.switch & True):
			if (not self.queue.empty()):
				self.data = self.queue.get()
				self.proccess(self.data)
			else:
				time.sleep(.2)		
	

	def proccess(self,data):
		'''
		Given a data package, decode, and executes the instructions allocated
		'''
		self.logger.log("Executing from " +self.name + "...")
		self.instruction = data[1]
		self.pcb = data[0]
		self.execute(self.instruction)
		self.interruptor.ioDone(self.pcb)
	
	
	def execute(self, instruction):
		'''
		Given an instructions, this is executed
		
		@param instruction: Instruction to be executed 
		'''
		self.logger.log(str(instruction.value))
	
	def sizeOfQueue(self):
		'''
		@return: Number of data packages, the structure possess
		'''
		return self.queue.qsize()
		
	def stop(self):
		'''
		For stoping its looping work
		'''
		self.switch = False  # The Switch stands for ON / OFF Device.. True==ON, FALSE== OFF
	
	def setLogger(self,logger):
		self.logger = logger
