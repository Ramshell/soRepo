from OperativeSystemFactory import OperativeSystemFactory
from RAM import RAM
from Shell import Shell
from discFactory import diskFactory


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
    
    
    
