from vpython import *
# from visual import *
from print import *


# actual colors

RED = color.red
GREEN = color.green
BLUE = color.blue

YELLOW = color.yellow
CYAN = color.cyan
MAGENTA = color.magenta
WHITE = color.white

LIGHTYELLOW = vector(1,1,.5) #255,255,128)
LIGHTCYAN =  vector(.5,1,1)
LIGHTMAGENTA = vector(1,.5,1)

LIGHTRED = vector(1,.5,.5) #255,255,128)
LIGHTGREEN =  vector(.5,1,.5)
LIGHTBLUE = vector(.5,.5,1)

REDREDGREEN = vector(.66,.33,0)
GREENGREENRED = vector(.33,.66,0)
#overridecolors
#
# RED = color.red
# GREEN = color.green
# BLUE = color.blue
#
# YELLOW = color.green
# CYAN = color.blue
# MAGENTA = color.red
# WHITE = color.white
#
# LIGHTYELLOW = color.yellow
# LIGHTCYAN =  color.blue
# LIGHTMAGENTA = color.red
#
# LIGHTRED = color.red
# LIGHTGREEN =  color.green
# LIGHTBLUE = color.blue



tip = 0;

scene = canvas(width=1024, height=700, background=color.black,stereo="crosseyed")

# see http://www.vb-helper.com/tutorial_platonic_solids.html


def calcP1(base):
    x = 0
    y = (base * sqrt(3)) - (base / sqrt(3))
    z = 0
    return (x, y, z)


def calcP2(base):
    x = base
    y = (base * -1) / sqrt(3)
    z = 0
    return (x, y, z)


def calcP3(base):
    x = (base * -1)
    y = (base * -1) / sqrt(3)
    z = 0
    return (x, y, z)


def calcP4(base):
    global tip
    x = 0
    y = 0
    z = tip
    return (x, y, z)


def calcChildPt(a, b):
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    z = (a[2] + b[2]) / 2
    return ([x, y, z])


def mdot_ggr(v, c):
    sphere(pos=vector(v[0], v[1], v[2]), radius=.1, color=c, texture="map_ggr.png")

def mdot_dot(v, clr):
    sphere(pos=vector(v[0], v[1], v[2]), radius=.1, color=clr)

def mdot(v, c):
    sphere(pos=vector(v[0], v[1], v[2]), radius=.1, color=c)

def mdot0(v, c):
    sphere(pos=vector(v[0]-.01, v[1]-.01, v[2]-.01), radius=.1, color=c)

def drawline(p1,p2,clr):

    x1 = p1[0] *.9
    y1 = p1[1] *.9
    z1 = p1[2] *.9
    x2 = p2[0] * 1.1
    y2 = p2[1] * 1.1
    z2 = p2[2] * 1.1

    curve(pos=[vector(x1,y1,z1), vector(x2,y2,z2)], color=clr)
    mdot_dot((x1,y1,z1), BLUE)
    mdot_dot((x2,y2,z2), GREEN)


def itet(hyp, gen):
    global tip
    base = hyp / 2  # = 1
    side = base * sqrt(3)
    B = (base * sqrt(3)) - (base / sqrt(3))
    tip = sqrt(hyp * hyp - B * B)

    p_blue_dot = calcP1(base)
    p_green_dot = calcP2(base)
    p_red_dot = calcP3(base)
    p_white = calcP4(base)

    # draw the base
    # ---------------------------------------------- cyan/blue line
    # mdot(p_blue_dot, BLUE)
    drawline(p_blue_dot, p_green_dot,WHITE)
    # ---------------------------------------------- cyan/blue line child dot
    p_cyan_dot = calcChildPt(p_blue_dot, p_green_dot)
    # mdot(p_cyan_dot, GREEN)

    # ---------------------------------------------- yellow/green line
    # mdot(p_green_dot, RED)
    drawline(p_green_dot, p_red_dot, WHITE)
    # ---------------------------------------------- yellow/green line child dot
    p_yellow_dot = calcChildPt(p_green_dot, p_red_dot)
    # mdot(p_yellow_dot, BLUE) #YELLOW

    # ---------------------------------------------- magenta/red line
    # mdot(p_red_dot, GREEN)
    drawline(p_red_dot, p_blue_dot,WHITE)


    # ---------------------------------------------- red/red line child dot
    p_magenta_dot = calcChildPt(p_red_dot, p_blue_dot)
    # mdot(p_magenta_dot, RED)

    # draw sides

    mdot(p_white, WHITE)

    p_lightred_dot = calcChildPt(p_red_dot, p_white)
    # mdot(p_lightred_dot, WHITE)
    drawline(p_red_dot, p_white,WHITE)

    p_lightblue_dot = calcChildPt(p_blue_dot, p_white)
    # mdot(p_lightblue_dot, WHITE)
    drawline(p_blue_dot, p_white,WHITE)

    p_lightgreen_dot = calcChildPt(p_green_dot, p_white)
    # mdot(p_lightgreen_dot, WHITE)
    drawline(p_green_dot, p_white,WHITE)

    # connect the dots

    curve(pos=[p_lightred_dot, p_yellow_dot], color=WHITE)
    curve(pos=[p_lightred_dot, p_magenta_dot], color=WHITE)
    curve(pos=[p_magenta_dot, p_yellow_dot], color=WHITE)

    curve(pos=[p_lightgreen_dot, p_yellow_dot], color=WHITE)
    curve(pos=[p_lightgreen_dot, p_cyan_dot], color=WHITE)
    curve(pos=[p_cyan_dot, p_yellow_dot], color=WHITE)

    curve(pos=[p_lightblue_dot, p_cyan_dot], color=WHITE)
    curve(pos=[p_lightblue_dot,p_magenta_dot], color=WHITE)
    curve(pos=[p_magenta_dot,p_cyan_dot], color=WHITE)

    curve(pos=[p_lightblue_dot, p_lightgreen_dot], color=WHITE)
    curve(pos=[p_lightblue_dot,p_lightred_dot], color=WHITE)
    curve(pos=[p_lightred_dot,p_lightgreen_dot], color=WHITE)

    quit()
    mdot(child_C, LIGHTREDWHITE)

    mdot(C, WHITE)


    quit()
    # ---------------------------------------------- white line
    mdot(C, RED)
    redline = curve(pos=[C, N], color=RED)
    # ---------------------------------------------- white line child dot
    child_W = calcChildPt(C, W)
    mdot(child_C, WHITE)

    quit()


    child_W = calcChildPt(C, W)
    mdot(child_C, color.white)

    X = calcNp1(C, W)
    mdot(X, color.yellow)

    # mdot(child_C,color.white)

    # child_W = calcNp1(p4,p1)
    # sphere(pos=vector(np4[0],np4[1],np4[2]), radius=.02, color=color.yellow)

    # draw inner
    # the BGR values have to be shifted by 1 to RBG for the child
    child_blueline = curve(pos=[child_D, child_C], color=color.blue)
    child_greenline = curve(pos=[child_C, child_N], color=color.green)
    child_redline = curve(pos=[child_N, child_D], color=color.red)
    child_whiteline = curve(pos=[child_C, child_W], color=color.white)


# tips touchign bases
# dtet(2)
# rtet(-2)

# dtet(2)
itet(2, 2)
