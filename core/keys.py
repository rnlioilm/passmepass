import os 
import sys




def keyy(key):
    try:
        memory = open("memory.log","r").readlines()
    except Exception as e:
        return 0
    if memory == None:
        return 0
    for line in memory:
        if line.startswith("\n") or line.startswith("#"):
            pass
        (skey,value) = line.split("=")
        if skey == key:
            return str(value[:-1])
        return 0
url = keyy("url") or None

port = int(8000)
ngrok = keyy("ngrok") or None
userAgent = keyy("userAgent") or "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"
html = None
files = None
exjs = keyy("exjs") or None
quiet_mode = False

