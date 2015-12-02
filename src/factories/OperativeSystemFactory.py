from Queue import Queue
from threading import Condition

from mainHardwareModules.CPU import CPU
from devices.Device import Device
from storage.HardDisk import HardDisk
from devices.IODelivery import IODelivery
from mainHardwareModules.InterruptorManager import InterruptorManager
from mainHardwareModules.Kernel import Kernel
from scheduler.OwnHeap import *
from mainHardwareModules.ProgramLoader import ProgramLoader
from storage.RAM import RAM

from scheduler.Scheduler import Scheduler
from mainHardwareModules.clock import Clock
from memoryManagement.MMU import MMU
from util.FileLogger import FileLogger
from util.CpuFileLogger import CpuFileLogger


class OperativeSystemFactory:
    '''
    @summary: useful for some components's abstraction. Returns different kernels, for multiple purposes
    '''



    def __init__(self,disk,ram,frameSize,mainConsole):
        '''
        @param HardDiskDrive: an HDD with some programs loaded.
        @param MemoryRam
        @param frameSize
        '''
        self.disk = disk
        self.ram = ram
        self.condition = Condition()
        self.mmu = MMU(frameSize,ram)
        self.console = mainConsole
    
    
    #####################
    # TIPOS DE SCHEDULERS#
    #####################
    def roundRobin(self, quantum):
        '''
        @return: given a <quantum>, returns a Round Robbin configured kernel, with quantum <quantum>
        '''
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)
        self.queue = OwnQueue(self.condition)
        self.scheduler = Scheduler(self.cpu, self.queue, quantum, self.condition)
        return self.__build(self.queue, self.scheduler)
    
    def fifo(self):
        '''
        @return: a FIFO kernel
        '''
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)    
        self.queue = OwnQueue(self.condition)
        self.scheduler = Scheduler(self.cpu, self.queue, -1, self.condition)
        return self.__build(self.queue, self.scheduler)
        
    def withPriority(self):
        '''
        @return: a Priority kernel
        '''
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)
        self.func = lambda pcb1,pcb2: pcb1.getPriority() >= pcb2.getPriority()
        self.queue = OwnHeap(self.condition,self.func)
        self.scheduler = Scheduler(self.cpu,self.queue,-1,self.condition)
        return self.__build(self.queue,self.scheduler)
    
    def roundRobin_withPriority(self, quantum):
        '''
        @return: given a <quantum> it returns a Priority-RR kernel with quantum <quantum>
        '''
        self.imanager = InterruptorManager()
        self.cpu = CPU(self.ram, self.imanager, self.condition,self.mmu)    
        self.func = lambda pcb1,pcb2: pcb1.getPriority() >= pcb2.getPriority()
        self.queue = OwnHeap(self.condition,self.func)
        self.scheduler = Scheduler(self.cpu,self.queue,quantum,self.condition)
        return self.__build(self.queue,self.scheduler)
    
    
    
    def __build(self, queue, scheduler):
        
        # miscellaneous
        self.ioDelivery = IODelivery()
        #hardware
        self.progLoader = ProgramLoader(self.ram, self.disk, queue,self.mmu)
        # InterruptorManager
        self.imanager.setScheduler(scheduler)
        self.imanager.setDisk(self.disk)
        self.imanager.setMmu(self.mmu)
        self.imanager.setIODelivery(self.ioDelivery)
        self.imanager.setSemaphore(self.condition)
        self.imanager.setPcbTable(self.progLoader.getPcbTable())
        self.imanager.setProgramLoader(self.progLoader)
        
        
        self.loggerCpu = CpuFileLogger("../log/cpu_log",self.console)
        self.cpu.setLogger(self.loggerCpu)
        
        self.clock = Clock(self.cpu)
        
        return Kernel(self.clock, self.progLoader, self.imanager, self.ioDelivery)

        
        
        
