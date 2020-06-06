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
    t.left(60)  # turn left
    t.forward(L)  # drawl line

    angl = t.heading()
    # t.dot(20)

    # get the end poijt position
    lpos = t.position()  # store pos
    t.right(60)  # face front

    ldat=[lpos[0],lpos[1],angl,pi]

    # larrow(clr);
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
    t.right(60)
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

    t.left(60)  # face front

    rdat = [rpos[0], rpos[1], angr, pi]

    poss.append(rdat)
    # rarrow(clr);
    return (rdat)


def larrow(clr):
    t.fillcolor(clr)
    t.begin_fill()

    t.left(210)
    t.forward(sz)

    t.left(120)
    t.forward(sz/2)

    t.left(90)
    t.forward(sz*.8)

    t.end_fill()

def rarrow(clr):
    t.fillcolor(clr)
    t.begin_fill()

    # t.left(90)
    # t.forward(sz)
    #
    # t.left(120)
    # t.forward(sz/2)
    #
    # t.left(90)
    # t.forward(sz*.8)
    #
    t.right(210)
    t.forward(sz)

    t.right(120)
    t.forward(sz/2)

    t.right(90)
    t.forward(sz*.8)

    t.end_fill()

    #
    # t.right(210)
    # t.forward(sz)
    # t.back(sz)
    # t.left(210)
    #
    # t.left(90)
    # t.forward(sz)
    #
    # t.left(120)
    # t.forward(sz)
    # t.back(sz)
    # t.right(210) #add the left that was skipped







def pause():
    t.getscreen()._root.mainloop()


def bifur(t, lx, ly,h,clr):
    global cc
    lp=dl(t, lx, ly,h,clr)
    rp=dr(t, lx, ly,h,clr)
    # print ("------",cc)
    cc = cc+1
    # print ("++++++",cc)


# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
sz = 27
L = 50
ps = 5

count = 5

sz = 14
L = 50
ps = 8

cpi = 0;
# W = [39,30,22,14,3]
W = [ps,ps,ps,ps,ps,ps,ps]
# W = [2,2,2,2,2,2]
# W = [1,1,1,1,1,1]

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

vposs={
    '0': [],
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],

}
poss=[]
# clr = [ "red","brown","green","cyan","blue","violet"]
clr = [
    "magenta"
    ,"Blue Violet"
    ,"medium turquoise"
    ,"sea green"
    ,"goldenrod"
    ,"maroon"
    ,"deep pink"

    ]
clr = [
    "black"
    ,"black"
    ,"black"
    ,"black"
    ,"black"
    ,"black"

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

# clr = [252,225,200,175,150,125,0]
die=0;

for p in range(count):

    # change_color(t)
    t.color(clr[p % len(clr)])
    t.pensize(W[p % len(W)])
####3
    # if p == 5:
    #     die=1;
    #     t.color("black")
    # else:
    #     t.color("lightgray")
####
    cpi=0
    for i in range(len(poss)):
        u=i
        if poss[u][3] == p:
            if p <= count:
                bifur(t, poss[u][0], poss[u][1], poss[u][2],clr[p % len(clr)]);
                # print("--------------------------ROUND: ", p, ": ", cpi)
                # print("--------------------------MIN/MAX: ", min(poss[u]), ": ", max(poss[u]))
                dlt = abs(poss[u][0]-poss[u][1])
                # print("DELTA: ",dlt, "   ",poss[u][3])
                # pprint(poss[u])
                su = str(poss[u][3])
                vposs[su].append(dlt)
    pi=pi+1
    cpi = cpi + 2
    print(p)





for j in range(count-1):
    va = vposs[str(j)]
    pmin = min(va)
    pmax = max(va)
    print(j,",",pmin,",",pmax)
t.penup()
t.setposition(1000,1000)
t.color("white")
pause()

