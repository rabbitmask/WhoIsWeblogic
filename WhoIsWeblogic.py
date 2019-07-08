#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import logging
import requests
from multiprocessing import Pool, Manager

headers = {'user-agent': 'ceshi/0.0.1'}
filename1='ipsource.txt'
filename2='ipresult.txt'

logging.basicConfig(filename='WhoIsWeblogic.log',
                    format='%(asctime)s %(message)s',
                    filemode="w", level=logging.INFO)

#Weblogic模糊识别模块
def isweblogic(url):
    if 'http' not in url:
        url = 'http://' + url
    try:
        url1=url+'/console/login/LoginForm.jsp'
        r1 = requests.get(url1,timeout=5,headers=headers)
        logging.info("当前站点：{}\t状态码：{}\n".format(url1,r1.status_code))
        print("当前站点：{}\t状态码：{}".format(url1,r1.status_code))

        url2=url+'/wls-wsat/CoordinatorPortType'
        r2 = requests.get(url2,timeout=5,headers=headers)
        logging.info("当前站点：{}\t状态码：{}\n".format(url2,r2.status_code))
        print("当前站点：{}\t状态码：{}".format(url2,r2.status_code))

        url3=url+'/_async/AsyncResponseService'
        r3 = requests.get(url3,timeout=5,headers=headers)
        logging.info("当前站点：{}\t状态码：{}\n".format(url3,r3.status_code))
        print("当前站点：{}\t状态码：{}".format(url3,r3.status_code))

        url4=url+'/ws_utc/config.do'
        r4 = requests.get(url4,timeout=5,headers=headers)
        logging.info("当前站点：{}\t状态码：{}\n".format(url4,r4.status_code))
        print("当前站点：{}\t状态码：{}".format(url4,r4.status_code))

        return r1.status_code,r2.status_code,r3.status_code,r4.status_code
    except:
        logging.info("当前站点：{}\t响应超时\n".format(url))
        print("当前站点：{}\t响应超时\n".format(url))

def readtxt(url,i,q):
    r1,r2,r3,r4=isweblogic(url)
    if r1 == 200 or r2 == 200 or r3 ==200 or r4 ==200:
        fw = open(filename2, 'a')
        fw.write(url + '\n')
        fw.close()
    q.put(i)

# 进程池管理模块
def poolmana():
    p = Pool(20)
    q = Manager().Queue()
    fr = open(filename1, 'r')
    urls=fr.readlines()
    fr.close()
    for i in range(len(urls)):
        url = urls[i]
        url = url.replace("\n", '')
        p.apply_async(readtxt, args=(url,i,q))
    p.close()
    p.join()
    print('>>>>>任务结束\n')

def main():
    poolmana()

if "__main__" == __name__:
    main()