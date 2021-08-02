# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

# t1 = input('输入>>:')
# t2 = t1+'\n'
#
# print(t1)
# print(t2)
# print(t1)


# def a(x=0,*args):
#     print(f'x是{x}---',*args)
# a()


# 测试yaml读取
import yaml


# 1.读取yaml文件
def get_yaml_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.load(f)
x1 = get_yaml_data('./configs/config.yaml')

config = x1['COMMON']

print(x1)

