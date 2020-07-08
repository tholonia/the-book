from vpython import *
# from visual import *
from print import *

tip = 0;

scene = canvas(width=1024, height=700, background=color.black)
# see http://www.vb-helper.com/tutorial_platonic_solids.html

def dtet(hyp):
    base = hyp / 2  # = 1
    side = base * sqrt(3)
    B = (base * sqrt(3)) - (base / sqrt(3))
    tip = sqrt(hyp * hyp - B * B)

    # p1 = ( 0 ,  (1 * sqrt(3)) - (1 / sqrt(3)) , 0)
    # p2 = ( 1 ,  -1 / sqrt(3)                  , 0)
    # p3 = (-1 ,  -1 / sqrt(3)                  , 0)

    x = 0
    y = (base * sqrt(3)) - (base / sqrt(3))
    z = 0
    p1 = (x,y,z)
    sphere(pos=vector(x,y,z), radius=.02, color=color.blue)

    x = base
    y = (base * -1) / sqrt(3)
    z = 0
    p2 = (x,y,z)
    sphere(pos=vector(x,y,z), radius=.02, color=color.green)

    x = (base * -1)
    y = (base * -1) / sqrt(3)
    z = 0
    p3 = (x,y,z)
    sphere(pos=vector(x, y, z), radius=.02, color=color.red)

    x = 0
    y= 0
    z = tip
    p4 = (x,y,z)
    sphere(pos=vector(x, y, z), radius=.02, color=color.white)

    # draw the base
    curve(pos=[p1, p2], color=color.blue)
    curve(pos=[p2, p3], color=color.green)
    curve(pos=[p3, p1], color=color.red)

    # draw side
    curve(pos=[p2, p4], color=color.cyan)
    curve(pos=[p1, p4], color=color.magenta)
    curve(pos=[p3, p4], color=color.yellow)

def rtet(hyp):
    base = hyp / 2  # = 1
    side = base * sqrt(3)
    B = (base * sqrt(3)) - (base / sqrt(3))
    tip = sqrt(hyp * hyp - B * B)
    tip = tip * -1

    # p1 = ( 0 ,  (1 * sqrt(3)) - (1 / sqrt(3)) , 0)
    # p2 = ( 1 ,  -1 / sqrt(3)                  , 0)
    # p3 = (-1 ,  -1 / sqrt(3)                  , 0)

    # p1 = (0, (base * sqrt(3)) - (base / sqrt(3)), 0)
    # p2 = (base, (base * -1) / sqrt(3), 0)
    # p3 = ((base * -1), (base * -1) / sqrt(3), 0)
    # # p4 = [0, 0, z]
    # p4 = [0, 0, 0]

    d = .817  # endges touching
    d = 1.618  # tips to bases

    x = 0
    y = (base * sqrt(3)) - (base / sqrt(3))
    z = +d

    p1 = (x,y,z)

    x = base
    y = (base * -1) / sqrt(3)
    z = +d

    p2 = (x,y,z)

    x = (base * -1)
    y = (base * -1) / sqrt(3)
    z = +d

    p3 = (x,y,z)

    x = 0
    y = 0
    z = tip +d

    p4 = [x,y,z]

    curve(pos=[p1, p2], color=color.red)
    curve(pos=[p2, p3], color=color.green)
    curve(pos=[p3, p1], color=color.blue)

    # draw side
    curve(pos=[p2, p4], color=color.cyan)
    curve(pos=[p1, p4], color=color.magenta)
    curve(pos=[p3, p4], color=color.yellow)

def calcP1(base):
    x = 0
    y = (base * sqrt(3)) - (base / sqrt(3))
    z = 0
    return(x,y,z)

def calcP2(base):
    x = base
    y = (base * -1) / sqrt(3)
    z = 0
    return(x,y,z)

def calcP3(base):
    x = (base * -1)
    y = (base * -1) / sqrt(3)
    z = 0
    return(x,y,z)


def calcP4(base):
    global tip
    x = 0
    y= 0
    z = tip
    return(x,y,z)

def calcNp1(a,b):
    x = (a[0] + b[0])/2
    y = (a[1] + b[1]) / 2
    z = (a[2] + b[2]) / 2
    return([x,y,z])

def mdot(v,c):
    sphere(pos=vector(v[0], v[1], v[2]), radius=.04, color=c)

def itet(hyp,gen):
    global tip
    base = hyp / 2  # = 1
    side = base * sqrt(3)
    B = (base * sqrt(3)) - (base / sqrt(3))
    tip = sqrt(hyp * hyp - B * B)

    N = calcP1(base)
    D = calcP2(base)
    C = calcP3(base)
    W = calcP4(base)

    child_N = calcNp1(N,D)
    mdot(child_N,color.green)

    child_D  = calcNp1(D,C)
    mdot(child_D,color.blue)

    child_C = calcNp1(C,N)
    mdot(child_C,color.red)

    # child_W = calcNp1(p4,p1)
    # sphere(pos=vector(np4[0],np4[1],np4[2]), radius=.02, color=color.yellow)

    # draw the base
    blueline = curve(pos=[N, D], color=color.blue)
    mdot(N,color.blue)
    greenline = curve(pos=[D, C], color=color.green)
    mdot(D,color.green)
    redline = curve(pos=[C, N], color=color.red)
    mdot(C,color.red)

    # draw side
    cyanline = curve(pos=[C, W], color=color.cyan)
    magentaline = curve(pos=[N, W], color=color.magenta)
    yellowline = curve(pos=[D, W], color=color.yellow)

    # draw inner
    # the BGR values have to be shifted by 1 to RBG for the child
    child_blueline = curve(pos=[child_D, child_C], color=color.blue)
    child_greenline = curve(pos=[child_C, child_N], color=color.green)
    child_redline = curve(pos=[child_N, child_D], color=color.red)

# tips touchign bases
# dtet(2)
# rtet(-2)

# dtet(2)
itet(2,2)
