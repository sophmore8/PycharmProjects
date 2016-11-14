#coding:utf-8
import ssh
from optparse import OptionParser


class SshExp:
    def __init__(self,ssh_file,timeout):
        self.ssh_file = ssh_file
        self.timeout = timeout
        self.ssh_info = []

    def __load_ssh_info(self):
        with open(self.ssh_file,'rb+') as f:
            for info in f.readlines():
                if not info.startswith('#') and info.strip():
                    self.ssh_info.append(info.strip())

    def __exec(self,ip,username,password,cmd):
            myclient = ssh.SSHClient()
            myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())

            myclient.connect(ip, port=22, username=username, password=password,timeout=self.timeout)

            stdin, stdout, stderr = myclient.exec_command(cmd)

            return stdout.read()

    def exp(self):
        self.__load_ssh_info()
        
        for item in self.ssh_info:
            _ = item.split('|||')
            try:
                result = self.__exec(ip=_[0],username=_[1],password=_[2],cmd=_[3])
                print '*'*50
                print _[0]
                print result
            except:
                print _[0],'command execute failed!'

if __name__ == '__main__':
    usage = 'usage: backdoor_exp [options] arg'
    parser = OptionParser(usage)
    parser.add_option('-f', dest = 'ip_file', default = 'ssh.txt', help = 'the target file to pentest,defalut ssh.txt')
    parser.add_option('--timeout', dest = 'timeout', default = 2, help = 'ssh timeout,default 2')

    (options, args) = parser.parse_args()

    file = options.ip_file
    timeout = options.timeout
    
    t = SshExp(file,timeout)
    t.exp()

    