#!/usr/bin/python2.7
#coding:gbk
#author:Seay
#blog:www.cnseay.com

import os
import sys
import time

#reload(sys)
#sys.setdefaultencoding('gbk')

plusarr=[] #����б�
backdoor_count=0

def loadplus():
    #if len(plusarr)>0:
    #    for plus in plusarr:
    #        del sys.modules['plus.'+plus]
    #    del plusarr[:]

    for root,dirs,files in os.walk("plus"):
        for filespath in files:
            if filespath[-3:] == '.py':
                plusname = filespath[:-3]
                if plusname=='__init__':
                    continue
                __import__('plus.'+plusname)
                plusarr.append(plusname)

def Scan(path):
    loadplus() #��̬���ز��
    global backdoor_count
    for root,dirs,files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root,filename)
            if os.path.getsize(filepath)<500000:
                    for plus in plusarr:
                        file= open(filepath,"rb")
                        filestr = file.read()
                        file.close()
                        result = sys.modules['plus.'+plus].Check(filestr,filepath)

                        if result!=None:
                            print '�ļ�: ',
                            print filepath
                            print '��������: ',
                            print result[1]
                            print '���Ŵ���: ',
                            for code in result[0]:
                                print code[0][0:100]
                            print '����޸�ʱ��: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))+'\n\n'
                            backdoor_count= backdoor_count+1
                            break

def ScanFiletime(path,times):
    global backdoor_count
    times = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
    print '########################################'
    print '�ļ�·��           ����޸�ʱ��   \n'

    for root,dirs,files in os.walk(path):
        for curfile in files:
            if '.' in curfile:
                suffix = curfile[-4:].lower()
                filepath = os.path.join(root,curfile)
                if suffix=='.php' or suffix=='.jsp':
                    FileTime =os.path.getmtime(filepath)
                    if FileTime>times:
                        backdoor_count +=1
                        print filepath+'        '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(FileTime))

if __name__ == "__main__":
    print '----------------------------------------'
    print """
         �q�r���������������q�r����
       ����������������������������
       �q�ةء��������������ةبr
       ��������������������������������
       ��������������������������������
       �����񡡡������������񡡩�
       ���𡡡��t�ЩЩШs������
       �����������t���s������������
       �t�����Уϡ������ϩС����s
       �� ���q�r���������q�r��������
       �� ���t�ء��������بs
----�����������������������������----
----�� SeayFindShell 1.0      ��----
----�� Author:Seay                ��----
----�� SITE:www.cnseay.com        ��----
----��������������������������������----
    """

    if len(sys.argv)!=3 and len(sys.argv)!=2:
        print '����������'
        print '\t����������ɱ: '+sys.argv[0]+' Ŀ¼��'
        print '\t���޸�ʱ���ɱ: '+sys.argv[0]+' Ŀ¼�� ����޸�ʱ��(��ʽ:"2013-09-09 12:00:00")'
        exit()

    if os.path.lexists(sys.argv[1])==False:
        print '��������ʾ����ָ����ɨ��Ŀ¼������--- '
        exit()

    if len(sys.argv)==2:
        print '\n\n����ʼ��ɱ��'
        print sys.argv[1]+'\n'
        Scan(sys.argv[1])
        print '����ɱ��ɡ�'
        print '\t��������: '+str(backdoor_count)
    else:
        print '\n\n����ʼ���ҡ�'
        print sys.argv[1]+'\n'
        ScanFiletime(sys.argv[1],sys.argv[2])
        print '\n��������ɡ�'
        print '\t�ļ�����: '+str(backdoor_count)