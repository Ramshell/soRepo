'''
Created on 27 de oct. de 2015

@author: Ramshell
@author: iGzo
@author: Exilio
'''
import unittest
from ProgramLoader import ProgramLoader
from mockito.mocking import Mock
from OwnHeap import OwnHeap
from RAM import RAM
from Scheduler import Scheduler
from CPU import CPU
from threading import Condition
from InterruptorManager import InterruptorManager
from IODelivery import IODelivery
from Device import Device
from Queue import Queue


class IntegrationTest(unittest.TestCase):


    def setUp(self):
        #miscellaneous
        self.semaphore = Condition()
        self.disk = Mock()
        self.comparator = lambda pcb1,pcb2: pcb1.getPriority() > pcb2.getPriority() #the greater, the better
        self.readyQueue = OwnHeap(self.semaphore, self.comparator)
        
        #hardware
        self.memory = RAM(1000)
        self.ioDelivery = IODelivery()
        self.progLoader = ProgramLoader(self.memory, self.disk, self.readyQueue)
        self.imanager = InterruptorManager()      
        self.cpu = CPU(self.memory, self.imanager, self.semaphore)
        self.scheduler = Scheduler(self.cpu, self.readyQueue , 5, self.semaphore)

        
        #devices
        self.spooler = Device('printer',  self.imanager)
        self.screen = Device('screen', self.imanager)
        
        self.ioDelivery.newDevice(self.spooler)
        self.ioDelivery.newDevice(self.screen)

        #im 
        self.imanager.setScheduler(self.scheduler)
        self.imanager.setDisk(self.disk)
        self.imanager.setMemory(self.memory)
        self.imanager.setIODelivery(self.ioDelivery)

    def test_when_probanding_todo_then_anding_todo(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()