
from abc import abstractmethod
from threading import Thread
from multiprocessing import Queue
from Queue import PriorityQueue
class Scheduler(Thread):


    def __init__(self, cpu, schedulingStrategy):
        self.cpu = cpu
        self.schedulingStrategy = schedulingStrategy
        
    def addPcb(self,pcb):
        self.schedulingStrategy.put(pcb)
        
    def setPcbToCPU(self):
        pcb = self.schedulingStrategy.choose()
        self.cpu.setPCB(pcb)
        self.schedulingStrategy.readyQueue.remove(pcb)
        
        
    
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
    
    def __init__(self):
        self.queue = Queue()

    def choose(self, readyQueue):
        return readyQueue.get()#This should be the first in pcb.
        
    def put(self,pcb):
        self.readyQueue.put(pcb);

        
class RoundRobbin(SchedulingStrategy):
    
    def __init__(self, countInstructionPerPCB):
        self.queue = Queue()
        self.rafaga = countInstructionPerPCB

    def choose(self, readyQueue):
        return self.assignRafaga(readyQueue.get())#This should be the first in pcb.
        
    def put(self,pcb):
        self.readyQueue.put(pcb);
        
    def assignRafaga(self, PCB):
        PCB.assignRafaga(self.rafaga)

class Priority(SchedulingStrategy):
    
    def __init__(self):
        self.readyQueue = PriorityQueue()
    
    def choose(self, readyQueue):
        return self.readyQueue.get()
    
    def put(self,pcb):
        self.readyQueue.put(pcb)
        
        