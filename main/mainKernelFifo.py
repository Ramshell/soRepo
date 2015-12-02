from programs.Manual import Manual
from factories.OperativeSystemFactory import OperativeSystemFactory
from storage.RAM import RAM
from scheduler.Scheduler import Scheduler
from Consoles.Shell import Shell
from factories.discFactory import diskFactory


if __name__ == '__main__':
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    osFc = OperativeSystemFactory(disk, RAM(65535))
    os = osFc.fifo()
    os.installNewDevice("printer")
    os.installNewDevice("screen")
    os.startUp()
    shell = Shell(os)
    shell.start()
