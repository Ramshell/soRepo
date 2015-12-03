from Queue import Queue

class IODelivery:
	'''
	Object that manages how to redirect data packages to all devices installed on OS.
	
	@author: Nicolas Leutwyler
	@author: Lucas Sandoval
	@author: Jesus Laime
	''' 

	def __init__(self):
		'''
	    Constructor of the io delivery.
	    ''' 
		self.queueDevices = []
		self.cant = 0
		
	
	def putInQueue(self, data, deviceCod):
		'''
	    Delivers data to an specific device
	    
	    @param data: Data to be delivered
	    @param deviceCod: Code of the device specified   
	    ''' 
		if (self.exist(deviceCod)):
			self.queueDevices[deviceCod].put(data)
		else:
			print("ERROR: -- DISPOSITIVO NO VALIDO!!! -- ")
		
	def newDevice(self, device):
		'''
	    Tells to the delivery, that a new device has been installed.
	    
	    @param device: Code of the new device 
	    ''' 
		self.newqueue = Queue()
		device.newqueue(self.newqueue)
		self.queueDevices.append(self.newqueue)
		self.cant = self.cant + 1
		
	def numberOfDevices(self):
		'''
	    @return: how many devices are installed
	    
	    @return: Number of devices 
	    ''' 
		return self.cant
	
	def numberOfInstructions(self, codDevice):
		'''
	    Informs how many data packages has a specified device.
	    
	    @return: Number of data packages
	    ''' 
		if (self.exist(codDevice)):
			return self.queueDevices[codDevice].qsize()
		
	def exist(self, codDevice):
		'''
	    Given a possibly actual device cod, tells if exists.
	    
	    @param codDevice: Specified code of the device 
	    
	    @return: True if exists, False otherwise
	    ''' 
		return codDevice < self.cant
