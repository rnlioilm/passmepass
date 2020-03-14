import sys
import os
from core.author import __version__
from core.author import __codename__

def logoo():
    print("\033[H\033[J")
    print("\033[031m")
    sys.stdout.write(open("core/logo.txt","r").read()[:-1])
    print("\033[00m")
    sys.stdout.write("\t\033[033m .:[passmepass last version(%s-%s)]:.\n\033[00m"%(__version__,__codename__,))
