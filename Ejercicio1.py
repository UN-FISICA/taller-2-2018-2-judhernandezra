#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import turtle
angulo = 90
angulor= 2*math.pi/4
r=50
d=2*r*math.sin(angulor/2)

turtle.penup()
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)
turtle.rt(angulo/2)
turtle.fd(r)
turtle.lt(135)
turtle.pendown()

for count in range(4):
  turtle.fd(d)
  turtle.lt(angulo)

turtle.penup()
turtle.lt(45)
turtle.fd(r)
turtle.lt(45)
turtle.fd(200)
turtle.lt(135)
turtle.fd(r)
turtle.lt(135)
turtle.pendown()

for count in range(4):
  turtle.fd(d)
  turtle.lt(angulo)

turtle.penup()
turtle.lt(45)
turtle.fd(r)
turtle.lt(135)
turtle.fd(200)
turtle.lt(45)
turtle.fd(r)
turtle.lt(135)
turtle.pendown()

for count in range(4):
  turtle.fd(d)
  turtle.lt(angulo)

turtle.penup()
turtle.lt(45)
turtle.fd(r)
turtle.rt(135)
turtle.fd(200)
turtle.lt(45)
turtle.fd(r)
turtle.lt(135)
turtle.pendown()

for count in range(4):
  turtle.fd(d)
  turtle.lt(angulo)
