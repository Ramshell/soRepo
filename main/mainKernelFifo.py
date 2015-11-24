from Manual import Manual
from OperativeSystemFactory import OperativeSystemFactory
from RAM import RAM
from Scheduler import Scheduler
from Shell import Shell
from discFactory import diskFactory


if __name__ == '__main__':
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    osFc = OperativeSystemFactory(disk,RAM(65535))
    os = osFc.fifo()
    os.installNewDevice("printer")
    os.installNewDevice("screen")
    os.estart()
    shell = Shell(os)
    shell.start()