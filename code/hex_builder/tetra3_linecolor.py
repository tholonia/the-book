from vpython import *
# from visual import *
from print import *



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

tip = 0;

scene = canvas(width=1024, height=700, background=color.black,stereo="crosseyed")

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
    p1 = (x, y, z)
    sphere(pos=vector(x, y, z), radius=.02, color=BLUE)

    x = base
    y = (base * -1) / sqrt(3)
    z = 0
    p2 = (x, y, z)
    sphere(pos=vector(x, y, z), radius=.02, color=color.green)

    x = (base * -1)
    y = (base * -1) / sqrt(3)
    z = 0
    p3 = (x, y, z)
    sphere(pos=vector(x, y, z), radius=.02, color=color.red)

    x = 0
    y = 0
    z = tip
    p4 = (x, y, z)
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

    p1 = (x, y, z)

    x = base
    y = (base * -1) / sqrt(3)
    z = +d

    p2 = (x, y, z)

    x = (base * -1)
    y = (base * -1) / sqrt(3)
    z = +d

    p3 = (x, y, z)

    x = 0
    y = 0
    z = tip + d

    p4 = [x, y, z]

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


def mdot(v, c):
    sphere(pos=vector(v[0], v[1], v[2]), radius=.04, color=c)


def itet(hyp, gen):
    global tip
    base = hyp / 2  # = 1
    side = base * sqrt(3)
    B = (base * sqrt(3)) - (base / sqrt(3))
    tip = sqrt(hyp * hyp - B * B)

    p_blue = calcP1(base)
    p_green = calcP2(base)
    p_red = calcP3(base)
    p_white = calcP4(base)

    # draw the base
    # ---------------------------------------------- cyan line
    mdot(p_blue, BLUE)
    curve(pos=[p_blue, p_green], color=CYAN)
    # ---------------------------------------------- cyan line child dot
    p_cyan = calcChildPt(p_blue, p_green)
    mdot(p_cyan, CYAN)

    # ---------------------------------------------- yellow line
    mdot(p_green, GREEN)
    curve(pos=[p_green, p_red], color=YELLOW)
    # ---------------------------------------------- yellow line child dot
    p_yellow = calcChildPt(p_green, p_red)
    mdot(p_yellow, YELLOW)

    # ---------------------------------------------- magenta line
    mdot(p_red, RED)
    curve(pos=[p_red, p_blue], color=MAGENTA)
    # ---------------------------------------------- red line child dot
    p_magenta = calcChildPt(p_red, p_blue)
    mdot(p_magenta, MAGENTA)




    # draw sides

    mdot(p_white, WHITE)

    p_lightred = calcChildPt(p_red, p_white)
    mdot(p_lightred, LIGHTRED)
    curve(pos=[p_red, p_white], color=LIGHTRED)

    p_lightblue = calcChildPt(p_blue, p_white)
    mdot(p_lightblue, LIGHTBLUE)
    curve(pos=[p_blue, p_white], color=LIGHTBLUE)

    p_lightgreen = calcChildPt(p_green, p_white)
    mdot(p_lightgreen, LIGHTGREEN)
    curve(pos=[p_green, p_white], color=LIGHTGREEN)

    # connect the dots

    curve(pos=[p_lightred, p_yellow], color=WHITE)
    curve(pos=[p_lightred, p_magenta], color=WHITE)
    curve(pos=[p_magenta, p_yellow], color=WHITE)

    curve(pos=[p_lightgreen, p_yellow], color=WHITE)
    curve(pos=[p_lightgreen, p_cyan], color=WHITE)
    curve(pos=[p_cyan, p_yellow], color=WHITE)

    curve(pos=[p_lightblue, p_cyan], color=WHITE)
    curve(pos=[p_lightblue,p_magenta], color=WHITE)
    curve(pos=[p_magenta,p_cyan], color=WHITE)

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
