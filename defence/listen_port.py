#!/usr/bin/env python
import sys
import commands
import json
import subprocess  
import time
"""
监听端口，设置白名单
"""

while 1:
    cmd = 'netstat -tnp'
    result =commands.getoutput(cmd)
    #d2 = json.dumps(result)
    result= result.split('\n')
    #print result[1]
    #print len(result)
    for i in range(2, len(result)):
        for j in range(1,10):
            result[i]=result[i].replace('  ',' ')
        result[i]=result[i].split(' ')
        #print result[i]
        if result[i][0]=='tcp':
            result[i][3]=result[i][3].split(':')
            result[i][4]=result[i][4].split(':')
            #print result[i][3][1]
            xinren=0
            file_object = open('bai.txt')
            try:
                #list_of_all_the_lines = file_object.readlines( )
                for line in file_object:
                    #print result[i][2][0]+'  '+result[i][3][0]+'  '+result[i][4][0]+'  '+result[i][5][0]
                    if line.__contains__(result[i][3][1]):
                        xinren=1
                        break
                    if result[i][3][0]==result[i][4][0]:
                        xinren=1
                        break
                    #if result[i][4][0]=='127.0.0.1':
                    if result[i].__contains__('127.0.0.1'):
                        xinren=1
                        #print 'safe connection!'+result[i][4][0]
                        break
            finally:
                file_object.close( )
                if xinren==0:
                    #print result[i]
                    if result[i][6].__contains__('/'):
                        result[i][6]=result[i][6].split('/')
                        #print result[i][6][0]
                        if result[i][6][0]!='-':
                            print 'Unsafe Link!'+' our ip:'+ result[i][3][0]+':'+result[i][3][1]+':'+'enemy ip:'+result[i][4][0]+':'+result[i][4][1]+':'+' pid:'+result[i][6][0]
                            status,output =commands.getstatusoutput("kill -9 "+result[i][6][0])
                            #print status
                            if cmp(status,0)==0:
                                print 'Link have been killed!'
                            else:
                                print 'link can not be killed! reason :'+output
                    else:
                        if result[i].__contains__('ESTABLISHED'):
                            print 'Unsafe Link! can not find pid!'
                            print result[i]

    
    time.sleep(3)

