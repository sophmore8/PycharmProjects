#!/usr/bin/env python
#-*- coding:utf-8 -*-
import redis  #pip install redis
import os


#将文件 1000ip.txt 中的数据导入到redis服务器 10.0.1.137:6379 表名同文件名
def push_redies(redis_svr, filename, db_num):  #redis_svr  10.0.1.138:6379
    count = 0
    svr_lst = redis_svr.split(':')


    rds = redis.Redis(host=svr_lst[0],
                    port=svr_lst[1] if len(svr_lst)>1 else 6379,
                    db=db_num)


    #使用连接池  如需要多次创建连接，避免每次建立、释放连接的开销
    # pool = redis.ConnectionPool(host = svr_lst[0],
    #                             port=svr_lst[1] if len(svr_lst)>1 else 6379,
    #                             db=db_num)
    # rds= redis.Redis(connection_pool = pool)

    key = os.path.basename(filename).split('.')[0]   #表名
    with open(filename) as fp:
        for line in fp:
            # line = line.strip()
            wlist = line.split(",",1)
            rds.rpush(key, line)
            count += 1
    print count  #打印数据总量

push_redies("192.168.49.146:6379","one.php",4)
#或 push_redies("10.0.1.137","1000ip.txt",4)