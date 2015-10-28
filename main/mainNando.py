from Scheduler import Scheduler
from Shell import Shell
from OperativeSystemFactory import OperativeSystemFactory
from discFactory import diskFactory
from RAM import RAM


if __name__ == '__main__':
    
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    osFc = OperativeSystemFactory(disk,RAM(1000))
    os = osFc.roundRobin_withPriority(10)
    os.installNewDevice("printer")
    os.installNewDevice("screen")
    os.estart()
    shell = Shell(os)
    shell.start()
    
    
    