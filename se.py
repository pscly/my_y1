from gong_neng.zaxiang import *
from lib.func_1 import *

# 方法:
# open_web 是没有参数的类型
# open_web2 是有参数的类型(搜索什么的就是有参数的)
from lib.func_2 import load_config
file_config = load_config()

dakai2 = {
    # 快捷键: [方法, "注释(菜单显示)", "url，或者config.yaml里面的url对应健"]
    # 'cs2': [open_web2, '搜索csdn', file_config['csdn']+'q={}',] # config 键加拼接(url混用)

    'mo': [open_web, '打开mooc', 'mooc_url'],   # 这里的mooc_url 就是对应键
    'cs': [open_web2, '搜索csdn', 'https://so.csdn.net/so/search?q={}&t=&u='],  # 这里就是直接的url{} 是替换搜索的字符
}

