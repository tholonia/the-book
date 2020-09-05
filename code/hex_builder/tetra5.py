from vpython import *
# from visual import *
from pprint import *
import numpy as  np
from point2d import *
import math as math

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

scene = canvas(width=1024, height=700, background=color.white)

# lamp = local_light(pos=vector(2,2,-2),color=color.white)
#

print(scene.camera.pos)
print(scene.camera.axis)

scene.camera.pos = vector(0,0,0)

# see http://www.vb-helper.com/tutorial_platonic_solids.html



def rotz(src,dst, a):

    x = src[0]
    y = src[1]

    xm = dst[0]
    ym = dst[1]

    a = math.radians(a)
    xr = x + math.cos(a) * (xm - x) - math.sin(a) * (ym - y)
    yr = y + math.sin(a) * (xm - x) + math.cos(a) * (ym - y)

    return (xr, yr, dst[2])

def roty(src,dst, a):

    x = src[0]
    z = src[2]

    xm = dst[0]
    zm = dst[2]

    a = math.radians(a)
    xr = x + math.cos(a) * (xm - x) - math.sin(a) * (zm - z)
    zr = z + math.sin(a) * (xm - x) + math.cos(a) * (zm - z)

    return (xr, zr, dst[1])

def cosd(t):
    return np.degrees(cos(t))

def sind(t):
    return np.degrees(sin(t))

def calcP1(base,ctrpt=(0,0,0)):
    x = 0
    y = (base * sqrt(3)) - (base / sqrt(3))
    z = 0
    return (x+ctrpt[0], y+ctrpt[1], z+ctrpt[2])

def calcP2(base,ctrpt=(0,0,0)):
    x = base
    y = (base * -1) / sqrt(3)
    z = 0
    return (x+ctrpt[0], y+ctrpt[1], z+ctrpt[2])

def calcP3(base,ctrpt=(0,0,0)):
    x = (base * -1)
    y = (base * -1) / sqrt(3)
    z = 0
    return (x+ctrpt[0], y+ctrpt[1], z+ctrpt[2])

def calcP4(base,ctrpt=(0,0,0),flip=1):
    global tip
    x = 0
    y = 0
    z = tip*flip
    return (x+ctrpt[0], y+ctrpt[1], z+ctrpt[2])

def mdot(v, c):
    ball= sphere(pos=vector(v[0], v[1], v[2]), radius=.22, color=c,opacity=1,emissive=False)
    return ball

def rotary(l,y=0):
    # pprint(l)
    if len(l) == 0:
        return l
    y = -y % len(l)  # flip rotation direction
    m = l[y:] + l[:y]
    # pprint(m)
    return m

def dcurve(pos, p_clrs):
    curve(pos, color=p_clrs, radius=.2)

def dtet(hyp,ctrpt,rot):
    global tip
    base = (hyp / 2)   # = 1
    shortbase = base # * .88
    side = base * sqrt(3)
    B = (base * sqrt(3)) - (base / sqrt(3))
    tip = sqrt(hyp * hyp - B * B) * -1

    p_blue_dot = calcP1(shortbase,ctrpt)
    p_green_dot = calcP2(shortbase,ctrpt)
    p_red_dot = calcP3(shortbase,ctrpt)
    p_white_dot = calcP4(shortbase,ctrpt)

    p_clrs = rotary([BLUE,GREEN,RED],rot)

    b_ball = mdot(p_blue_dot, p_clrs[0])
    g_ball = mdot(p_green_dot, p_clrs[1])
    r_ball = mdot(p_red_dot, p_clrs[2])
    w_ball= mdot(p_white_dot, WHITE)

    scene.camera.pos = vector(p_white_dot[0],p_white_dot[1],10)
    scene.camera.follow(w_ball)
    # scene.camera.pos = vector(p_green_dot[0],p_green_dot[1],p_green_dot[2])
    # scene.camera.pos = vector(p_red_dot[0],p_red_dot[1],p_red_dot[2])

    distant_light(direction=vector(p_white_dot[0],p_white_dot[1],p_white_dot[2]), color=color.gray(0.15))

    # draw the base
    dcurve([p_blue_dot, p_green_dot], p_clrs[0])
    dcurve([p_green_dot, p_red_dot], p_clrs[1])
    dcurve([p_red_dot, p_blue_dot], p_clrs[2])

    dcurve([p_red_dot, p_white_dot], p_clrs[0])
    dcurve([p_blue_dot, p_white_dot], p_clrs[1])
    dcurve([p_green_dot, p_white_dot], p_clrs[2])

def ftet(hyp,ctrpt,rotclr,rotang):
    global tip
    base = (hyp / 2)   # = 1
    shortbase = base  #* .88
    side = base * sqrt(3)
    B = (base * sqrt(3)) - (base / sqrt(3))
    tip = sqrt(hyp * hyp - B * B) * -1
    p_clrs = rotary([BLUE,GREEN,RED],rotclr)

    p_white_dot = calcP4(shortbase, ctrpt,-1)
    # p_white_dot  = roty(p_white_dot, calcP4(shortbase, ctrpt), rotang)


    print(p_white_dot)
    p_blue_dot  = rotz(p_white_dot, calcP1(shortbase, ctrpt), rotang)
    p_green_dot = rotz(p_white_dot, calcP2(shortbase, ctrpt), rotang)
    p_red_dot   = rotz(p_white_dot, calcP3(shortbase, ctrpt), rotang)

    b_ball = mdot(p_blue_dot, p_clrs[0])
    g_ball = mdot(p_green_dot, p_clrs[1])
    r_ball = mdot(p_red_dot, p_clrs[2])
    w_ball = mdot(p_white_dot, WHITE)

    scene.camera.pos = vector(p_white_dot[0],p_white_dot[1],10)
    scene.camera.follow(w_ball)
    # scene.camera.pos = vector(p_green_dot[0],p_green_dot[1],p_green_dot[2])
    # scene.camera.pos = vector(p_red_dot[0],p_red_dot[1],p_red_dot[2])

    distant_light(direction=vector(p_white_dot[0],p_white_dot[1],p_white_dot[2]), color=color.gray(0.15))

    # draw the base
    dcurve([p_blue_dot, p_green_dot], p_clrs[0])
    dcurve([p_green_dot, p_red_dot], p_clrs[1])
    dcurve([p_red_dot, p_blue_dot], p_clrs[2])

    dcurve([p_red_dot, p_white_dot], p_clrs[0])
    dcurve([p_blue_dot, p_white_dot], p_clrs[1])
    dcurve([p_green_dot, p_white_dot], p_clrs[2])


# add virtual center tetra

# tips touchign bases
# dtet(2)
# rtet(-2)

# dtet(2)

dtet(1,(  0,  0,       0      ),0)
dtet(1,(-1, 0.86603*2, 0      ),2)
dtet(1,( 1, 0.86603*2, 0      ),1)



ftet(1,( 0,  .58*2,     -0  ),3,180)
# dtet(1,(0,-.57,-.82),3)
