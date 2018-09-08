#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import turtle
lados = int(input("Número de lados del polígono "))
angulo = 360 / lados
angulor= 2*math.pi/lados
r=50
d=2*r*math.sin(angulor/2)


turtle.penup()
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)
turtle.rt(angulo/2)
turtle.fd(r)
turtle.lt(90+(angulo/2))
turtle.pendown()

for count in range(lados):
  turtle.fd(d)
  turtle.lt(angulo)

turtle.penup()
turtle.lt(90-(angulo/2))
turtle.fd(r)
turtle.lt((angulo/2))
turtle.fd(200)
turtle.rt(180+(angulo/2))
turtle.fd(r)
turtle.lt((angulo/2)+90)
turtle.pendown()

for count in range(lados):
  turtle.fd(d)
  turtle.lt(angulo)

turtle.penup()
turtle.lt(90-(angulo/2))
turtle.fd(r)
turtle.lt(90+(angulo/2))
turtle.fd(200)
turtle.lt(90-(angulo/2))
turtle.fd(r)
turtle.lt(90+(angulo/2))
turtle.pendown()

for count in range(lados):
  turtle.fd(d)
  turtle.lt(angulo)

turtle.penup()
turtle.lt(90-(angulo/2))
turtle.fd(r)
turtle.lt(180+(angulo/2))
turtle.fd(200)
turtle.rt(angulo/2)
turtle.fd(r)
turtle.lt(90+(angulo/2))
turtle.pendown()

for count in range(lados):
  turtle.fd(d)
  turtle.lt(angulo)

