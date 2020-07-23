# example:
# python ./hex_builder_lapse.py -l 25 -e 0 -f 60 -t 60





from turtleplus import *
from pprint import pprint
import numpy as np
import random
from tkinterx import *
import os, sys, getopt






def diff(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)


def change_color(t):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    t.color(R, G, B)


def dl(t, lx, ly, h, clr):
    # set the position to a previous point
    global cpi
    global p
    cpi = cpi + 1

    t.setheading(h)
    t.penup()
    t.setposition(lx, ly)
    t.pendown()

    # drae the left line
    t.left(angle)  # turn left
    t.forward(L)  # drawl line

    angl = t.heading()
    # t.dot(20)

    # get the end poijt position
    lpos = t.position()  # store pos
    t.right(angle)  # face front

    ldat = [lpos[0], lpos[1], angl, pi]

    larrow(clr);
    poss.append(ldat)

    return (ldat)


def dr(t, lx, ly, h, clr):
    global cpi
    global p
    t.setheading(h)
    t.penup()
    t.setposition(lx, ly)
    t.pendown()

    # draw the right line
    t.right(angle)
    t.forward(L)

    cpi = cpi + 1
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

    poss.append(rdat)
    rarrow(clr);
    return (rdat)


def larrow(clr):
    t.fillcolor(clr)
    t.begin_fill()

    t.left(angle * 3.5)  # 210)
    t.forward(sz)

    t.left(angle * 2)  # 120)
    t.forward(sz / 2)

    t.left(angle * 1.5)  # 90)
    t.forward(sz * .8)

    t.end_fill()


def rarrow(clr):
    t.fillcolor(clr)
    t.begin_fill()

    t.right(angle * 3.5)  # 210
    t.forward(sz)

    t.right(angle * 2)  # 120)
    t.forward(sz / 2)

    t.right(angle * 1.5)  # 90)
    t.forward(sz * .8)

    t.end_fill()


def pause():
    t.getscreen()._root.mainloop()


def bifur(t, lx, ly, h, clr):
    global cc
    lp = dl(t, lx, ly, h, clr)
    rp = dr(t, lx, ly, h, clr)
    # print ("------",cc)
    cc = cc + 1
    # print ("++++++",cc)


def random_deviate(angle, pct):
    lo = angle * (1 - pct)
    hi = angle * (1 + pct)
    return random.uniform(lo, hi)


def deviate(angle, lo, hi):
    return random.uniform(int(lo), int(hi))


# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

# def main(argv):
#
#     global cpi
#     global angle
#     global L
#     global t
#     global sz
#     global poss
#     global cc

L = 25  # length of line
# parameters for absolute angle

hi, lo = 0, 16  # young plant
# hi, lo = 0, 60  # bush
# hi, lo = 0, 360  # chaos
# parameters for relative angle - percantage 0.6 = 60%

_P = .60

# parameters for length
L = 50
_L = .50

# python ./hex_builder_lapse.py -l 50 -f 0 -t 60

argv = sys.argv[1:]

# pprint(argv)

try:
    opts, args = getopt.getopt(argv, "hl:e:d:i:f:t:", ["length=", "deviation=", "increment=", "fromangle=", "toangle="])
except getopt.GetoptError:
    print('test.py -h -l <length> -e <length variation> -d <deviation> -i <increment> -f <from angle> -t <to angle>')
    sys.exit(2)

for opt, arg in opts:
    # print(opt,arg);
    if opt == '-h':
        print('-h -l <length> -d <deviation> -i <increment>')
        sys.exit()
    if opt in ("-l", "--length"):
        L = int(arg)
    if opt in ("-e", "--lengthvariation"):
        _L = float(arg)
    if opt in ("-i", "--increment"):
        _P = arg
    if opt in ("-f", "--fromangle"):
        lo = arg
    if opt in ("-t", "--toangle"):
        hi = arg

# print('Length (L) :',L)
# print('Increment (_P) :',_P)
# print('From (lo) :',lo)
# print('To (hi) :',hi)

count = 5  # coiunt+1 = number of generations
angle = 60  # angle of separation
sz = 14  # size of arrowhead
Lorg = 25  # default length of line
ps = 0  # point size
cpi = 0  # thickness of line
W = [5,4,3,2,1,0]  # W = [39,30,22,14,3]# W = [2,2,2,2,2,2]# W = [1,1,1,1,1,1]

poss = []
cc = 0
pi = 0

screen = Screen()
screen.setup(500,500)

t = Turtle()

t.color(255, 255, 255)
t.pensize(ps)
t.setx(0)
t.sety(0)
# t.right(90)


t.forward(L)
t, color("white")
pos = t.position()  # store pos
x = pos[0]
y = pos[1]
t.speed(9)

poss = []

# clr = [ "red","brown","green","cyan","blue","violet"]
# clr = [252,225,200,175,150,125,0]
clr = [
    "magenta"
    , "Blue Violet"
    , "medium turquoise"
    , "sea green"
    , "goldenrod"
    , "maroon"
    , "deep pink"

]
clr = [
    "#5a3313"
    , "#a86f3b"
    , "#7d8558"
    , "#cecc06"
    , "#cb7d98"
    , "#ca4c25"
    , "#d4db37"

]

# ----------------------------------------------------


# FIRST
# change_color(t)
# t.color("pink")
bifur(t, x, y, 0, "white");
# print("FIRST: ")
# print(cc,len(poss))
# pprint(poss)
pi = pi + 1

die = 0;

for p in range(count):

    t.color(clr[p % len(clr)])
    t.pensize(W[p % len(W)])

    cpi = 0
    for i in range(len(poss)):

        L = random_deviate(L, _L)  # get new length

        # -----------------------------------------------------------------------------------------------------
        # these randomly alter the deviation of each pair by a percentage relative to their natural position
        # -----------------------------------------------------------------------------------------------------
        angle = random_deviate(angle, _P)

        # -----------------------------------------------------------------------------------------------------
        # these chooses thh angle randomly between two absolutes
        # -----------------------------------------------------------------------------------------------------

        angle = deviate(angle, hi, lo)

        # print(angle, L)

        u = i
        if poss[u][3] == p:
            if p <= count:
                bifur(t, poss[u][0], poss[u][1], poss[u][2], clr[p % len(clr)]);
    # print("--------------------------ROUND: ", p, ": ", cpi)
    pi = pi + 1
    cpi = cpi + 2

t.penup()
t.setposition(1000, 1000)
t.color("white")

ts = t.getscreen()
ang = "{:02d}".format(int(angle))
ts.getcanvas().postscript(file=f"eps/hex-{ang}.eps")
cmd = f"epstopdf eps/hex-{ang}.eps"
print(cmd)
os.system(cmd)

cmd = f"convert -rotate -90 -density 300 -trim eps/hex-{ang}.pdf -quality 100 eps/hex-{ang}.png "
print(cmd)
os.system(cmd)

# best to batch this later so th eimages can be mergedintoa movie
# cmd = f"convert -border 100 -bordercolor white  eps/hex-{ang}.png  eps/shex-{ang}.png "
# print(cmd)
# os.system(cmd)
#
# cmd = f"mv -f eps/shex-{ang}.png eps/hex-{ang}.png"
# print(cmd)
# os.system(cmd)


print('FINISHED')

# if __name__ == "__main__":
#    main(sys.argv[1:])
