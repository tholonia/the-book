#!/bin/python


from turtleplus import *
from pprint import pprint
import numpy as np
import random
from tkinterx import *
import os, sys, getopt, random, re
import subprocess
import toml
import functools
import time, datetime

sys.path.insert(1, '/home/jw/books/tholonia/code/hexani/')
import lapselib as ll

thisprog = os.path.basename(__file__)
ll.banner(thisprog)


def getOutlineVal(outline):
    # it is an int
    try:
        ok = int(outline)
        return (ok)
    except:
        pass
    # is it a hex color?

    if outline[0] == "#":
        return (outline)

        # is it a named color?
        # assume that of the first two filters fail it is a color name
    return (outline)

def bifur(bargs):
    global cc
    t.pendown()

    lp = draw_left_line(bargs)
    rp = draw_right_line(bargs)

    t.penup()
    cc = cc + 1

def draw_left_line(bargs):
    outline_pensize = bargs['outline_pensize']
    last_heading = bargs['last_heading']
    last_x = bargs['last_x']
    last_y = bargs['last_y']
    len = bargs['lenL']
    color = bargs['color']
    flowersize = bargs['flowersize']
    outline = bargs['outline']
    t = bargs['t']
    angle = bargs['angles'][1]
    level = bargs['level']


    # set the position to a previous point
    # global cpi
    global p
    # cpi = cpi + 1

    t.setheading(last_heading)
    t.penup()
    t.setposition(last_x, last_y)

    # draw the right line
    t.pendown()
    # pensize = t.pensize()  # save pensize
    # t.pensize(outline_pensize)  # get new pensize pensize
    t.left(angle)  # change direction
    t.forward(len)  # draw line
    # t.pensize(pensize)  # reset pensize
    # t.pensize(C['args']['style'][level + 1])  # reset pensize
    t.penup()

    angl = t.heading()

    lpos = t.position()  # store pos

    t.right(angle)  # turn left

    ldat = [lpos[0], lpos[1], angl, pi]

    if C['args']['show_left'] == True:
        larrow(bargs)
    positions.append(ldat)  # BAD

    return (ldat)

def draw_right_line(bargs):
    # global cpi
    global p

    outline_pensize = bargs['outline_pensize']
    last_heading = bargs['last_heading']
    last_x = bargs['last_x']
    last_y = bargs['last_y']
    len = bargs['lenR']
    color = bargs['color']
    flowersize = bargs['flowersize']
    outline = bargs['outline']
    t = bargs['t']
    angle = bargs['angles'][0]
    level = bargs['level']

    t.setheading(last_heading)
    t.penup()
    t.setposition(last_x, last_y)

    # draw the right line
    t.pendown()
    # pensize = t.pensize()  # save pensize
    # t.pensize(outline_pensize)  # get new pensize pensize
    t.right(angle)  # change direction
    t.forward(len)  # draw line
    # t.pensize(pensize)  # reset pensize
    t.penup()

    angr = t.heading()  # save heading coords
    # t.dot(25)

    rpos = t.position()  # store pos    # get the position
    rx = rpos[0]
    ry = rpos[1]

    rpos = t.position()  # get the end point position

    t.left(angle)  # face front

    rdat = [rpos[0], rpos[1], angr, pi]

    if C['args']['show_right'] == True:
        rarrow(bargs)
    positions.append(rdat)

    makedot(t, DOTS[0], DOTS[1], level) # we draw the dot AFTER the last lines have been drawn



    return (rdat)

def larrow(bargs):

    clr             = bargs['color']
    flowersize      =  bargs['flowersize']
    outline         = bargs['outline']
    t               = bargs['t']
    angle           = bargs['angles'][1]
    outline_pensize = bargs['outline_pensize']
    length          = bargs['lenL']
    baselength      = bargs['baselength']

    colormode(255)
    # t.dot(10)
    lpos = t.position()  # store pos
    lx = lpos[0]
    ly = lpos[1]
    h = t.heading()

    # get pensize
    org_pensize = t.pensize()
    org_pencolor = t.pencolor()
    org_fillcolor = t.fillcolor()

    # set new vals
    t.pensize(outline_pensize)
    new_fillcolor = clr[C['args']['flowerpalette']]
    t.fillcolor(new_fillcolor)
    t.pencolor(clr[C['args']['stempalette']])

    outline = getOutlineVal(outline)
    if type(outline) is str:
        t.pencolor(outline)
    else:
        t.pencolor(calcColor(new_fillcolor, outline))

    ratio = 1
    # IF THE BASELENGTH = 0, CRASHES
    try:
        ratio = length/baselength
        try:
            if C['args']['floDev'] == True:
                flowersize = flowersize * ratio
        except:
            pass
    except:
        pass


    # draw and fill
    t.pendown()
    t.begin_fill()
    t.left(angle * 3.5)  # 'angle' = 60 default - point back 210 deg (180+30 = 60 * 3.5)
    t.forward(flowersize)
    t.left(angle * 2)  # 120    # point back to right angle of stem (90+30 = 60 * 2)
    t.forward(flowersize / 2)
    t.left(angle * 1.5)  # 90   # were now back on the stem so we go forward to the point where it started
    t.forward(flowersize * .8)
    t.end_fill()
    t.penup()

    # reset values
    t.pensize(org_pensize)
    t.pencolor(rgb2hex(org_pencolor))
    t.fillcolor(rgb2hex(org_fillcolor))
    # t.heading(org_heading)
    t.setx(lx)
    t.sety(ly)

def rarrow(bargs):

    clr             = bargs['color']
    flowersize      =  bargs['flowersize']
    outline         = bargs['outline']
    t               = bargs['t']
    angle           = bargs['angles'][0]
    outline_pensize = bargs['outline_pensize']
    length          = bargs['lenR']
    baselength      = bargs['baselength']

    colormode(255)
    # t.dot(10)

    rpos = t.position()  # store pos
    rx = rpos[0]
    ry = rpos[1]

    # get pensize
    org_pensize = t.pensize()
    org_pencolor = t.pencolor()
    org_fillcolor = t.fillcolor()

    # set new vals
    t.pensize(outline_pensize)
    new_fillcolor = clr[C['args']['flowerpalette']]
    t.fillcolor(new_fillcolor)
    t.pencolor(clr[C['args']['stempalette']])

    outline = getOutlineVal(outline)
    if type(outline) is str:
        t.pencolor(outline)
    else:
        t.pencolor(calcColor(new_fillcolor, outline))


    try:
        ratio = length/baselength
        try:
            if C['args']['floDev'] == True:
                flowersize = flowersize * ratio
        except:
            pass
    except:
        pass

    # draw and fill
    t.pendown()
    t.begin_fill()
    t.right(angle * 3.5)  # 'angle' = 60 default - point back 210 deg (180+30 = 60 * 3.5)
    t.forward(flowersize)
    t.right(angle * 2)  # 120    # point back to right angle of stem (90+30 = 60 * 2)
    t.forward(flowersize / 2)
    t.right(angle * 1.5)  # 90   # were now back on the stem so we go forward to the point where it started
    t.forward(flowersize * .8)
    t.end_fill()
    t.penup()

    # reset values
    t.pensize(org_pensize)
    t.pencolor(rgb2hex(org_pencolor))
    t.fillcolor(rgb2hex(org_fillcolor))
    # t.heading(org_heading)
    t.setx(rx)
    t.sety(ry)

def diff(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)

def change_color(t):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    t.color(R, G, B)

def getContrastReverse(color):
    if (color[0]) == "#":
        color = color[1:]

        rh = color[0:2]
        gh = color[2:4]
        bh = color[4:6]


    rd = 255 - color[0]
    gd = 255 - color[1]
    bd = 255 - color[2]

    rh = hex(int(rd))[2:].zfill(2)
    gh = hex(int(gd))[2:].zfill(2)
    bh = hex(int(bd))[2:].zfill(2)

    newcolor = f"#{rh}{gh}{bh}"
    return (newcolor)

def getContrastComplementary(color):
    if len(color) == 3: #we have a turtle color
        rh = str(hex(int(color[0]))).zfill(2)[2:]
        gh = str(hex(int(color[0]))).zfill(2)[2:]
        bh = str(hex(int(color[0]))).zfill(2)[2:]
        color = f"{rh}{gh}{bh}"

    if color[0] == "#": #we have a hex color
        color = color[1:]

    # strip the # from the beginning
    # color = color[1:]

    # convert the string into hex
    color = int(color, 16)

    # invert the three bytes
    # as good as substracting each of RGB component by 255(FF)
    comp_color = 0xFFFFFF ^ color

    # convert the color back to hex by prefixing a #
    comp_color = "#%06X" % comp_color

    # return the result
    # print(f"COMPLEMENTARY COLOR: {comp_color}")
    return f"{comp_color}"

def getContrast120(color):
    # print(color)
    rh = str(hex((int(color[0]) + 85) % 255)).zfill(2)[2:]
    gh = str(hex((int(color[1]) + 85) % 255)).zfill(2)[2:]
    bh = str(hex((int(color[2]) + 85) % 255)).zfill(2)[2:]

    color = f"{rh}{gh}{bh}".zfill(6)
    # print(f"CONTRAST HEX COLOR: {color}")
    return (f"#{color}")

def getContrastbyDeg(color, deg):
    def gcbd(hv,deg):
        cv = int(deg * 1.422) % 256

        hi = int(hv,16)
        # ri = int(hi * cv) % 255
        comp_color = cv ^ hi
        # print(f"{cv}^{hi}")
        cc = hex(comp_color)
        return(cc[2:])
    rh=""
    gh=""
    bh=""
    if len(color) == 3: #we have a turtle color
        rh = str(hex(int(color[0]))).zfill(2)[2:]
        gh = str(hex(int(color[1]))).zfill(2)[2:]
        bh = str(hex(int(color[2]))).zfill(2)[2:]
        color = f"{rh}{gh}{bh}"
    if (color[0]) == "#":
        color = color[1:]
        rh = color[0:2]
        gh = color[2:4]
        bh = color[4:6]
        # print(rh,gh,bh)
    rv = gcbd(rh,deg)
    gv = gcbd(gh,deg)
    bv = gcbd(bh,deg)

    cs = f"{rv}{gv}{bv}"
    cs = cs.zfill(6)
    return(f"#{cs}")

# def xxxxxgetContrastbyDeg(color, deg):
#     if len(color) == 3: #we have a turtle color
#         rh = str(hex(int(color[0]))).zfill(2)[2:]
#         gh = str(hex(int(color[0]))).zfill(2)[2:]
#         bh = str(hex(int(color[0]))).zfill(2)[2:]
#         color = f"{rh}{gh}{bh}"
#
#     if color[0] == "#": #we have a hex color
#         color = color[1:]
#
#     color = int(color, 16)
#
#
#     # get the vale for offset
#     ioffset = deg*1.422 % 255
#     # make hex str
#     hoffset = str(hex(int(ioffset)))[2:].zfill(2)
#     # make color string
#     soffset = f"{hoffset}{hoffset}{hoffset}"
#     # convert back to int
#     ics =  f"0x{int(soffset, 16)}")
#
#     comp_color = isc ^ color
#
#     # convert the color back to hex by prefixing a #
#     comp_color = "#%06X" % comp_color
#
#     # return the result
#     print(f"COMPLEMENTARY COLOR: {comp_color}")
#     return f"{comp_color}"
#     # ====
#     # offset = int(deg * ((255 / 360) * deg))
#     # rh = str(hex((int(color[0]) + offset) % 255)).zfill(2)[2:]
#     # gh = str(hex((int(color[1]) + offset) % 255)).zfill(2)[2:]
#     # bh = str(hex((int(color[2]) + offset) % 255)).zfill(2)[2:]
#     #
#     # color = f"{rh}{gh}{bh}".zfill(6)
#     # print(f"CONTRAST by {deg}: {color} ")
#     # return (f"#{color}")

def calcColor(color, type):
    return getContrastbyDeg(color, type)

def rgb2hex(ca):
    rs = str(hex(int(ca[0]) % 255))[2:].zfill(2)
    gs = str(hex(int(ca[1]) % 255))[2:].zfill(2)
    bs = str(hex(int(ca[2]) % 255))[2:].zfill(2)
    return (f"#{rs}{gs}{bs}")

def pause():
    t.getscreen()._root.mainloop()

def makedot(t, color, size, level):
    if size != 0:
        try:
            size = int(size)
        except:
            # no 0 and not an int, assume function
            if size == "level_x_2":
                size = level * 2

    if color != 0:

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",size, level)
        org_pencolor = t.pencolor()
        org_fillcolor = t.fillcolor()

        t.fillcolor(color)
        t.pencolor(color)

        t.dot(size)

        t.pencolor(rgb2hex(org_pencolor))
        t.fillcolor(rgb2hex(org_fillcolor))

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
        shortargs = shortargs + k

    sargs = ""
    shortargsAry = []
    for a in myargs.values():
        a = a.replace(":", "")
        a = f"-{a}"
        shortargsAry.append(a)
        sargs = sargs + a

    largs = []
    for a in myargs.keys():
        a = a.replace("=", "")
        a = f"--{a}"
        largs.append(a)

    comp = {}
    for i in range(0, len(largs)):
        # print(largs[i])
        # print(shortargsAry[i])
        comp[largs[i]] = shortargsAry[i]
    # print(comp)
    # print(sargs)
    # print(largs)
    #
    return longargs, shortargs, comp

def getALLangles(counter, lo, hi):
    def getangle(l, t):
        t = 30
        for k in range(0, 361):
            j = int(k / 30)
            s = 1 if j % 2 == 0 else -1
            t = t + s
            if (k == l):
                return (t)

    rary = []

    for r in range(0, 361):
        x = getangle(r, counter)
        rary.append(x)
    na = np.interp(rary, (min(rary), max(rary)), (lo, hi))
    ab = []
    for i in range(0, 361):
        ab.append(round(na[i]))
    return (ab)



# ----------------------------------------------------------
#################################################################
# define default vals
#################################################################

# -- load config data ------------
cwd = os.getcwd()
angle = 60
nameangle = angle
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "a:", ["angle="])
except getopt.GetoptError as err:
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-a", "--angle"):
        angle = arg
        nameangle = arg

wpath = f"{cwd}"
C = toml.load(f"{wpath}/build.toml")
WD = C['def']['root']
REPO = C['def']['repo']
# -- end load -----------------------

# ANGLE           = C['args']['angle'] #60
ANGLE = int(angle)

USECOLOR = C['args']['usecolor'][0]
USE_ALT_COLOR = C['args']['usecolor'][1]
LENGTH = C['args']['length']  # "60,0,'':60,0,''"  # length of lines, right, left
LENGTHR = int(C['args']['length'][0][0])  # 60  # length of line
LENGTHL = int(C['args']['length'][1][0])  # 60  # length of line
LRSUB = int(C['args']['length'][0][1])  # 0
LLSUB = int(C['args']['length'][1][1])  # 0
LRFUN = C['args']['length'][0][2]  # "NULL"
LLFUN = C['args']['length'][1][2]  # "NULL"
INCREMENT = "???"
# _ANG_DEVIATION  = C['args']['angDev'] #0 #.60 # parameters for relative angle - percantage 0.6 = 60% || [0,1] # .6 # parameters for length/angle variance
ANG_DEVIATION = C['args']['angDev'][0]  # _ANG_DEVIATION[0]
ANG_DEVIATION_r = C['args']['angDev'][1]  # _ANG_DEVIATION[1]
# _LEN_DEVIATION  = C['args']['lenDev'] #[0,0] #.1
LEN_DEVIATION = C['args']['lenDev'][0]  # _LEN_DEVIATION[0]
LEN_DEVIATION_r = C['args']['lenDev'][1]  # _LEN_DEVIATION[1]
SUBDIR = f"{C['def']['name']}_{C['def']['series']}"  # "ani_3"
COUNT = C['args']['ncount']  # 6
STYLE = C['args']['style']  # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
FLOWERSIZE = C['args']['flowersize']  # 15
LOCKED = C['def']['desklock']  # 1
OUTLINE = int(C['args']['outline'][0])  # "0"
OUTLINE_PENSIZE = int(C['args']['outline'][1])
GROWFLOWER = C['args']['growflower']  # 0
NAME = C['def']['name']  # "name"
SERIES = C['def']['series']  # "series"
SYNCPOINTS = C['args']['syncpoints']  # 0
CORES = C['args']['cores']  # 1
RANDCLR = C['args']['randclr']  # 0
DOTS =  [0,0]
try:
    if C['args']['dot'][0] != 0:
        DOTS = C['args']['dot']
except:
    pass


print(f"LOADING: colordata/{int(ANGLE)}.npy", flush=True)
colors = np.load(f"{REPO}/colordata/{int(ANGLE)}.npy", allow_pickle=True)
clr1 = colors.item().get(USECOLOR)
clr2 = colors.item().get(USE_ALT_COLOR)

quiet = ""  # > /dev/null 2>&1"

clrs = [clr1, clr2]
#################################################################
# define other vars
#################################################################

angle = 60  # 5 # angle of separation
cc = 0
pi = 0
level = 0  # set first level
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

screen.setup(1200, 1200)
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

# this_color = clrs[pallete][level % len(clrs[pallete])]


# c1 = clrs[0][level % len(clrs[0])]
# c2 = clrs[C['args']['flowerpalette']][level % len(clrs[C['args']['flowerpalette']])]

c1 = clrs[C['args']['stempalette']][level % len(clrs[C['args']['stempalette']])]
c2 = clrs[C['args']['flowerpalette']][level % len(clrs[C['args']['flowerpalette']])]

this_color_ary = [c1, c2]  # array of two colors

if RANDCLR == True:
    c1 = clrs[C['args']['stempalette']][random.randint(0, COUNT - 1)]  # select a random color from the array of redefined colors
    c2 = clrs[C['args']['flowerpalette']][random.randint(0, COUNT - 1)]  # select a random color from the array of redefined colors

    this_color_ary = [c1, c2]

t.color(this_color_ary[0])  # set color of stems
t.forward(LENGTHR)  # draw first vertical line
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

bifur1angle = ANGLE  # use calculated ang;e
if CORES  == 2:  # unless it has two cores, then hard code the angle
    bifur1angle = 60

bifur1angles = [bifur1angle, bifur1angle]  # the argument expects an array for levels > 1, so we use an array here as well

bargs = {
    't': t,
    'last_x': current_x,
    'last_y': current_y,
    'last_heading': current_heading,
    'color': this_color_ary,
    'lenR': LENGTHR,
    'lenL': LENGTHR,
    'flowersize': round((FLOWERSIZE / (COUNT - 1)) * 0),
    'angles': bifur1angles,
    'outline': OUTLINE,
    'outline_pensize': OUTLINE_PENSIZE,
    'pensize': C['args']['style'][level],
    'level': level,
    'baseangle': nameangle,
    'baselength': LENGTHR

}

bifur(bargs)

# use existing color

# bifur(t, current_x, current_y, current_heading, this_color, LENGTHR, LENGTHL, round((FLOWERSIZE/(COUNT-1))*0), bifur1angles, OUTLINE,OUTLINE_PENSIZE, level)  # use existing color
pi = pi + 1  # counts lines drawn (forgot why :/ )

#################################################################
# loop thru he remaining 5 levels
#################################################################
# print(f"PENSIZE = {pensize}, LEVEL = {level}, COUNT= {COUNT - 1}, COLOR = {this_color}")

# anglesLengthList_60_20_80 = getALLangles(60, 20, 80)

aLL_big = getALLangles(60, 10, 25)
aLL_small = getALLangles(60, 25, 50)
big_osc = getALLangles(60, 10, 60)
osc_btn_20_and_80 = getALLangles(60, 20, 80)

for level in range(0, COUNT - 1):  # we reduce by one because the first bifurc is not in the loop

    baselength = LENGTHR

    # adjust lengths
    if (LRSUB > 0):
        LENGTHR = LENGTHR + ANGLE
        LENGTHR = 60 if ((LRFUN == "stop_at_60") and (LENGTHR > 60)) else LENGTHR
        LENGTHR = aLL_big[ANGLE] if LRFUN == "osc_aLL_big" else LENGTHR
        LENGTHR = aLL_small[ANGLE] if LRFUN == "osc_aLL_small" else LENGTHR
        LENGTHR = big_osc[ANGLE] if LRFUN == "big_osc" else LENGTHR
        LENGTHR = osc_btn_20_and_80[ANGLE] if LRFUN == "osc_btn_20_and_80" else LENGTHR
    if (LLSUB > 0):
        LENGTHL = LENGTHL + ANGLE
        LENGTHL = 60 if ((LLFUN == "stop_at_60") and (LENGTHL > 60)) else LENGTHL
        LENGTHL = aLL_big[ANGLE] if LLFUN == "osc_aLL_big" else LENGTHL
        LENGTHL = aLL_small[ANGLE] if LLFUN == "osc_aLL_small" else LENGTHL
        LENGTHL = big_osc[ANGLE] if LLFUN == "big_osc" else LENGTHL
        LENGTHL = osc_btn_20_and_80[ANGLE] if LLFUN == "osc_btn_20_and_80" else LENGTHL

    # print(f"LEN (right):  {LENGTHR}")
    # print(f"LEN  (left):  {LENGTHL}")

    #this_color = clrs[C['args']['stempalette']][(level+1) % len(clrs[C['args']['stempalette']])]

    # print(f"======================= {this_color}")  ['#f58df8', '#bbbb06']

    t.color(this_color_ary[0])
    pensize = STYLE[(level + 1) % len(STYLE)]
    # print(f"PENSIZE = {pensize}, LEVEL = {level}, COUNT= {COUNT-1}, COLOR = {this_color}")
    t.pensize(pensize)
    original_angle = angle

    for i in range(len(positions)):
        new_ang_dev = ANG_DEVIATION
        new_len_dev = LEN_DEVIATION
        if SYNCPOINTS > 0:
            sync_angle = 15
            angslowdown = ANG_DEVIATION / sync_angle
            new_ang_dev = abs(ANG_DEVIATION - (angslowdown * (sync_angle - (ANGLE % sync_angle))))
            lenslowdown = LEN_DEVIATION / sync_angle
            new_len_dev = abs(LEN_DEVIATION - (lenslowdown * (sync_angle - (ANGLE % sync_angle))))

        # print(f"new_ang/len_dev: {new_ang_dev}/{new_len_dev}  - slowdown: {angslowdown} - ANGLE: {ANGLE} slowdown*ANGLE {(ANGLE-(ANGLE % 15))} ")

        newlenR = random_deviate(LENGTHR, new_len_dev, LEN_DEVIATION_r)  # get new length
        newlenL = random_deviate(LENGTHL, new_len_dev, LEN_DEVIATION_r)  # get new length
        newang = random_deviate(ANGLE, new_ang_dev, ANG_DEVIATION_r)

        newangles = [newang, newang]
        newangles[0] = newangles[0] + C['args']['hardangle'][0]
        newangles[1] = newangles[1] + C['args']['hardangle'][1]

        fSize = FLOWERSIZE
        if GROWFLOWER == 1:
            fSize = round((FLOWERSIZE / (COUNT - 1)) * (level + 1))
        # print(positions)
        u = i

        # newangles=[60,60]

        if positions[u][3] == level:  #3

            # if (level <= (CORES - 1)):
                # newangles = [60,60]


            c1 = clrs[C['args']['stempalette']][level % len(clrs[C['args']['stempalette']])]
            c2 = clrs[C['args']['flowerpalette']][level % len(clrs[C['args']['flowerpalette']])]

            if level <= COUNT:
                if RANDCLR == True:
                    c1 = clrs[C['args']['stempalette']][random.randint(0, COUNT - 1)]  # select a random color from the array of redefined colors
                    c2 = clrs[C['args']['flowerpalette']][random.randint(0, COUNT - 1)]  # select a random color from the array of redefined colors
                this_color_ary = [c1, c2]
                bargs = {
                    't': t,
                    'last_x': positions[u][0],
                    'last_y': positions[u][1],
                    'last_heading': positions[u][2],
                    'color': this_color_ary,
                    'lenR': newlenR,
                    'lenL': newlenL,
                    'flowersize': fSize,
                    'angles': newangles,
                    'outline': OUTLINE,
                    'outline_pensize': OUTLINE_PENSIZE,
                    'pensize': C['args']['style'][level+1],
                    'level': level,
                    'baseangle':nameangle,
                    'baselength': baselength
                }
                bifur(bargs)
    pi = pi + 1

t.setposition(1000, 1000)
t.color("white")

# os.system(f"mkdir {SUBDIR}")

if LOCKED == 0:
    exit()
#################################################################
# Image done - save to file
#################################################################
ts = t.getscreen()
ANGLE = nameangle
ang = "{:03d}".format(int(ANGLE))

# ts.getcanvas().postscript(file=f"{NAME}_{SERIES}/ORG/hex-{ang}.eps")
ts.getcanvas().postscript(file=f"/tmp/hex-{ang}.eps")
# cmd = f"epstopdf {NAME}_{SERIES}/ORG/hex-{ang}.eps"
cmd = f"epstopdf /tmp/hex-{ang}.eps"
# print(cmd)
ll.runthis(cmd)

# cmd = f"convert -rotate -90 -density 300 {NAME}_{SERIES}/ORG/hex-{ang}.pdf -quality 100 {NAME}_{SERIES}/ORG/hex-{ang}.gif {quiet}"
cmd = f"convert -rotate -90 -density 300 /tmp/hex-{ang}.pdf -quality 100 {WD}/ORG/hex-{ang}.gif"
# print(cmd)
ll.runthis(cmd)

cmd = f"/usr/sbin/sha256sum {WD}/ORG/hex-{ang}.gif"

# write to file

t = datetime.datetime.fromtimestamp(time.time())
ts = t.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)")

desc = f"Title: {C['def']['name']}\n"
desc = desc + f"Series: {C['def']['series']}\n"
desc = desc + f"Sequence: {nameangle}\n"
desc = desc + f"File 1/2: ANI_{C['def']['name']}_{C['def']['name']}_ALL.gif\n"
desc = desc + f"File 2/2: ANI_{C['def']['name']}_{C['def']['name']}_UNI.gif\n"
desc = desc + "----------------------------------------------------\n"
desc = desc + "\nCONFIG VARS FOR THIS IMAGE\n"
desc = desc + ll.listArgs(C)

desc = desc + "\nFILE DETAILS\n"

output = subprocess.getoutput(cmd)
rs = output.split(" ")
desc = desc + f"sha256: {rs[0]}\n"
desc = desc + f"Created: {ts}\n"

filename = f"{WD}/ORG/details/details_{NAME}_{SERIES}_{ANGLE}.txt"

f = open(filename, "a+")
f.write(desc)
f.close()

# cmd = f"convert -rotate -90 -density 300 {sub}/hex-{ang}.pdf -quality 100 {sub}/hex-{ang}.jpg "
# print(cmd)
# os.system(cmd)
#
# cmd = f"convert -rotate -90 -density 300 {sub}/hex-{ang}.pdf -quality 100 {sub}/hex-{ang}.png "
# print(cmd)
# os.system(cmd)

# cmd = f"rm {NAME}_{SERIES}/ORG/*.eps {NAME}_{SERIES}/ORG/*.pdf {quiet} "
# print(cmd)
# os.system(cmd)


# print('FINISHED')
