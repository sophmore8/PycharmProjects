#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
import pexpect
import os, sys, getpass


host='192.168.116.135'
user='user'
password='123456'
status='success'
def ssh_command(user, host, password, command):
    ssh_newkey = '.*(yes/no).*'
    passwd_key = '.*assword.*'
    child = pexpect.spawn('ssh -l %s %s %s' %(user, host, command),timeout=1800)
    child.logfile = sys.stdout
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, passwd_key])

    if i == 0: #timeout
        print child.before
        print "Error time out"
        print child.after
        return None
    if i ==1 :
        child.sendline('yes')
        i = child.expect([pexpect.TIMEOUT, passwd_key])
        if i == 0:
            print child.before
            print 'time out ERROR'
            print child.after
            return None
    child.sendline(password)
    return child


def scp2(ip, user, passwd, dst_path, filename):
    status='success'
    passwd_key = '.*assword.*'
    if os.path.isdir(dst_path):
        cmdline = 'scp -r %s@%s:%s %s' % (user, ip, dst_path, filename)
    else:
        cmdline = 'scp %s@%s:%s %s' % (user, ip, dst_path, filename)
    try:
        ssh_newkey = '.*(yes/no).*'
        passwd_key = '.*assword.*'
        child = pexpect.spawn(cmdline,timeout=1800)
        child.logfile = sys.stdout
        i = child.expect([pexpect.TIMEOUT, ssh_newkey, passwd_key])

        if i == 0: #timeout
            print child.before
            print "Error time out"
            print child.after
            return None
        if i ==1 :
            child.sendline('yes')
            i = child.expect([pexpect.TIMEOUT, passwd_key])
            if i == 0:
                print child.before
                print 'time out ERROR'
                print child.after
                return None
        child.sendline(password)
        return child
    except:
        status='fail'

def scp_folder (ip, user, passwd, dst_path, filename):
    status='success'
    passwd_key = '.*assword.*'
    cmdline = 'scp -r %s@%s:%s %s' % (user, ip, dst_path, filename)
    try:
        ssh_newkey = '.*(yes/no).*'
        passwd_key = '.*assword.*'
        child = pexpect.spawn(cmdline,timeout=1800)
        child.logfile = sys.stdout
        i = child.expect([pexpect.TIMEOUT, ssh_newkey, passwd_key])

        if i == 0: #timeout
            print child.before
            print "Error time out"
            print child.after
            return None
        if i ==1 :
            child.sendline('yes')
            i = child.expect([pexpect.TIMEOUT, passwd_key])
            if i == 0:
                print child.before
                print 'time out ERROR'
                print child.after
                return None
        child.sendline(password)
        return child
    except:
        status='fail'

def scp_file (ip, user, passwd, dst_path, filename):
    status='success'
    passwd_key = '.*assword.*'
    cmdline = 'scp %s@%s:%s %s' % (user, ip, dst_path, filename)
    try:
        ssh_newkey = '.*(yes/no).*'
        passwd_key = '.*assword.*'
        child = pexpect.spawn(cmdline,timeout=1800)
        child.logfile = sys.stdout
        i = child.expect([pexpect.TIMEOUT, ssh_newkey, passwd_key])

        if i == 0: #timeout
            print child.before
            print "Error time out"
            print child.after
            return None
        if i ==1 :
            child.sendline('yes')
            i = child.expect([pexpect.TIMEOUT, passwd_key])
            if i == 0:
                print child.before
                print 'time out ERROR'
                print child.after
                return None
        child.sendline(password)
        return child
    except:
        status='fail'

def main():
    #child = ssh_command(user, host, password, command)
    # 前一个参数是靶机目录，后一个参数为本机目录
    # 备份文件夹使用scp_folder（），备份文件使用scp_file（）

    child=ssh_command(user,host,password,'mv /var/www/8022/wp-content/plugins/site-import /var/www/8022/wp-content/plugins/site-import-bak')
    child.expect(pexpect.EOF)
    print child.before

    child=ssh_command(user,host,password,'mv /var/www/8022/wp-content/plugins/wp-mobile-detector /var/www/8022/wp-content/plugins/wp-mobile-detector-bak')
    child.expect(pexpect.EOF)
    print child.before

    child=ssh_command(user,host,password,'mv /var/www/8022/wp-content/plugins/photocart-link /var/www/8022/wp-content/plugins/photocart-link-bak')
    child.expect(pexpect.EOF)
    print child.before



if __name__ == "__main__":
    main()
