#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import turtle

n= input("Número de lados del polígono ")
np= input("Número de filas de la pirámide ")

ang=360/n 

turtle.penup()
turtle.lt(90)
turtle.fd(200)
turtle.rt(90)
turtle.pendown()

for j in range(np+1):
	i=-j+1
	while -j<i<j:
		turtle.penup()
		turtle.goto(i*n*7,200-(15*n*(j-1)))
		turtle.rt(90+(ang/2))
		turtle.fd(10)
		turtle.lt(90+(ang/2))
		i=i+2
		for count in range(n):
			turtle.pendown()
			turtle.fd(25)
			turtle.lt(ang)
			

