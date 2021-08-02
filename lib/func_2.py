# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

import shutil
import yaml
import os
import time

def copy1():
    file1 = input('请输入是第**天():')
    shutil.copytree(r'F:\1SH10\day{0}\代码\day{0}'.format(file1),
                    r'F:\1py\.S10_sh\001day\day{0}\day{0}'.format(file1))  # 可以用的

def load_config():
    """从yaml中读取配置"""
    yaml_file = r'./configs/config.yaml'
    # 判断文件配置文件是否存在
    if not os.path.exists(yaml_file):
        print('配置文件不存在，或者是启动方式有问题，没有获取到正确的配置文件路径')
        time.sleep(10)
    with open(yaml_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
    return {}

    
