#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import turtle

np= input("Número de filas de la pirámide ")
r=20 #Radio del círuculo
 

turtle.penup()
turtle.lt(90)
turtle.fd(200)
turtle.rt(90)
turtle.pendown()

for j in range(np+1):
	i=-j+1
	ang=360/(j+2)
	angr=2*math.pi/(j+2)
	while -j<i<j:
		turtle.penup()
		turtle.goto(i*5*np,200-(10*np*(j-1)))
		turtle.rt(90+(ang/2))
		turtle.fd(r)
		turtle.lt(90+(ang/2))
		i=i+2
		for count in range(j+2):
			d=2*r*math.sin(angr/2)
			turtle.pendown()
			turtle.fd(d)
			turtle.lt(ang)
			
