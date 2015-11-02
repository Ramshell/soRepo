from Scheduler import Scheduler
from Shell import Shell
from OperativeSystemFactory import OperativeSystemFactory
from discFactory import diskFactory
from RAM import RAM
from Manual import Manual

if __name__ == '__main__':
    
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    osFc = OperativeSystemFactory(disk,RAM(1000))
    os = osFc.roundRobin_withPriority(2)
    os.installNewDevice("printer")
    os.installNewDevice("screen")
    os.estart()
    
    #manuals
    manuals = []
    manexe = Manual("execute", "run a program", ["a program"])
    manps = Manual("ps", "see the pcb information like pid, state and pc")
    mankill = Manual("kill", "close a program", ["a program"])
    manman = Manual("man", "see the manual of a program, utility or function",["a program", "a utility of the system", "a function"])
    manuals.append(manexe)
    manuals.append(manps)
    manuals.append(mankill)
    manuals.append(manman)
    
    shell = Shell(os,manuals)
    shell.start()
    
    
    