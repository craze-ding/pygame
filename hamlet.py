# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:54:24 2020

@author: 30217
"""
def gettxt():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    str='!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~'        
    for i in str:
        txt=txt.replace(i," ")
    return txt
hamlet=gettxt()
words=hamlet.split()
counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for n in range(10):
    word,count=items[n]
    print("{:<20} {:<10}".format(word,count))
    