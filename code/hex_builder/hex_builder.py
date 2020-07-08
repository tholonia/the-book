from turtleplus import *
from pprint import pprint
import numpy as np
import random


def diff(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)




def change_color(t):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    t.color(R, G, B)

def dl(t, lx, ly,h,clr):
    # set the position to a previous point
    global cpi
    global p
    cpi =  cpi + 1

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

    ldat=[lpos[0],lpos[1],angl,pi]

    larrow(clr);
    poss.append(ldat)


    return(ldat)

def dr(t, lx, ly,h,clr):
    global cpi
    global p
    t.setheading(h)
    t.penup()
    t.setposition(lx, ly)
    t.pendown()

    # draw the right line
    t.right(angle)
    t.forward(L)

    cpi =  cpi + 1
    angr = t.heading()
    # t.dot(25)

    #get the position
    rpos = t.position()  # store pos
    rx=rpos[0]
    ry=rpos[1]

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

    t.left(angle * 3.5) # 210)
    t.forward(sz)

    t.left(angle * 2) # 120)
    t.forward(sz/2)

    t.left(angle * 1.5) # 90)
    t.forward(sz*.8)

    t.end_fill()

def rarrow(clr):
    t.fillcolor(clr)
    t.begin_fill()

    t.right(angle * 3.5) # 210
    t.forward(sz)

    t.right(angle * 2) # 120)
    t.forward(sz/2)

    t.right(angle * 1.5) # 90)
    t.forward(sz*.8)

    t.end_fill()

def pause():
    t.getscreen()._root.mainloop()


def bifur(t, lx, ly,h,clr):
    global cc
    lp=dl(t, lx, ly,h,clr)
    rp=dr(t, lx, ly,h,clr)
    # print ("------",cc)
    cc = cc+1
    # print ("++++++",cc)

def random_deviate(angle,pct):
    lo = angle * (1-pct)
    hi = angle * (1+pct)
    return random.uniform(lo,hi)

def deviate(angle,lo,hi):
    return random.uniform(lo,hi)
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

count = 5   # coiunt+1 = number of generations
angle = 60  # angle of separation
sz = 14     # size of arrowhead
L = 25      # length of line
Lorg = 25   # default length of line
ps = 0      # point size
cpi = 0     # thickness of line
W = [ps,ps,ps,ps,ps,ps,ps] # W = [39,30,22,14,3]# W = [2,2,2,2,2,2]# W = [1,1,1,1,1,1]

poss = []
cc = 0
pi=0

t = Turtle()
t.color(255,255,255)
t.pensize(ps)
t.setx(0)
t.sety(0)
#t.right(90)
t.forward(L)
t,color("white")
pos = t.position()  # store pos
x = pos[0]
y = pos[1]
t.speed(9)

poss=[]

# clr = [ "red","brown","green","cyan","blue","violet"]
# clr = [252,225,200,175,150,125,0]
clr = [
    "magenta"
    ,"Blue Violet"
    ,"medium turquoise"
    ,"sea green"
    ,"goldenrod"
    ,"maroon"
    ,"deep pink"

    ]

# ----------------------------------------------------


# FIRST
# change_color(t)
# t.color("pink")
bifur(t, x, y, 0,"white");
print("FIRST: ")
print(cc,len(poss))
pprint(poss)
pi=pi+1


die=0;

for p in range(count):

    t.color(clr[p % len(clr)])
    t.pensize(W[p % len(W)])

    cpi=0
    for i in range(len(poss)):

        # parameters for length
        L = 50
        _L = .50

        L = random_deviate(L,_L) # get new length

        # parameters for relative angle - percantage 0.6 = 60%

        _P = .60


        # -----------------------------------------------------------------------------------------------------
        # these randomly alter the deviation of each pair by a percentage relative to their natural position
        # -----------------------------------------------------------------------------------------------------
        angle = random_deviate(angle,_P)

        # -----------------------------------------------------------------------------------------------------
        # these chooses thh angle randomly between two absolutes
        # -----------------------------------------------------------------------------------------------------

        # parameters for absolute angle

        hi, lo = 0, 16 # young plant
        #hi, lo = 0, 60  # bush
        #hi, lo = 0, 360  # chaos

        angle= deviate(angle,hi,lo)

        print(angle, L)

        u=i
        if poss[u][3] == p:
            if p <= count:
                bifur(t, poss[u][0], poss[u][1], poss[u][2],clr[p % len(clr)]);
    print("--------------------------ROUND: ", p, ": ", cpi)
    pi=pi+1
    cpi = cpi + 2

t.penup()
t.setposition(1000,1000)
t.color("white")
pause()
pause();
