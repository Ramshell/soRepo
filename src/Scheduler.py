
from threading import Thread
from multiprocessing import Queue
from OwnHeap import OwnHeap
from validate import ValidateError

class Scheduler:


    def __init__(self, cpu, queue, burst,condition):
        '''
        @param cpu: the cpu hardware
        @param queue: the kernel's readyQueue
        @param burst: the instruction's quantum to be executed by the cpu. -1 if inifinte.  
        '''
        self.cpu = cpu
        self.readyQueue = queue
        self.burst = burst
        self.condition = condition
        

        
    def setPcbToCPU(self):
        '''
        @invariant: sets the chosen pcb in the cpu if it exists. wait else
        '''
        self.condition.acquire()
        print self.readyQueue.empty()
        if self.readyQueue.empty():
            self.condition.wait()
        pcb = self.readyQueue.get()#this method also removes the element
        if pcb is None:
            raise Exception('Pcb is Null')
        self.assignRafaga(pcb)
        self.cpu.setPCB(pcb)
        self.condition.release()
    
    def assignRafaga(self, pcb):
        pcb.assignBurst(self.burst)
        
        
        
#         
#     def setRR(self,rafaga):
#         self.schedulingStrategy = RoundRobbin(rafaga,self.semaphore)
#         
#     def setFIFO(self):
#         self.schedulingStrategy = FIFO(self.semaphore)
#         
#     def setPriority(self):
#         self.schedulingStrategy = Priority(self.semaphore)
#         
#     def setPriorityAndRoundRobin(self,rafaga):
#         self.schedulingStrategy = PriorityAndRoundRobin(rafaga,self.semaphore)
    
# class SchedulingStrategy(object):
#     
#     def __init__(self):
#         pass
#     
#     
#     @abstractmethod
#     def choose(self):
#         pass
#     
#     @abstractmethod
#     def put(self):
#         pass
#     
# class FIFO(SchedulingStrategy):
#     
#     def __init__(self,semaphore):
#         self.queue = Queue()
# 
#     def choose(self):
#         return self.readyQueue.get()#This should be the first in pcb.
#         
#     def put(self,pcb):
#         self.readyQueue.put(pcb)
# 
#         
# class RoundRobbin(SchedulingStrategy):
#     
#     def __init__(self, countInstructionPerPCB,semaphore):
#         self.readyQueue = Queue()
#         self.rafaga = countInstructionPerPCB
# 
#     def choose(self):
#         return self.assignRafaga(self.readyQueue.get())#This should be the first in pcb.
#         
#     def put(self,pcb):
#         self.readyQueue.put(pcb)
#         
#     def assignRafaga(self, pcb):
#         pcb.assignRafaga(self.rafaga)
# 
# class Priority(SchedulingStrategy):
#     
#     def __init__(self,semaphore):
#         self.readyQueue = OwnHeap(semaphore)
#     
#     def choose(self):
#         return self.readyQueue.get()
#     
#     def put(self,pcb):
#         self.readyQueue.add(pcb)
#         
# class PriorityAndRoundRobin(SchedulingStrategy):
#     
#     def __init__(self, countInstructionPerPCB,semaphore):
#         self.readyQueue = OwnHeap(semaphore,(lambda pcb1,pcb2: pcb1.getPriority() > pcb2.getPriority()))
#         self.rafaga = countInstructionPerPCB
# 
#     def choose(self):
#         return self.assignRafaga(self.readyQueue.getAndRemoveMin()) #This should be the first in pcb.
#         
#     def put(self,pcb):
#         self.readyQueue.add(pcb)
#         
#     def assignRafaga(self, pcb):
#         pcb.assignRafaga(self.rafaga)
#         return pcb
# 
#     #un get de la cola para el program loader
#     def getReadyQueue(self):
#         return self.readyQueue
#     
    
          