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
        #self.logger = FileLogger("../log/cpu_log")
        

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
        if pcb.isTerminated():
            self.condition.release()
            self.logger.log("Deleting terminated process with pid: "+ str(pcb.getPid()))
            return
        self.assignRafaga(pcb)
        pcb.runing()
        #self.logger.log("Setting new process to CPU")
        self.cpu.setPCB(pcb)
        self.condition.release()
    
    def assignRafaga(self, pcb):
        '''
        @param: the pcb to assign the burst
        '''
        pcb.assignBurst(self.burst)
        
    def getCpu(self):
        return self.cpu
    
    def getCpuPid(self):
        return self.cpu.pcb.getPid()
    
    def expropiate(self):
        self.cpu.pcb = None
        
        
        
          
