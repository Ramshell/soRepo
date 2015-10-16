from threading import Thread


class Device(Thread):

	def __init__(self,devName,queueAsoc):
		self.name = devName;
		self.queue = queueAsoc;
		

	def run(self):
		
		while (True) {
			if (not self.queue.empty()){
				self.data = self.queue.get();
				self.proccess(self.data);
			} else {
				time.sleep(10);
			}
		}
		
	
	def proccess(self,data):
		self.instruction = data[1]
		self.pcb = data[0]
		
		self.execute(self.instruction)
		self.interruptor.ioDone(self.pcb);
	
	
	def execute(self,instruction):
		self.instruction = instruction
		self.instruction.run