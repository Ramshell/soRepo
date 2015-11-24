from threading import *
import unittest

from IODelivery import IODelivery
from mockito.mocking import Mock
from mockito.mockito import verify
from mockito.mockito import when


class IODeliveryTest(unittest.TestCase):
	
	def setUp(self):
		self.delivery = IODelivery()
		self.device1 = Mock()
		self.device2 = Mock()
		self.device3 = Mock()
		self.delivery.newDevice(self.device1)  # Impresora
		self.delivery.newDevice(self.device2)  # Pantalla
		
		print(self.delivery.numberOfDevices())
		
	def test_when_ask_how_many_devices_are_then_correct_number_of_them(self):
		self.delivery.newDevice(self.device3)  # ARRANGE
		self.expected = 3
		
		self.value = self.delivery.numberOfDevices()  # ACT
		
		self.assertEquals(self.expected , self.value)  # ASSERT
	
	def test_when_new_instruction_puts_the_data_in_the_expected_device_queue(self):
		self.data = Mock()  # ARRANGE
		self.cod = 0  # CODIGO CORRESPONDIENTE A LA IMPRESORA 
		
		self.delivery.putInQueue(self.data, self.cod)  # ACT
	
		self.assertEquals(self.delivery.numberOfInstructions(self.cod) , 1)
		
	
