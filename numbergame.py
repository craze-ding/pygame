import types
from random import *
from random import randint
num = randint(1, 10)
tim = 0
while 1:
    try:
        putnum = eval(input("请输入您猜测的数字："))
        tim += 1
        if putnum > num:
            print("遗憾！太大了")
        elif putnum < num:
            print("遗憾！太小了")
        elif putnum == num:
            print("预测{}次，你猜中了！".format(tim))
            break
    except:
        print("输入有误！")
stri = input("请输入您想要的字符串：")
kong = 0
alpha = 0
chi = 0
num = 0
other = 0
for i in stri:
    if i == " ":
        kong += 1
    elif '0' <= i <= '9':
        num += 1
    elif i >= u'\u4e00' and i <= u'\u9fa5':
        chi += 1
    elif True == i.isalpha():
        alpha += 1
    else:
        other += 1
        print("您输入的字符串中有{}个空格, {}个数字, {}个中文, {}个英文字符, {}\
      个其他字符".format(kong, num, chi, alpha, other))
a, b = eval(input("请输入两个整数，中间用,隔开："))
c = a*b
if a < b:
    a, b = b, a
while False == (a in [0, 1]):
    b, a = a, b % a
c = c/b
print("最小公约数为：{},最大公倍数为：{}".format(b, c))
seed(100)
num = randint(0, 100)
tim = 0
while 1:
    try:
        putnum = eval(input("请输入您猜测的数字："))
        tim += 1
        if putnum > num:
            print("遗憾！太大了")
        elif putnum < num:
            print("遗憾！太小了")
        elif putnum == num:
            print("预测{}次，你猜中了！".format(tim))
            break
    except:
        print("输入有误！")
seed(100)
num = randint(0, 100)
tim = 0
while 1:
    try:
        putnum = eval(input("请输入您猜测的数字："))
        if type(putnum) == type(1):
            tim += 1
        if putnum > num:
            print("遗憾！太大了")
        elif putnum < num:
            print("遗憾！太小了")
        elif putnum == num:
            print("预测{}次，你猜中了！".format(tim))
            break
        else:
            print("输入内容必须为整数！")
    except:
            print("输入有误！")
