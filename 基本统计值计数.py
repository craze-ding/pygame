# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:33:30 2020

@author: 30217
"""
def ave(lt,l):
    sum=0
    for i in lt:
        sum+=eval(i)
    #print(sum,l)
    return sum/l
def fanfcha(lt,l,pj):
    sum=0
    for i in lt:
        sum+=pow(eval(i)-pj,2)
    #print(sum,l,pj)
    return pow(sum/(l-1),0.5)
def zhongweishu(lt,l):
    ls=sorted(lt)
    #print(ls,l)
    if l%2==0:
        zhong=(eval(ls[l//2-1])+eval(ls[l//2]))/2
    else:
        zhong=eval(ls[l//2])
    #print(zhong)
    return zhong
def get():
    lt=list()
    ls=input("请输入数字")
    while ls!="":
        lt.append(ls)
        ls=input("请输入数字")
    #print(lt)
    l=len(lt)
    return lt,l
def main( ):
    lt,l=get()
    pj=ave(lt,l)
    fc=fanfcha(lt,l,pj)
    zhong=zhongweishu(lt,l)
    print("平均数{:.2} 方差{:.2} 中位数{}".format(pj,fc,zhong))
try:
    main()
except :
    print("input error!")
    
        