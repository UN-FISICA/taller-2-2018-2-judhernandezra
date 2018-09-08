#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import turtle 
x=0
y=10
n=input ("Digite el número de lados del polígono ")
k=1
if (n%2==0):
    while (k<=n):
        print x,y
        x=10*math.cos((math.pi/n)+(2*math.pi*k/n))
        y=10*math.sin((math.pi/n)+(2*math.pi*k/n))
        k=k+1
else:
    while (k<=n):
        print x,y
        x=10*math.cos((math.pi/2)+(2*math.pi*k/n))
        y=10*math.sin((math.pi/2)+(2*math.pi*k/n))
        k=k+1
        

        
