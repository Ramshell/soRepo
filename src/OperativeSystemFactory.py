'''
Created on 27/10/2015

@author: exilio
'''

from Queue import Queue
from threading import Condition

from CPU import CPU
from Device import Device
from HardDisk import HardDisk
from IODelivery import IODelivery
from InterruptorManager import InterruptorManager
from Kernel import Kernel
from OwnHeap import OwnHeap, OwnQueue
from ProgramLoader import ProgramLoader
from RAM import RAM

from Scheduler import Scheduler
from clock import Clock
from memoryManagement.MMU import MMU


class OperativeSystemFactory:
    '''
    classdocs
    '''



    def __init__(self,disk,ram,frameSize):
        '''
        Constructor
        '''
        self.disk = disk
        self.ram = ram
        self.condition = Condition()
        self.mmu = MMU(frameSize,ram)
    
    
    #####################
    # TIPOS DE SCHEDULERS#
    #####################
    def roundRobin(self, quantum):
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)
        self.queue = OwnQueue(self.condition)
        self.scheduler = Scheduler(self.cpu, self.queue, quantum, self.condition)
        return self.__build(self.queue, self.scheduler)
    
    def fifo(self):
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)    
        self.queue = OwnQueue(self.condition)
        self.scheduler = Scheduler(self.cpu, self.queue, -1, self.condition)
        return self.__build(self.queue, self.scheduler)
        
    def withPriority(self):
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)
        self.func = lambda pcb1,pcb2: pcb1.getPriority() >= pcb2.getPriority()
        self.queue = OwnHeap(self.condition,self.func)
        self.scheduler = Scheduler(self.cpu,self.queue,-1,self.condition)
        return self.__build(self.queue,self.scheduler)
    
    def roundRobin_withPriority(self, quantum):
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)    
        self.func = lambda pcb1,pcb2: pcb1.getPriority() >= pcb2.getPriority()
        self.queue = OwnHeap(self.condition,self.func)
        self.scheduler = Scheduler(self.cpu,self.queue,quantum,self.condition)
        return self.__build(self.queue,self.scheduler)
    
    
    
    def __build(self, queue, scheduler):
        
        # miscellaneous
        self.ioDelivery = IODelivery()
#         self.device = Device("printer",self.imanager)
#         self.ioDelivery.newDevice(self.device)

        #hardware
        self.progLoader = ProgramLoader(self.ram, self.disk, queue,self.mmu)


        # InterruptorManager
        self.imanager.setScheduler(scheduler)
        self.imanager.setDisk(self.disk)
        self.imanager.setMmu(self.mmu)
        self.imanager.setIODelivery(self.ioDelivery)
        self.imanager.setSemaphore(self.condition)
        self.imanager.setPcbTable(self.progLoader.getPcbTable())
        
        self.clock = Clock(self.cpu)  #THREAD VIVO!!!! 
        
        return Kernel(self.clock, self.progLoader, self.imanager, self.ioDelivery)

        
        
if __name__ == '__main__':
    factori = OperativeSystemFactory(HardDisk(), RAM(1000))
    factori.roundRobin(4)
        
