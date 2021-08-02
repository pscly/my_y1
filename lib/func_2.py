# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

import shutil
import yaml
import os
import time
import requests
from pathlib import Path

def copy1():
    file1 = input('请输入是第**天():')
    shutil.copytree(r'F:\1SH10\day{0}\代码\day{0}'.format(file1),
                    r'F:\1py\.S10_sh\001day\day{0}\day{0}'.format(file1))  # 可以用的

def load_config():
    """从yaml中读取配置"""
    
    yaml_file = Path.cwd() / 'configs' / 'config.yaml'
    # 判断文件配置文件是否存在
    if not Path.is_file(yaml_file):
        print('配置文件不存在，或者是启动方式有问题，没有获取到正确的配置文件路径,现在使用我的网络版配置文件(部分功能可能会出现问题)')
        return yaml.safe_load(requests.get(r'https://gitee.com/pscly/my_y1/raw/master/configs/config.yaml').text)
    with open(yaml_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
    return {}

    
