import time

def printf(n,msg):

    if n == 0:
        print('\033[32m[%s]Error...%s\033[00m'%(time.strftime("%H:%M:%S"),msg))
        sys.exit()
    elif n == 1:
        print('\033[32m[%s]\033[00m%s'%(time.strftime("%H:%M:%S"),msg))
    else:
        print('\033[32m[%s]\033[00m%s'%(time.strftime("%H:%M:%S"),msg))

