from multiprocessing import Queue
from threading import Thread


class InterruptorManager(Thread):
    """
    @summary: Object that represents the Interruptor Manager Hardware that interact with CPU
    
    @author: Nicolas Leutwyler
    @author: Lucas Sandoval
    @author: Jesus Laime
    """
         

    def __init__(self,mmu=None,scheduler=None,hdd=None,ioDelivery=None,semaphore=None,pcbTable=None):
        """
        Constructor of the interruptor
        
        @param mmu: Memory management associated
        @param scheduler: Scheduler associated for replacement policies
        @param hdd: Hardware Disk to communicate with
        @param ioDelivery: Device that allows the communications with all the devices installed
        @param semaphore: Used to take control of the system on kernel mode
        @param pcbTable: Structure used to manage information about pcb      
        """
        self.mmu = mmu
        self.schPCB = scheduler
        self.io = ioDelivery
        self.hdd = hdd
        self.semaphore = semaphore
        self.pcbTable = pcbTable
    
    def ioQueue(self, data, cod):
        """
        Signal of an I/O interruption that sends data to an specified devide
        
        @param data: Data package to be delivered
        @param cod: Device code of the specified Device  
        """
        data[0].toWaiting()
        self.io.putInQueue(data, cod)
        self.schPCB.expropiate()
        self.schPCB.setPcbToCPU()
         

    

    def kill(self, pid):
        """
        Signal of a Kill interruption that terminate with a process
        
        @param pid: ID of the process to be terminated 
        """
        self.pcb = self.pcbTable.getPCB(pid)
        if self.pcb is None:
            return None
        self.semaphore.acquire()
        self.pcbIsAlreadyInCpu(self.pcb)
        self.pcbTable.delete(self.pcb)
        self.mmu.clean(self.pcb)
        self.semaphore.release()
        self.schPCB.getCpu().enable()
        
    def timeOut(self, pcb):
        """
        Signal of Timeout interruption that expropriate the cpu
        
        @param pcb: Pcb that will return to the the waiting state 
        """
        pcb.toReady()
        self.schPCB.put(pcb)
        self.schPCB.expropiate()
        self.schPCB.setPcbToCPU()
        
    def storePageNeeded(self, pcb):
        self.programLoader.storeNeededPage(pcb)
        

    def ioDone(self, pcb):
        """
        Signal of I/O end interruption invoked by a device
        
        @param pcb: That will return to the waiting state 
        """
        pcb.toReady()
        self.schPCB.put(pcb)
    
    def idleCPU(self):
        """
        Signal of IDLE CPU interruption, that will get a new pcb for assigning to the cpu
        """
        self.schPCB.setPcbToCPU()
    
    def setMmu(self, mmu):
        self.mmu = mmu
    
    def setScheduler(self, scheduler):
        self.schPCB = scheduler
        
    def setDisk(self, disk):
        self.hdd = disk
        
    def setIODelivery(self, iodelivery):
        self.io = iodelivery
        
    def setProgramLoader(self,programLoader):
        self.programLoader = programLoader
        
    def setSemaphore(self, semaphore):
        self.semaphore = semaphore
        
    def setPcbTable(self, pcbTable):
        self.pcbTable = pcbTable
        
    def pcbIsAlreadyInCpu(self, pcb):
        if self.schPCB.getCpuPid() == pcb.getPid():
            self.schPCB.expropiate()
        else:
            pcb.toTerminated()
            self.schPCB.cpu.disable()
