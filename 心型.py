# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:14:54 2020

@author: 30217
"""

import turtle as t
t.penup()
t.seth(-90)
t.fd(160)
t.pendown()
t.pensize(2)
t.colormode(255)
for j in range(10):
    t.speed(1)
    t.pencolor(25*j,5*j,15*j)
    t.seth(130)
    t.fd(220)
    for i in range(23):
        t.circle(-80,10)
    t.seth(100)
    for i in range (23):
        t.circle(-80,10)
    t.fd(220)