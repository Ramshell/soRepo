
from abc import abstractmethod
from threading import Thread
class Scheduler(Thread):


    def __init__(self, cpu,readyQueue):
        self.readyQueue = readyQueue
        self.cpu = cpu
        self.schedulingStrategy = SchedulingStrategy()
        
    def addPcb(self,pcb):
        self.readyQueue.add(pcb)
        
    def freeCPU(self):
        pcb = self.schedulingStrategy.choose(self.readyQueue)
        self.cpu.setPCB(pcb)
        self.readyQueue.remove(pcb)
        
        
    
class SchedulingStrategy(object):
    
    def __init__(self):
        pass
    
    
    @abstractmethod
    def choose(self):
        pass
    
    
class FIFO(SchedulingStrategy):
    
    def __init__(self):
        pass

    def choose(self, readyQueue):
        return readyQueue.last()
        

        
class RoundRobbin(SchedulingStrategy):
    
    def __init__(self):
        pass

    def choose(self, readyQueue):
        return readyQueue.last()



class Priority(SchedulingStrategy):
    
    def __init__(self):
        pass
    
    def choose(self, readyQueue):
        