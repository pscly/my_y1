# coding:utf-8
# 浏览器
# 作者：Pscly 
# 联系: qq:550191537   wechat: ps1cly
# 创建：2019年7月10日，18:40:05
# 用意：快速执行我想要实现的功能(后期打算加上更多功能(爬虫，数据分析, 不过可以写到别的文件，不过可以使用连接的方式让各个软件连接起来))

# 下一步目标：图形化， 窗口化，而不是用一个黑乎乎的cmd (有时间就去弄)
# (2020年3月29日-21点36分: 我打算连接远程数据库，弄个同步账号密码的东西，)

import webbrowser as web
import os
import shutil
import time
import datetime
import socket
from gong_neng.zaxiang import *
from lib.func_1 import *
from lib import func_2

d = datetime.datetime.now()
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
    2020年12月17日
        1:(08点51分) 精简化
    2021年2月10日
        1:(23点27分) 添加了ip地址
    2021年7月27日
        1:(11点25分) 添加了打开工作中查询任务的功能
    2021年8月1日
        1:(18点47分) 添加了一键打开工作目录
        2:(21点17分) 添加了一键打开学习目录，添加了扩展性，*添加了配置文件*
'''



def dayin(*args):
    for i in dakai:
        print(i, ' \t'.expandtabs(6), dakai[i][1])


config = func_2.load_config()['COMMON']

# 如果有参数，就放在[]的索引2位置
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
    'al': [open_ali, '打开阿里云的镜像网站'],
    'w1': [w1, '打开任务查询'],
    'wd': [wd, '打开工作的目录', config['work_dir']],
    'ed': [wd, '打开学习的目录', config['edu_dir']],

    'p': [ping, '测试网络'],
    'h': [dayin, 'look 菜单'],
    'm': [mstsc, '使用windows远程连接，'],
    'xh': [xh, '查看我的学号，'],

}


PATH = os.path.abspath(__file__)
ip_addr_1 = socket.gethostbyname_ex('')

print('-------------------------------------------------')
print(PATH)
print(f'    当前时间     {now_time}       星期{d1 + 1}')
print(f'    主机名_ip地址     {ip_addr_1[0]}{ip_addr_1[-1]}       ')
print(f'   周围主机     {ip_addr_1[1]}       ')
print('-------------------------------------------------')

dayin()

while 1:
    xuanzhe = input('输入快捷名,也可以直接输入cmd命令 开头选项+空格自动使用搜索功能(1)\n'
                    '------------------------------------------------------------------\n>>:').lower()

    if len(xuanzhe) < 1:
        continue

    if xuanzhe in dakai:
        if len(dakai[xuanzhe]) > 2:
            # 代表这个是有参数的
            dakai[xuanzhe][0](dakai[xuanzhe][2])

        else:
            [xuanzhe][0]()
        continue

    if xuanzhe[0] == ' ':
        search_content = xuanzhe[1:]  # 得到需要搜索文字
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
        dakai[head1][0](body1)  # TODO 这里传个参数进去

        continue

    if xuanzhe not in dakai:
        # print('输入错误，重新输入')
        os.system(f'{xuanzhe}')
        continue
    # eval(dakai[xuanzhe][0])
    # dakai[xuanzhe1]