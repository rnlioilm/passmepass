import sys
import optparse
import time
from core.main import shell
from core.printf import printf


    

def py_version():
    if sys.version_info.major == 2:
        pass
    elif sys.version_info.major == 3:
        printf(1,"passmepass has no support for python3.")
    else:
        printf(1,"your python version is very old........")
        

def platform():
    import sys
    if sys.platform.startswith('linux'):
        printf(2,"Running passmepass on linux ... (All good)")
      
    elif sys.platform.startswith('win32'):
        printf(2,"Running passmepass on \'Windows\' (Not tested)")

    elif sys.platform.startswith('darwin'):
        printf(2,"Running passmepass on \'Mac\' (Not tested)")  

    else:
        printf(2,"If \'passmepass\' runs sucsessfuly on your platform %s\nPlease contact me twitter! @rnlioilm" %sys.platform)




def main():
    py_version()
    platform()
    parser = optparse.OptionParser()
    parser.add_option("-p", "--profile", "--platform",dest="profile", help="|_O4d passmepass profile.")
    options,r = parser.parse_args()

    if options.profile:
        from core.main import shell_noint
        shell_noint(options.profile)
    else:
        from core.main import shell
        shell()

if __name__ == '__main__':
    main()
