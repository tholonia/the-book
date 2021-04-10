#!/bin/python

# example:
# python ./hex_builderDEVIATIONapse.py -l 25 -e 0 -f 60 -t 60





from turtleplus import *
from pprint import pprint
import numpy as np
import random
from tkinterx import *
import os, sys, getopt, random, re
import subprocess






def diff(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)


def change_color(t):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    t.color(R, G, B)


def dl(t, last_x, last_y, last_heading, color, len, flowersize, angle, outline,outline_pensize):
    # set the position to a previous point
    # global cpi
    global p
    # cpi = cpi + 1

    t.setheading(last_heading)
    t.penup()
    t.setposition(last_x, last_y)
    t.pendown()

    # drae the left line
    t.left(angle)  # turn left
    t.forward(len)  # drawl line

    angl = t.heading()
    # t.dot(20)

    # get the end poijt position
    lpos = t.position()  # store pos
    t.right(angle)  # face front

    ldat = [lpos[0], lpos[1], angl, pi]

    larrow(color,flowersize, outline,t, angle,outline_pensize)
    positions.append(ldat)

    return (ldat)


def dr(t, last_x, last_y, last_heading, color, len, flowersize, angle, outline,outline_pensize):
    # global cpi
    global p

    t.setheading(last_heading)
    t.penup()
    t.setposition(last_x, last_y)
    t.pendown()

    # draw the right line
    t.right(angle)
    t.forward(len)

    # cpi = cpi + 1
    angr = t.heading()
    # t.dot(25)

    # get the position
    rpos = t.position()  # store pos
    rx = rpos[0]
    ry = rpos[1]

    # get the end poijt position
    rpos = t.position()  # store pos

    t.left(angle)  # face front

    rdat = [rpos[0], rpos[1], angr, pi]

    positions.append(rdat)
    rarrow(color,flowersize, outline,t, angle,outline_pensize)
    return (rdat)

def reverseColor(t):
    currentColor = t.fillcolor()

    rd = 255 - currentColor[0]
    gd = 255 - currentColor[1]
    bd = 255 - currentColor[2]

    rh = hex(int(rd))[2:].zfill(2)
    gh = hex(int(gd))[2:].zfill(2)
    bh = hex(int(bd))[2:].zfill(2)

    newcolor = f"#{rh}{gh}{bh}"
    return(newcolor)

def larrow(clr,flowersize, outline, t, angle,outline_pensize):

    # get pensize
    tps = t.pensize()

    # get the position
    rpos = t.position()  # store pos
    rx = rpos[0]
    ry = rpos[1]
    h = t.heading()

    # -------
    t.fillcolor(clr)
    t.begin_fill()

    t.left(angle * 3.5)  # 210)
    t.forward(flowersize)

    t.left(angle * 2)  # 120)
    t.forward(flowersize / 2)

    t.left(angle * 1.5)  # 90)
    t.forward(flowersize * .8)

    t.end_fill()

    if (outline != "no"):
        t.penup()
        # -------
        t.setx(rx)
        t.sety(ry)
        t.setheading(h)

        t.pensize(outline_pensize)

        if outline == "reverse":
            t.color(reverseColor(t))
        else:
            t.color(outline)

        t.left(angle * 3.5)  # 210)
        t.pendown()
        t.forward(flowersize)
        t.penup()

        t.left(angle * 2)  # 120)
        t.pendown()
        t.forward(flowersize / 2)
        t.penup()

        t.left(angle * 1.5)  # 90)
        t.pendown()
        t.forward(flowersize * .8)
        t.penup()

        t.pensize(tps)
        t.color(clr)




def rarrow(clr,flowersize, outline, t, angle, outline_pensize):
    # get pensize
    tps = t.pensize()
    # get the position
    rpos = t.position()  # store pos
    rx = rpos[0]
    ry = rpos[1]
    h=t.heading()


    # -------
    t.fillcolor(clr)
    t.begin_fill()

    t.right(angle * 3.5)  # 210
    t.forward(flowersize)

    t.right(angle * 2)  # 120)
    t.forward(flowersize / 2)

    t.right(angle * 1.5)  # 90)
    t.forward(flowersize * .8)

    t.end_fill()

    if (outline != "no"):
        t.penup()
        # -------
        t.setx(rx)
        t.sety(ry)
        t.setheading(h)

        t.pensize(outline_pensize)
        if outline == "reverse":
            t.color(reverseColor(t))
        else:
            t.color(outline)

        t.right(angle * 3.5)  # 210

        t.pendown()
        t.forward(flowersize)
        t.penup()

        t.right(angle * 2)  # 120)
        t.pendown()
        t.forward(flowersize / 2)
        t.penup()

        t.right(angle * 1.5)  # 90)
        t.pendown()
        t.forward(flowersize * .8)
        t.penup()

        t.pensize(tps)
        t.color(clr)



def pause():
    t.getscreen()._root.mainloop()


def bifur(t, last_x, last_y, last_heading, color, len, flowersize, angle, outline, outline_pensize):
    global cc
    t.pendown()
    lp = dl(t, last_x, last_y, last_heading, color, len, flowersize, angle, outline,outline_pensize)
    rp = dr(t, last_x, last_y, last_heading, color, len, flowersize, angle, outline,outline_pensize)
    t.penup()
    cc = cc + 1

def random_deviate(val, pct, isRandom):
    delta = float(val) * float(pct)

    lo = float(val) - delta
    hi = float(val) + delta

    if (isRandom):
        return round(random.uniform(lo, hi))
    else:
        return round(hi)

def deviate(angle, lo, hi):
    return round(random.uniform(lo, hi))


def makeArgs(myargs):
    longargs = []
    for k in myargs.keys():
        longargs.append(k)

    shortargs = ""
    for k in myargs.values():
        shortargs = shortargs +  k

    sargs = ""
    shortargsAry = []
    for a in  myargs.values():
        a = a.replace(":","")
        a = f"-{a}"
        shortargsAry.append(a)
        sargs = sargs +  a

    largs = []
    for a in  myargs.keys():
        a = a.replace("=","")
        a = f"--{a}"
        largs.append(a)

    comp = {}
    for i in range(0,len(largs)):
        # print(largs[i])
        # print(shortargsAry[i])
        comp[largs[i]] = shortargsAry[i]
    # print(comp)
    # print(sargs)
    # print(largs)
    #
    return longargs,shortargs, comp

# ----------------------------------------------------------
#################################################################
# define default vals
#################################################################

USECOLOR        = "default"
USE_ALT_COLOR   = USECOLOR
LENGTH          = 60  # length of line
INCREMENT       = 0 #.60 # parameters for relative angle - percantage 0.6 = 60%
_ANG_DEVIATION  = [0,1] # .6 # parameters for length/angle variance
ANG_DEVIATION   = _ANG_DEVIATION[0]
ANG_DEVIATION_r = _ANG_DEVIATION[1]
_LEN_DEVIATION  = [0,0] #.1
LEN_DEVIATION   = _LEN_DEVIATION[0]
LEN_DEVIATION_r = _LEN_DEVIATION[1]
SUBDIR          = "ani_3"
COUNT           = 6
ANGLE           = 60
STYLE           = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
FLOWERSIZE      = 15
LOCKED          = 1
OUTLINE         = "no"
OUTLINE_PENSIZE = 1
GROWFLOWER      = 0
NAME            = "name"
SERIES          = "series"
SYNCPOINTS      = 0
CORES           = 1
RANDCLR         = 0

colors          = np.load(f"colordata/{ANGLE}.npy", allow_pickle=True)
clr1            = []
clr2            = []
#############################################################
# process command line args
#################################################################

argv = sys.argv[1:]
# print(argv, flush=True)


myargs = {
         "length="      :"l:",
         "ANGdeviation=":"e:",
         "LENdeviation=":"E:",
         "angle="       :"a:",
         "subdir="      :"s:",
         "count="       :"c:",
         "usecolor="    :"u:",
         "use_alt_color=" :"U:",
         "style="       :"S:",
         "flowersize="  :"F:",
         "desklock="    :"D:",
         "outline="     :"o:",
         "growflower="  :"g:",
         "name="        :"y:",
         "series="      :"z:",
         "syncpoints="  :"w:",
         "cores="       :"C:",
         "randclr="     :"r:",
}

longargs, shortargs, comp = makeArgs(myargs)
try:
    opts, args = getopt.getopt(argv, shortargs, longargs)
except getopt.GetoptError as err:
    print("--------------------------------------------------")
    print(f"hex_builder_lapse.py: {err}")
    print("--------------------------------------------------")
    sys.exit(2)
for opt, arg in opts:
    # print(opt,arg);
    if opt in (comp['--length'], "--length"):
        LENGTH = int(arg) #L
    if opt in (comp['--ANGdeviation'], "--ANGdeviation"):
        _ANG_DEVIATION = arg.split(":")
        ANG_DEVIATION = float(_ANG_DEVIATION[0])
        ANG_DEVIATION_r = int(_ANG_DEVIATION[1])
    if opt in (comp['--LENdeviation'], "--LENdeviation"):
        _LEN_DEVIATION = arg.split(":")
        LEN_DEVIATION = float(_LEN_DEVIATION[0])
        LEN_DEVIATION_r = int(_LEN_DEVIATION[1])
    if opt in (comp['--angle'], "--angle"):
        ANGLE = int(arg)
        print(f"LOADING: colordata/{ANGLE}.npy", flush=True)
        colors = np.load(f"colordata/{ANGLE}.npy", allow_pickle=True)
    if opt in (comp['--subdir'], "--subdir"):
        SUBDIR = arg
    if opt in (comp['--count'], "--count"):
        COUNT = int(arg)
    if opt in (comp['--usecolor'], "--usecolor"):
        USECOLOR = arg
        clr1 = colors.item().get(USECOLOR)
    if opt in (comp['--use_alt_color'], "--use_alt_color"):
        use_alt_color = arg
        clr2 = colors.item().get(use_alt_color)
    if opt in (comp['--style'], "--style"):
        STYLE = arg.split(',')
    if opt in (comp['--flowersize'], "--flowersize"):
        FLOWERSIZE = int(arg)
    if opt in (comp['--desklock'], "--desklock"):
        LOCKED = int(arg)
    if opt in (comp['--outline'], "--outline"):
        tmp = arg.split(":")
        OUTLINE = tmp[0]
        if (len(tmp) > 1):
            OUTLINE_PENSIZE = int(tmp[1])
    if opt in (comp['--growflower'], "--growflower"):
        GROWFLOWER = int(arg)
    if opt in (comp['--name'], "--name"):
        NAME = arg
    if opt in (comp['--series'], "--series"):
        SERIES = arg
    if opt in (comp['--syncpoints'], "--syncpoints"):
        SYNCPOINTS = int(arg)
    if opt in (comp['--cores'], "--cores"):
        CORES = int(arg)
    if opt in (comp['--randclr'], "--randclr"):
        RANDCLR = int(arg)

clrs = [clr1,clr2]
print("-------------------------------------------",flush=True)
print(clrs, flush=True)
print("-------------------------------------------",flush=True)

cmd = f"(running/{SUBDIR}) ./hex_builder_lapse.py"
cmd = cmd + f" --length {LENGTH}"
cmd = cmd + f" --ANGdeviation {ANG_DEVIATION}:{ANG_DEVIATION_r}"
cmd = cmd + f" --LENdeviation {LEN_DEVIATION}:{LEN_DEVIATION_r} "
cmd = cmd + f" --angle {ANGLE}  "
cmd = cmd + f" --count {COUNT} "
cmd = cmd + f" --usecolor {USECOLOR}"
cmd = cmd + f" --use_alt_color {use_alt_color}"
cmd = cmd + f" --subdir {SUBDIR}"
cmd = cmd + f" --desklock {LOCKED}"
cmd = cmd + f" --cores {CORES}"
cmd = cmd + f" --randclr {RANDCLR}"

print(cmd, flush=True)
# key_pressed = input('Press ENTER to continue: ')

#################################################################
# define other vars
#################################################################

angle = 60  #5 # angle of separation
cc   = 0
pi   = 0
level = 0 # set first level
pensize = (STYLE[level])
#################################################################
# init turtle
#################################################################

screen = Screen()
screenhide = 1

if LOCKED == 1:
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-type', 'desktop')
    screenhide = 0

screen.tracer(screenhide)  # turns off screen drawing


screen.setup(1200,1200)
t = Turtle()
t.hideturtle()
screen.bgcolor("white")
t.pensize(pensize)
#################################################################
# start to draw
#################################################################
# draw first bottom arrows
# rarrow("red",FLOWERSIZE)
# t.setx(0)
# t.sety(0)
# t.setheading(0)
# larrow("red",FLOWERSIZE)
t.setx(0)
t.sety(0)
t.setheading(0)

pallete = 0


this_color = clrs[pallete][level % len(clrs[pallete])]
if RANDCLR == 1:
    this_color = clrs[pallete][random.randint(0, COUNT - 1)]  # select a random color from the array of redefined colors

t.color(this_color)
t.forward(LENGTH)  # draw first vertical line

pos = t.position()  # store pos
current_x = pos[0]
current_y = pos[1]
t.speed(0)

positions = []

#################################################################
# draw the first bifurcation
#################################################################
# bifur(t, x, y, 0, "red", LENGTH,FLOWERSIZE, ANGLE)    # use hard coded color
current_heading = 0

# t.pensize(pensize)

bifur1angle = ANGLE
if CORES==2:
    bifur1angle = 60

bifur(t, current_x, current_y, current_heading, this_color, LENGTH, round((FLOWERSIZE/(COUNT-1))*0), bifur1angle, OUTLINE,OUTLINE_PENSIZE)  # use existing color
pi  = pi + 1 # counts lines drawn (forgot why :/ )

#################################################################
# loop thru he remaining 5 levels
#################################################################
# print(f"PENSIZE = {pensize}, LEVEL = {level}, COUNT= {COUNT - 1}, COLOR = {this_color}")

for level in range(0,COUNT-1):  # we reduce by one because the first bifurc is not in the loop
    this_color = clrs[pallete][(level+1) % len(clrs[pallete])]

    t.color(this_color)
    pensize = STYLE[(level+1) % len(STYLE)]
    # print(f"PENSIZE = {pensize}, LEVEL = {level}, COUNT= {COUNT-1}, COLOR = {this_color}")
    t.pensize(pensize)
    original_angle =  angle

    for i in range(len(positions)):
        new_ang_dev = ANG_DEVIATION
        new_len_dev = LEN_DEVIATION
        if SYNCPOINTS > 0:
            sync_angle = 15
            angslowdown = ANG_DEVIATION/sync_angle
            new_ang_dev = abs(ANG_DEVIATION - (angslowdown * (sync_angle - (ANGLE % sync_angle))   ))
            lenslowdown = LEN_DEVIATION/sync_angle
            new_len_dev = abs(LEN_DEVIATION - (lenslowdown * (sync_angle - (ANGLE % sync_angle))   ))

        # print(f"new_ang/len_dev: {new_ang_dev}/{new_len_dev}  - slowdown: {angslowdown} - ANGLE: {ANGLE} slowdown*ANGLE {(ANGLE-(ANGLE % 15))} ")

        newlen = random_deviate(LENGTH, new_len_dev,LEN_DEVIATION_r)  # get new length
        newang = random_deviate(ANGLE, new_ang_dev, ANG_DEVIATION_r)

        fSize = FLOWERSIZE
        if GROWFLOWER == 1:
              fSize = round((FLOWERSIZE/(COUNT-1))*(level+1))
        # print(positions)
        u = i
        if positions[u][3] == level:
            if level <= COUNT:
                if RANDCLR == 1:
                    this_color = clrs[pallete][random.randint(0, COUNT - 1)]  # select a random color from the array of redefined colors
                bifur(t, positions[u][0], positions[u][1], positions[u][2], this_color ,newlen,fSize, newang, OUTLINE,OUTLINE_PENSIZE)
    pi = pi + 1


t.setposition(1000, 1000)
t.color("white")

#os.system(f"mkdir {SUBDIR}")

if LOCKED == 0:
    exit()
#################################################################
# Image done - save to file
#################################################################
ts = t.getscreen()
ang = "{:03d}".format(int(ANGLE))

ts.getcanvas().postscript(file=f"{NAME}_{SERIES}/ORG/hex-{ang}.eps")
cmd = f"epstopdf {NAME}_{SERIES}/ORG/hex-{ang}.eps > /dev/null 2>&1"
# print(cmd)
os.system(cmd)

cmd = f"convert -rotate -90 -density 300 {NAME}_{SERIES}/ORG/hex-{ang}.pdf -quality 100 {NAME}_{SERIES}/ORG/hex-{ang}.gif > /dev/null 2>&1"
# print(cmd)
os.system(cmd)

cmd = f"/usr/sbin/sha256sum /home/jw/books/tholonia/code/hexani/{NAME}_{SERIES}/ORG/hex-{ang}.gif"

output = subprocess.getoutput(cmd)
rs = output.split(" ")
line = f"sha256: {rs[0]}"
filename = f"/home/jw/books/tholonia/code/hexani/{NAME}_{SERIES}/ORG/details/details_{NAME}_{SERIES}_{ANGLE}.txt"

f = open(filename, "a+")
f.write(f"{line}\n")
f.close()

# cmd = f"convert -rotate -90 -density 300 {sub}/hex-{ang}.pdf -quality 100 {sub}/hex-{ang}.jpg "
# print(cmd)
# os.system(cmd)
#
# cmd = f"convert -rotate -90 -density 300 {sub}/hex-{ang}.pdf -quality 100 {sub}/hex-{ang}.png "
# print(cmd)
# os.system(cmd)

cmd = f"rm {NAME}_{SERIES}/ORG/*.eps {NAME}_{SERIES}/ORG/*.pdf > /dev/null 2>&1 "
# print(cmd)
os.system(cmd)


# print('FINISHED')

