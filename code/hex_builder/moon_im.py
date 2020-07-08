#!/usr/bin/python3.7
# coding: utf-8
"""
====================================
Planet Positions in the Solar System
====================================

The purpose of this demo is to demonstrate the ability of sunpy
to get the position of planetary bodies im the solar system.
"""

##############################################################################
import numpy as np
from pprint import *
import os, sys, getopt
from math import sqrt
import cv2
from itertools import count, islice


argv = sys.argv[1:]

# pprint(argv)
redrawonly = False
tdelta=1.618
height=720
width=216
ts = "2020-06-24 17:31:07.0"
hlp = "-h -d <time delta> -t <timestamp> -r -x <width> -y <height>"
try:
    opts, args = getopt.getopt(argv, "hrd:t:x:y:", ["help=","redrawonly==","delta=","timestamp=","width==","height=="])
except getopt.GetoptError:
    print("Oops...")
    print(hlp)
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print(hlp)
        sys.exit()
    if opt in ("-t", "--timestamp"):
        ts = arg
    if opt in ("-d", "--delta"):
        tdelta = arg
    if opt in ("-r", "--redrawonly"):
        redrawonly = True
    if opt in ("-x", "--width"):
        width = int(arg)
    if opt in ("-y", "--height"):
        height = int(arg)


def is_prime(n):
    if n < 2:
        return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False
    return True

def ssum(l):
    s = 0
    for i in l:
        jn = int(i)
        s = s + jn
    return s

def reduce(ni):
    n = f'{ni}'
    m = n.replace('.', '')
    m = list(m)
    mas = ssum(m)
    # print("---",mas)`
    if (mas>9):
        mas = reduce(mas)
    return int(f'{mas}')

def ipru(c):
    if (c == 2): #hyper yin
        return(255,0,0) # t.color('blue')
    if (c == 3): #yang
        return(0,0,255) # t.color('red')
    if (c == 5): #yin
        return(0,255,0) # t.color('green')
    if (c == 7): #hyper yang
        return(0,255,255) # t.color('yellow')

def cleanstr(s):
    remove_characters = [":", " ", "."]

    for character in remove_characters:
        s = s.replace(character, "_")

    return s

def argfix(s):
        return s.replace("_", " ")

def fillrec(img,width,height,clr):
    for x in range(width):
        for y in range(height):
            img[x, y] = clr
    return img
##############################################################################
"""
data[0]     {maz}   moon.az radians
data[1]     {mas}   moon.az reduced
data[2]     {saz}   sun.az radians
data[3]     {sas}   sun.az reduced
data[4]     {tms}   total reduced - reduced
data[5]             date 
data[6]             time
data[7]     {flag}  ^N or ^P
"""
fs=[tdelta]

fmi=""
for fp in fs:

    cmd=f"./moon_dat.py -d {fp} -t {ts}"
    print(f"EXECUTE: {cmd}",end="")
    if redrawonly:
        print("...skipping",end="")
    else:
        os.system(cmd)
    print("\n")

    datfn = f"dat/data-{fp}sec_{cleanstr(ts)}.dat"
    print(f"DATFILE: {datfn}")
    dat = open(datfn,"r")
    fmi = f"eps/moon_im_{fp}_{cleanstr(ts)}.png"
    print(f"IMGFILE: {fmi}")

    data = []
    for line in dat:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        data.append(line_list)

    # height=720
    newx=0
    newy=0
    size=1
    img = np.zeros((width,height,3),np.uint8)

    img=fillrec(img,width,height,[0,0,0])
    for d in data:
        # mas = reduce(d[1])
        # sas = reduce(d[3])
        mas = d[1]
        sas = d[3]
        # ut = f"{repr(moon.az)}.{repr(sun.az)}"
        tms = d[4]

        # print(d[7], end="",flush=True)
        # if (d[7] == "^P"):
        # if is_prime(int(d[4])) and is_prime(int(d[1])) and is_prime(int(d[3])):
        if is_prime(int(d[4])):
            # print(f"{ut     },{str},{datetime.datetime.now()}", file=savedata, flush=True)
            clr = ipru(int(tms))
            # print(clr)

            # print(newx)
            img[newx,newy] = clr

            newx = newx + size
            # ct = ct + 1
            # print(f"{clr}/{newx}/{width}")
            if (newx >= width ):
                newy = newy + size
                newx = 0
                # print(".",end="")

            if (newy >= height):
                # print(f"writing image {fmi}")
                cv2.imwrite(fmi, img)
                print(f"WIDTH: {newy}")
                newx = 0
                newy = 0
                continue
    print(f"end of data, {newy} of {height}")

    cv2.imwrite(fmi, img)
