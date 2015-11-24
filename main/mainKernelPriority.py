from Scheduler import Scheduler
from Shell import Shell
from OperativeSystemFactory import OperativeSystemFactory
from discFactory import diskFactory
from RAM import RAM
from Manual import Manual

if __name__ == '__main__':
    
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    osFc = OperativeSystemFactory(disk,RAM(65535),4)
    os = osFc.roundRobin_withPriority(2)
    os.installNewDevice("printer")
    os.installNewDevice("screen")
    os.estart()
    shell = Shell(os)
    shell.start()
    
    
    