# coding: utf-8
# 作者:Pscly
# 创建日期: 2020年4月8日
# 用意： 放一些杂项(免得有些文件堆的太多了)

def huan_hang():
    def tihuan(text1, fangshi):
        if fangshi == '1':
            tihuan_text = input('请输入要替换的文字>>:')
            tihuan_later = tihuan_text + '\n'
            over_text1 = text1.replace(tihuan_text, tihuan_later)

        elif fangshi == '2':
            tihuan_text = input('请输入要替换的文字>>:')
            tihuan_later = '\n'
            over_text1 = text1.replace(tihuan_text, tihuan_later)

        else:
            print('替换模式输入有误，请重新来')
            return None

        return over_text1

    text1 = input('请输入需要被换行的文字\n>>:')
    over_text = ''
    while not over_text:
        fangshi = input('如果保留替换文字请输入1,不保留请输入2\n>>:')
        over_text = tihuan(text1, fangshi)
    print(over_text)
    print()


if __name__ == '__main__':
    huan_hang()


