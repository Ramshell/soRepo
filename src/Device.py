from threading import Thread
import time

from util.FileLogger import FileLogger


class Device(Thread):

	def __init__(self, devName, interruptorM, queueAsoc=None):
		Thread.__init__(self)
		self.interruptor = interruptorM
		self.switch = True
		self.name = devName
		self.queue = queueAsoc
		
		self.logger = FileLogger("../../log/" + self.name)
		
	def newqueue(self, queue):
		self.queue = queue
		

	def run(self):
		
		while (self.switch & True):
			if (not self.queue.empty()):
				self.data = self.queue.get()
				self.proccess(self.data)
			else:
				time.sleep(.2)		
	

	def proccess(self,data):
		print "Executing from " , self.name , "..."
		self.instruction = data[1]
		self.pcb = data[0]
		
		self.execute(self.instruction)
		self.interruptor.ioDone(self.pcb)
	
	
	def execute(self, instruction):
		instruction.run()
	
	def sizeOfQueue(self):
		return self.queue.qsize()
		
	def stop(self):
		self.switch = False  # The Switch stands for ON / OFF Device.. True==ON, FALSE== OFF
	
