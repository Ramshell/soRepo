
from abc import abstractmethod
from threading import Thread
from multiprocessing import Queue
from OwnHeap import OwnHeap
class Scheduler:


    def __init__(self, cpu, semaphore):
        self.cpu = cpu
        self.semaphore = semaphore
        self.schedulingStrategy = FIFO(semaphore)
        
    def addPcb(self,pcb):
        self.schedulingStrategy.put(pcb)
        
    def setPcbToCPU(self):
        pcb = self.schedulingStrategy.choose()
        self.cpu.setPCB(pcb)
        
    def setRR(self,rafaga):
        self.schedulingStrategy = RoundRobbin(rafaga,self.semaphore)
        
    def setFIFO(self):
        self.schedulingStrategy = FIFO(self.semaphore)
        
    def setPriority(self):
        self.schedulingStrategy = Priority(self.semaphore)
        
    def setPriorityAndRoundRobin(self,rafaga):
        self.schedulingStrategy = PriorityAndRoundRobin(rafaga,self.semaphore)
    
    #despues lo vemos 
    def getQueue(self):
        return self.schedulingStrategy.getReadyQueue() 
    
class SchedulingStrategy(object):
    
    def __init__(self):
        pass
    
    
    @abstractmethod
    def choose(self):
        pass
    
    @abstractmethod
    def put(self):
        pass
    
class FIFO(SchedulingStrategy):
    
    def __init__(self,semaphore):
        self.queue = Queue()

    def choose(self):
        return self.readyQueue.get()#This should be the first in pcb.
        
    def put(self,pcb):
        self.readyQueue.put(pcb)

        
class RoundRobbin(SchedulingStrategy):
    
    def __init__(self, countInstructionPerPCB,semaphore):
        self.readyQueue = Queue()
        self.rafaga = countInstructionPerPCB

    def choose(self):
        return self.assignRafaga(self.readyQueue.get())#This should be the first in pcb.
        
    def put(self,pcb):
        self.readyQueue.put(pcb)
        
    def assignRafaga(self, pcb):
        pcb.assignRafaga(self.rafaga)

class Priority(SchedulingStrategy):
    
    def __init__(self,semaphore):
        self.readyQueue = OwnHeap(semaphore)
    
    def choose(self):
        return self.readyQueue.get()
    
    def put(self,pcb):
        self.readyQueue.add(pcb)
        
class PriorityAndRoundRobin(SchedulingStrategy):
    
    def __init__(self, countInstructionPerPCB,semaphore):
        self.readyQueue = OwnHeap(semaphore,(lambda pcb1,pcb2: pcb1.getPriority() > pcb2.getPriority()))
        self.rafaga = countInstructionPerPCB

    def choose(self):
        return self.assignRafaga(self.readyQueue.getAndRemoveMin()) #This should be the first in pcb.
        
    def put(self,pcb):
        self.readyQueue.add(pcb)
        
    def assignRafaga(self, pcb):
        pcb.assignRafaga(self.rafaga)
        return pcb

    #un get de la cola para el program loader
    def getReadyQueue(self):
        return self.readyQueue
    
    
          