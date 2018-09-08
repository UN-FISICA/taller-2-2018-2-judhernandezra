#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import turtle
lados = int(input("Número de lados del polígono "))
ali =int(input("Número de lados del polígono de alineación "))

ang=360/lados #ángulo polígono pequeño
aliang=360/ali #ángulo polígono de alineación
angr=2*math.pi/lados #ángulo polígono pequeño en radianes
aliangr=2*math.pi/ali #ángulo polígono de alineación en radianes

rp=50 #Radio del polígono pequeño
rg=200 #Radio del polígono de alineación
mi=180*(ali-2)/ali #ángulo interno del polígono de alineación

lp=2*rp*math.sin(angr/2) #longitud lado polígono pequeño
lg=2*rg*math.sin(aliangr/2) #longitud lado polígono de alineación


turtle.penup()
turtle.rt(90+(aliang/2))
turtle.fd(rg)
turtle.lt((aliang/2)+mi-90)
turtle.pendown()

for count in range(ali):
	
	turtle.penup()
	turtle.rt(mi-90)
	turtle.rt((ang/2)+(aliang*count))
	turtle.fd(rp)
	turtle.lt(90+(ang/2))
	turtle.pendown()

	for cuenta in range(lados):
		turtle.fd(lp)
		turtle.lt(ang)

	turtle.penup()
	turtle.lt(90-(ang/2))
	turtle.fd(rp)
	turtle.rt(90-(ang/2))
	turtle.lt((180-mi)*count)
	turtle.fd(lg)
	turtle.pendown()



