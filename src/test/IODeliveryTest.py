import unittest
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when
import os, sys
from threading import *

src_path = os.path.abspath(os.path.join('..'))
sys.path.append(src_path)

from IODelivery import IODelivery

class IODeliveryTest(unittest.TestCase):
	
	def setUp(self):
		self.delivery = IODelivery()
		self.delivery.newDevice() #Impresora
		self.delivery.newDevice() #Pantalla
		
		print(self.delivery.numberOfDevices())
		
	def test_when_ask_how_many_devices_are_then_correct_number_of_them(self):
		self.delivery.newDevice() # ARRANGE
		self.expected = 3
		
		self.value = self.delivery.numberOfDevices() #ACT
		
		self.assertEquals(self.expected , self.value) #ASSERT
	
	def test_when_new_instruction_came_then_good_assigned_place(self):
		self.data = Mock() #ARRANGE
		self.cod = 0 #CODIGO CORRESPONDIENTE A LA IMPRESORA 
		
		self.delivery.putInQueue(self.data,self.cod) # ACT
	
		self.assertEquals(self.delivery.numberOfInstructions(self.cod) , 1)
		
	
