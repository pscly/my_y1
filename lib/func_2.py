# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

import shutil
def copy1():
    file1 = input('请输入是第**天():')
    shutil.copytree(r'F:\1SH10\day{0}\代码\day{0}'.format(file1),
                    r'F:\1py\.S10_sh\001day\day{0}\day{0}'.format(file1))  # 可以用的

