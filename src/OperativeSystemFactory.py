'''
Created on 27/10/2015

@author: exilio
'''

from ProgramLoader import ProgramLoader
from Scheduler import Scheduler
from CPU import CPU
from threading import Condition
from InterruptorManager import InterruptorManager
from IODelivery import IODelivery
from clock import Clock
from Queue import Queue
from OwnHeap import OwnHeap
from RAM import RAM
from HardDisk import HardDisk

class OperativeSystemFactory:
    '''
    classdocs
    '''


    def __init__(self,disk,ram):
        '''
        Constructor
        '''
        self.disk = disk
        self.ram = ram
        self.condition = Condition()
    
    
    #####################
    #TIPOS DE SCHEDULERS#
    #####################
    def roundRobin(self,quantum):
        self.interruptor = InterruptorManager()
        self.cpu = CPU(self.ram, self.interruptor, self.condition)
        self.queue = Queue()
        self.scheduler = Scheduler(self.cpu,self.queue,quantum,self.condition)
        self.build(self.queue,self.scheduler)
    
    def fifo(self):
        self.interruptor = InterruptorManager()
        self.cpu = CPU(self.ram, self.interruptor, self.condition)
        self.queue = Queue()
        self.scheduler = Scheduler(self.cpu,self.queue,-1,self.condition)
        self.build(self.queue,self.scheduler)
        
    def withPriority(self):
        self.interruptor = InterruptorManager()
        self.cpu = CPU(self.ram, self.interruptor, self.condition)
        self.func = lambda pcb1,pcb2: pcb1.getPriority() > pcb2.getPriority()
        self.queue = OwnHeap(self.condition,self.func)
        self.scheduler = Scheduler(self.cpu,self.queue,1,self.condition)
        self.build(self.queue,self.scheduler)
    
    def roundRobin_withPriority(self,quantum):
        self.interruptor = InterruptorManager()
        self.cpu = CPU(self.ram, self.interruptor, self.condition)    
        self.func = lambda pcb1,pcb2: pcb1.getPriority() > pcb2.getPriority()
        self.queue = OwnHeap(self.condition,self.func)
        self.scheduler = Scheduler(self.cpu,self.queue,quantum,self.condition)
        self.build(self.queue,self.scheduler)
    
    
    
    def build(self,queue,scheduler):
        
        #miscellaneous
        self.ioDelivery = IODelivery()
        
        #hardware
        self.progLoader = ProgramLoader(self.ram, self.disk, queue)
        self.imanager = InterruptorManager()      
        self.cpu = CPU(self.ram, self.imanager, self.condition)
        
        #InterruptorManager
        self.imanager.setScheduler(scheduler)
        self.imanager.setDisk(self.disk)
        self.imanager.setMemory(self.ram)
        self.imanager.setIODelivery(self.ioDelivery)
        
        self.clock = Clock(self.cpu) #THREAD VIVO!!!! 
        
        #self.shell = Shell() HACER
        
        
if __name__ == '__main__':
    factori = OperativeSystemFactory(HardDisk(),RAM(1000))
    factori.roundRobin(4)
        