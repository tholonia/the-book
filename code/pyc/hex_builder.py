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

def dl(t, lx, ly,h):
    # set the position to a previous point
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

    poss.append(ldat)
    return(ldat)

def dr(t, lx, ly,h):
    t.setheading(h)
    # set the position to a previous point
    t.penup()
    t.setposition(lx, ly)
    t.pendown()

    # draw the right line
    t.right(60)
    t.forward(L)
    angr = t.heading()
    # t.dot(25)

    #get the position
    rpos = t.position()  # store pos
    rx=rpos[0]
    ry=rpos[1]

    # get the end poijt position
    rpos = t.position()  # store pos
    t.left(60)  # face front

    rdat=[rpos[0],rpos[1],angr,pi]

    poss.append(rdat)
    return(rdat)

def pause():
    t.getscreen()._root.mainloop()


def bifur(t, lx, ly,h):
    global cc
    lp=dl(t, lx, ly,h)
    rp=dr(t, lx, ly,h)
    # print ("------",cc)
    cc = cc+1
    # print ("++++++",cc)


# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
L = 50
W = [39,30,22,14,8,4]


poss = []
cc = 0
pi=0
t = Turtle()
t.color(255,255,255)

t.pensize(8)
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
# ----------------------------------------------------


# FIRST
# change_color(t)
# t.color("pink")
bifur(t, x, y, 0);
print("FIRST: ")
print(cc,len(poss))
pprint(poss)
pi=pi+1

clr = [ "red","orange","pink","lightgreen","darkblue","violet"]

# clr = [252,225,200,175,150,125,0]
die=0;
for p in range(5):
    # SECOND
    # change_color(t)
    t.color(clr[p])
    t.pensize(W[p])
####3
    # if p == 5:
    #     die=1;
    #     t.color("black")
    # else:
    #     t.color("lightgray")
####
    for i in range(len(poss)):
        u=i
        if poss[u][3] == p:
            bifur(t, poss[u][0], poss[u][1], poss[u][2]);
    pi=pi+1
    print("SECOND: ")
    print(cc,len(poss),i)
    pprint(poss)
###
    # if die:
    #     t.penup()
    #     t.setposition(1000,1000)
    #     t.color("white")
    #     pause()
###
t.penup()
t.setposition(1000,1000)
t.color("white")
pause()
pause();
