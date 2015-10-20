from Queue import Queue


class IODelivery:

	def __init__(self):
		self.queueDevices = []
		self.cant = 0
		
	
	def putInQueue(self,data,deviceCod):
		if (self.exist(deviceCod)):
			self.queueDevices[deviceCod].put(data)
		else:
			print("ERROR: -- DISPOSITIVO NO VALIDO!!! -- ")
		
	def newDevice(self):
		self.queueDevices.append(Queue())
		self.cant = self.cant +1
		
	def numberOfDevices(self):
		return self.cant
	
	def numberOfInstructions(self,codDevice):
		if (self.exist(codDevice)):
			return self.queueDevices[codDevice].qsize()
		
	def exist(self,codDevice):
		return codDevice < self.cant