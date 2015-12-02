from factories.OperativeSystemFactory import OperativeSystemFactory
from storage.RAM import RAM
from Consoles.Shell import Shell
from factories.discFactory import diskFactory


if __name__ == '__main__':
    
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    osFc = OperativeSystemFactory(disk,RAM(65535),4)
    os = osFc.roundRobin_withPriority(2)
    os.installNewDevice("printer")
    os.installNewDevice("screen")
    os.startUp()
    shell = Shell(os)
    shell.start()
    
    
    
