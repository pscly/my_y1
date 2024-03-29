# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

import webbrowser as web
import os
import shutil
import time
import datetime
import requests
from lib.func_2 import load_config
from multiprocessing import Process
from threading import Thread

file_config = load_config()

def baidu(url1=''):
    if url1 == '':  # 判断有没有传入搜索的东西
        while 1:
            url1 = input('输入问题(1)>>:').strip()
            if url1 == '':
                return
            elif url1.lower() == 'q':
                return
    web.open('https://www.baidu.com/s?wd={}'.format(url1))

def yixia(url1=''):
    '''1
    :param url1: 这个是需要搜索的东西
    '''
    if url1 == '':  # 判断有没有传入搜索的东西
        while 1:
            url1 = input('输入问题(1)>>:').strip()
            if url1 == '':
                return
            elif url1.lower() == 'q':
                return
    web.open(
        'https://www.google.com/search?ei=DJQlXcWbJJvW-QaYnr2YBA&q={0}&oq={0}&gs_l=psy-ab.3...0.0..1577...0.0..0.0.0.......0......gws-wiz.1DqK64vuO1U'.format(
            url1))
    baidu(url1)


def zhidao(url1=''):
    if url1 == '':
        url1 = input('输入知识(2)>>')
        if url1 == '':
            return
        elif url1.upper() == 'q':
            return
    web.open('https://zh.wikipedia.org/wiki/{}'.format(url1))
    web.open('https://baike.baidu.com/item/{}'.format(url1))


def hebin(url1=''):
    if url1 == '':
        url1 = input('输入查询>>:')
        if url1 == '':
            return
        elif url1.upper() == 'q':
            return
    web.open('https://zh.wikipedia.org/wiki/{}'.format(url1))
    web.open('https://baike.baidu.com/item/{}'.format(url1))
    web.open(
        'https://www.google.com/search?ei=DJQlXcWbJJvW-QaYnr2YBA&q={0}&oq={0}&gs_l=psy-ab.3...0.0..1577...0.0..0.0.0.......0......gws-wiz.1DqK64vuO1U'.format(
            url1))
    web.open('https://www.baidu.com/s?wd={}'.format(url1))


def zhihu(url1=''):
    if url1 == '':
        url1 = input('输入查询>>:')
        if url1 == '':
            return
        elif url1.upper() == 'q':
            return
    web.open(f'https://www.zhihu.com/search?type=content&q={url1}')


def shopping(url1=''):
    if url1 == '':
        url1 = input('输入查询>>:')
        if url1 == '':
            return
        elif url1.upper() == 'q':
            return
    web.open(
        f'https://s.taobao.com/search?q={url1}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200805&ie=utf8')
    web.open(f'https://search.jd.com/Search?keyword={url1}&enc=utf-8&wq={url1}&pvid=447c3e9e63904d03a8c281c22da7e78e')

def start_1():
    def send_1(*args):
        try:
            requests.post('http://pscly.cn:31001/end1/', headers={'is_y':'1'}, json={'gn':'my_y1'})
        except Exception as e:
            ...
    t = Thread(target=send_1, args=())
    t.start()

def zhengze(*args):
    web.open('http://tool.chinaz.com/regex/')


def ping(*ip_addr):
    if not ip_addr:
        ip_addr = ['pscly.cn']
    os.system('ping {}'.format(ip_addr[0]))



def mstsc(ipaddr='', *args):
    os.system('mstsc -v %s' % ipaddr)
    return


def ipconfig(hou='', *args):
    os.system('ipconfig %s' % hou)


def xh(*args):
    print('202040030804')
    return


def open_ali(x=0, *args):
    print("pypi\n-i https://mirrors.aliyun.com/pypi/simple\n")
    if x:
        web.open("https://developer.aliyun.com/mirror/")
    return


def w1():
    url = file_config.get('work_url')
    # url = r'http://20.30.1.119:7001/'
    web.open(url + r"issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cupdated_on%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=3&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%3D&v%5Bassigned_to_id%5D%5B%5D=41&f%5B%5D=done_ratio&op%5Bdone_ratio%5D=%3C%3D&v%5Bdone_ratio%5D%5B%5D=90&f%5B%5D=&c%5B%5D=project&c%5B%5D=fixed_version&c%5B%5D=parent&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=start_date&c%5B%5D=due_date&c%5B%5D=done_ratio&group_by=&t%5B%5D=")
    return

def is1(iss_num=891):
    """
    iss_num: 对应的iss号码
    """
    url = file_config.get('work_url')
    web.open(url+r'issues/%s' % iss_num)

def wd(path):
    os.system(f'explorer {path}')

def open_web(config_url):
    """通过url打开浏览器访问"""
    if '.' in config_url:
        # 代表这是直接的url 而不是配置文件格式
        url1 = config_url
    else:
        url1 = file_config.get(config_url)
    web.open(url1)
    return
    
def open_web2(config_url, url2=''):
    """通过url打开浏览器访问, 附加参数"""

    if '.' in config_url:
        # 代表这是直接的url 而不是配置文件格式
        url1 = config_url
    else:
        url1 = file_config.get(config_url)
        
    if url2:
        web.open(url1.format(url2))
    else:
        if url2 == '':
            url2 = input('输入查询>>:')
        if url2 == '':
            return
        elif url2.upper() == 'q':
            return
        web.open(url1.format(url2))
