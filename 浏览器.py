# 浏览器
# 作者：Pscly
# 创建：2019年7月10日，18:40:05
# 用意：快速执行我想要实现的功能(后期打算加上更多功能(爬虫，数据分析, 不过可以写到别的文件，不过可以使用连接的方式让各个软件连接起来))

# 下一步目标：图形化， 窗口化，而不是用一个黑乎乎的cmd (有时间就去弄)
# (2020年3月29日-21点36分: 我打算连接远程数据库，弄个同步账号密码的东西，)

import webbrowser as web
import os
import shutil
import time
import datetime
from gong_neng.zaxiang import *

d=datetime.datetime.now()
d1 = d.weekday()



now_time = time.strftime('%m-%d %X')

'''
# 更新日志:
    2020年3月26日(时间): 
        1：(上午)加上首位空格直接百度  更新成功    版本号1.0.1a
        2：(下午16点10分) 让p命令可以传入参数，指定p需要的地址(后续可以加入自动寻找网关) 1.0.2a
    2020年3月27日
        1: (09点30分) 让程序显示今天的日期,和星期 (后续打算调用天气的API接口)   1.1.0a
    2020年3月29日
        1: (21点20分) 添加了mstsc(远程控制命令) 1.2.0
    2020年3月30日
        1:(09点25分) 添加1和2合并在一起的功能3   （1.2.1）
    2020年4月2日
        1:(10点29分) 添加了单独百度的功能 (1.2.2)
	2020年4月6日
		1:(19点32分) 添加了查询ip的功能
    2020年4月8日
        1:(17点30分) 添加了特定符号进行换行输出的功能，(封装到其他文件夹下)
    2020年8月12日
        1:(13点47分) 打算添加淘宝的搜索和京东的搜索+知乎的搜索
    2020年12月10日
        1:(13点16分) 打算添加快捷打开阿里镜像
'''

# sign = '''
# # 此程序由‎2019‎年‎7‎月‎10‎日，‏‎18:40:05   
# Pscly开发------目前版本号为1.2.0版本
# '''
# print(sign) # 打印告示()

PATH = os.path.abspath(__file__)

print('-------------------------------------------------')
print(PATH)
print(f'    当前时间     {now_time}       星期{d1+1}')
print('-------------------------------------------------')

now1 = datetime.datetime.now()
end1 = now1.strftime("%Y-%m-%d %H:%M:%S")
# if end1 < '2020-2-12 20:50:12':    # 在什么时间以内  （这样他是按照年进行计算的）
if end1 < '4-12':    # 在什么时间以内  （这样他是按照月份）
    # 开始执行

    def baidu(url1=''):
        if url1 == '':             # 判断有没有传入搜索的东西
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
        if url1 == '':             # 判断有没有传入搜索的东西
            while 1:
                url1 = input('输入问题(1)>>:').strip()
                if url1 == '':
                    return
                elif url1.lower() == 'q':
                    return
        web.open('https://www.google.com/search?ei=DJQlXcWbJJvW-QaYnr2YBA&q={0}&oq={0}&gs_l=psy-ab.3...0.0..1577...0.0..0.0.0.......0......gws-wiz.1DqK64vuO1U'.format(url1))
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
        web.open('https://www.google.com/search?ei=DJQlXcWbJJvW-QaYnr2YBA&q={0}&oq={0}&gs_l=psy-ab.3...0.0..1577...0.0..0.0.0.......0......gws-wiz.1DqK64vuO1U'.format(url1))
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
        web.open(f'https://s.taobao.com/search?q={url1}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200805&ie=utf8')
        web.open(f'https://search.jd.com/Search?keyword={url1}&enc=utf-8&wq={url1}&pvid=447c3e9e63904d03a8c281c22da7e78e')




    def copy1():
        file1 = input('请输入是第**天():')
        shutil.copytree(r'F:\1SH10\day{0}\代码\day{0}'.format(file1),
                        r'F:\1py\.S10_sh\001day\day{0}\day{0}'.format(file1))  # 可以用的

    def zhengze(*args):
        web.open('http://tool.chinaz.com/regex/')

    def ping(*ip_addr):

        if not ip_addr:
            ip_addr = ['pscly.cn']
        os.system('ping {}'.format(ip_addr[0]))


    def dayin(*args):
        for i in dakai:
            print(i,' \t'.expandtabs(6),dakai[i][1])

    def mstsc(*ip_addr):

        if not ip_addr:
            os.system('mstsc')
        os.system('mstsc /v {}'.format(ip_addr[0]))
        return

    def ipconfig(*args):
        if args:
            os.system('ipconfig /all')
            return
        os.system('ipconfig')

    def xh(*args):
        print('202040030804')
        return

    def open_ali(x = 0,*args):
        print("pypi\n-i https://mirrors.aliyun.com/pypi/simple\n")
        if x:
            web.open("https://developer.aliyun.com/mirror/")
        return

    dakai = {

        '1': [yixia, '百度&谷歌一下'],
        '2': [zhidao, '百度知道/维基百科'],
        '3': [zhihu, '知乎'],
        '4': [shopping, '购物搜索'],
        '12': [hebin, '1和2同时使用'],
        'b': [baidu, '单用百度搜索'],
        'z': [zhengze, 're,正则查询'],
        'ip': [ipconfig, '查询IP地址，输入a=/all'],
        'hh': [huan_hang, '将文本按特定的字符串进行换行'],
        'al': [open_ali, '打开阿里云的网站'],


        'p': [ping, '测试网络'],
        'h': [dayin, 'look 菜单'],
        'm': [mstsc, '使用windows远程连接，'],
        'xh': [xh, '查看我的学号，'],

    }


    dayin()

    while 1:
        xuanzhe = input('输入快捷名,也可以直接输入cmd命令 开头选项+空格自动使用搜索功能(1)\n'
                        '------------------------------------------------------------------\n>>:').lower()

        if len(xuanzhe) < 1:
            continue

        if xuanzhe in dakai:
            dakai[xuanzhe][0]()
            continue

        if xuanzhe[0] == ' ':
            search_content = xuanzhe[1:]   # 得到需要搜索文字
            yixia(search_content)
            continue

        # if xuanzhe[0] in dakai and xuanzhe[1] == ' ':          # 第一个是参数，而且第二个也必须是空格才可以执行功能
        all_text = xuanzhe.split(' ', 1)
        if all_text[0] in dakai:
            head1 = all_text[0]
            body1 = all_text[1]
            print('head1:', head1, '||\tbody1:', body1)
            # xuanzhe0 = xuanzhe[0]
            # xuanzhe1 = xuanzhe[2:]
            # print(xuanzhe1)
            # dakai[xuanzhe0][0](xuanzhe1)    # TODO 这里传个参数进去
            dakai[head1][0](body1)    # TODO 这里传个参数进去

            continue


        if xuanzhe not in dakai:
            # print('输入错误，重新输入')
            os.system(f'{xuanzhe}')
            continue
        # eval(dakai[xuanzhe][0])
        # dakai[xuanzhe1]

else :
    print('使用时间已过,请联系qq:58766980 or 微信:ps1cly\nPscly(陈力源)')
    input()

