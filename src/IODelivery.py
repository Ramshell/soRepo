from Queue import Queue


class IODelivery:

	def __init__(self):
		self.queueDevices [];
		self.cant = 0;
		
	
	def putInQueue(self,data,deviceCod):
		if (self.__exist(deviceCod)):
			self.queueDevices[deviceCod].put(data)
		else:
			print("ERROR: -- DISPOSITIVO NO VALIDO!!! -- ")
		
	def newDevice(self):
		self.queueDevices[self.cant] = Queue();
		self.cant = self.cant +1;
		
	def numberOfDevices(self):
		self.cant
	
	def numberOfInstructions(self,codDevice):
		if (self.__exist(codDevice)):
			self.queueDevices[codDevice].qsize()
		
	def __exist(self,codDevice):
		codDevice < self.cant