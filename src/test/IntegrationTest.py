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
from HardDisk import HardDisk
from Program import Program
from Instructions.InstCPU import InstCPU
from Instructions.InstIO import InstIO

class IntegrationTest(unittest.TestCase):


    def setUp(self):
        #miscellaneous
        self.semaphore = Condition()
        self.disk = HardDisk()
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

        #loading programs
        self.ioInstruction = InstIO('directory', 0)
        self.cpuInstruction = InstCPU('1+1')
        self.prog1 = Program('ls')
        self.prog2 = Program('pwd')
        
        self.prog1.addInstruction(self.cpuInstruction)
        self.prog2.addInstruction(self.ioInstruction)
        
        self.disk.setProgram(self.prog1)
        self.disk.setProgram(self.prog2)
        

    def test_when_programLoader_loadProcessWithNoPriority_then_it_starts_the_expected_sequence(self):
        self.progLoader.loadProcessWithNoPriority("ls")
        self.progLoader.loadProcessWithPriority("pwd", 3)
        self.table =self.progLoader.getPcbTable()
        self.table.getPS()
        self.assertEqual(2, self.table.countActiveProcess())
        self.assertEquals(2 ,self.readyQueue.length())
        self.assertEqual(self.cpuInstruction, self.memory.getDir(0))


