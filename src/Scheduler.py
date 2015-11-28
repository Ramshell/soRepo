from util.FileLogger import FileLogger


class Scheduler:


    def __init__(self, cpu, queue, burst, condition):
        '''
        @param: cpu the cpu hardware
        @param: queue: the kernel's readyQueue
        @param: burst: the instruction's quantum to be executed by the cpu. -1 if inifinte. 
        @param: condition: the condition is the current semaphore in the system 
        '''
        self.cpu = cpu
        self.readyQueue = queue
        self.burst = burst
        self.condition = condition
        self.logger = FileLogger("../log/scheduler_log")
        

    def put(self, pcb):
        self.readyQueue.put(pcb)
        
    def setPcbToCPU(self):
        '''
        @invariant: sets the chosen pcb in the cpu if it exists. wait else
        '''

        self.condition.acquire()
        if self.readyQueue.empty():
            self.condition.wait()
        pcb = self.readyQueue.get()  # this method also removes the element
        if pcb is None:
            raise Exception('Pcb is Null')
        self.assignRafaga(pcb)
        pcb.runing()
        self.logger.log("Setting new process to CPU")
        self.cpu.setPCB(pcb)
        self.condition.release()
    
    def assignRafaga(self, pcb):
        '''
        @param: the pcb to assign the burst
        '''
        pcb.assignBurst(self.burst)
        
        
        
          
