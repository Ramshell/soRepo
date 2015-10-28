from threading import Thread
import time

class Device(Thread):

	def __init__(self,devName,interruptorM,queueAsoc=None):
		Thread.__init__(self)
		self.interruptor = interruptorM
		self.switch = True
		self.name = devName
		self.queue = queueAsoc
		
	def newqueue(self,queue):
		self.queue = queue
		

	def run(self):
		
		while (self.switch & True):
			if (not self.queue.empty()):
				self.data = self.queue.get()
				self.proccess(self.data)
			else:
				print "Waiting for an instruction to process -", self.devName
				time.sleep(2)		
	
	def proccess(self,data):
		self.instruction = data[1]
		self.pcb = data[0]
		
		self.execute(self.instruction)
		self.interruptor.ioDone(self.pcb);
	
	
	def execute(self,instruction):
		instruction.run()
	
	def sizeOfQueue(self):
		return self.queue.qsize()
		
	def stop(self):
		self.switch = False #The Switch stands for ON / OFF Device.. True==ON, FALSE== OFF
		
	def start(self):
		self.switch = True