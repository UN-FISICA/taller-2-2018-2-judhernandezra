#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import turtle
sides = int(input("Número de lados del polígono "))
angle = 360 / sides
angler= 2*math.pi/sides
r=50
d=2*r*math.sin(angler/2)

turtle.penup()
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)
turtle.rt(angle)
turtle.fd(r)
turtle.lt(angle+90)
turtle.pendown()

for count in range(sides):
  turtle.fd(d)
  turtle.lt(angle)


