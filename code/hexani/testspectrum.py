#!/bin/python


from turtleplus import *
from pprint import *
import numpy as np
import random
from tkinterx import *
import os, sys, getopt, random, re
import subprocess


def pause():
    t.getscreen()._root.mainloop()
# ----------------------------------------------------------
#################################################################
# define default vals
#################################################################

USECOLOR        = "SinSinSin"
#############################################################
# process command line args
#################################################################

argv = sys.argv[1:]
# print(argv, flush=True)

try:
    opts, args = getopt.getopt(argv, "s:", ["spectrum="])
except getopt.GetoptError:
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-s", "--spectrum"):
        USECOLOR = arg

        # colors = np.load(f"colordata/{ANGLE}.npy", allow_pickle=True)


screen = Screen()
screen.tracer(0)
screen.setup(1600,1600)
t = Turtle()
t.hideturtle()
screen.bgcolor("white")
t.penup()

xpos=-750
t.setx(-750)

ypos = 750
t.sety(ypos)

t.pendown()
t.pensize(1)
t.speed(9)
spectrums = np.load(f"colordata/spectrums.npy", allow_pickle=True)
# pprint(spectrums['progres])

slist2=[
    "denimbamboo",
    "yellows",
    "blues",
    "greens",
    "browns",
    "darkgrays",
    "lightgrays",
    "default",
    "medical_gray",
    "medical_gray_3",
    "aura_red",
    ]
slist=[
    "prog_A",
    "prog_B",
    "prog_C",
    "prog_C_fast",
    "prog_C_medium",
    "SinSinSin",
    "SinSinSinFast",
    "SinCosSin",
    "SinCosDelta",
    "SinCosDeltaFast",
    "pi",
    "progressive3",
    "progressive4",
]


for s in slist2:
    colors = spectrums.item().get(s)
    print(s)
    print(colors)
    for j in range(0,3):
        for i in range(0,len(colors)): #361):
            t.color(colors[i])
            print(i)
            t.penup()
            t.forward(40)
            t.pendown()
            t.dot(50)
    t.penup()
    # t.sety(ypos-50)
    t.pendown()
    t.color("black")
    t.write(s)
    t.penup()

    ypos = ypos - 100
    t.penup()
    t.sety(ypos)
    t.setx(xpos)
    t.pendown()

for s in slist:
    colors = spectrums.item().get(s)
    print(s)
    print(colors)
    for i in range(0,len(colors)): #361):
        t.color(colors[i])
        print(i)
        t.forward(4)
        t.dot(50)
    t.penup()
    t.sety(ypos-50)
    t.pendown()
    t.color("black")
    t.write(s)
    t.penup()

    ypos = ypos - 100
    t.penup()
    t.sety(ypos)
    t.setx(xpos)
    t.pendown()
pause()