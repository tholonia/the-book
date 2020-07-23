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
numtype="P"
ts = "2020-06-24 17:31:07.0"
hlp = "-h -d <time delta> -t <timestamp> -r -x <width> -y <height> -u <numtype> (P, N, A)"
try:
    opts, args = getopt.getopt(argv, "hrd:t:x:y:u:", ["help=","redrawonly==","delta=","timestamp=","width==","height==","numtype=="])
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
        height = int(arg)
    if opt in ("-y", "--height"):
        width = int(arg)
    if opt in ("-u", "--numtype"):
        numtype = arg


def is_prime(n):
    if n < 2:
        return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False
    return True

def is_not_prime(n):

    if n < 2:
        return True
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return True
    return False

def is_any(n):
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
fs=[tdelta]
newx = 0
newy = 0
size = 1
i = 0
# colors are BGR, not RGB
#1
iclr=[]
iclr.append([0,0,0]) # skip because index 0
iclr.append([0,0,255])
iclr.append([0,128,255])
iclr.append([64,255,255])
iclr.append([0,255,128])
iclr.append([0,255,0])
iclr.append([128,255,0])
iclr.append([255,255,0])
iclr.append([255,128,0])
iclr.append([255,0,0])

for i in range(len(iclr)):
    iclr[i]=[255,255,255]

iclr[1]=[0,0,150]
iclr[2]=[0,80,150]
iclr[3]=[0,150,150]
iclr[4]=[0,150,80]
iclr[5]=[0,150,0]
iclr[6]=[80,150,0]
iclr[7]=[150,150,0]
iclr[8]=[150,80,0]
iclr[9]=[150,0,0]


#iclr[0]=[255,255,255]
# iclr[1]=[255,255,255]
# iclr[2]=[255,255,255]
# iclr[3]=[255,255,255]
# iclr[4]=[255,255,255]
# iclr[5]=[255,255,255]
# iclr[6]=[255,255,255]
# iclr[7]=[255,255,255]
# iclr[8]=[255,255,255]
#iclr[9]=[255,255,255]

#36
#2589



#iclr[3]=[0,255,255]
#iclr[4]=[0,255,128]
#iclr[5]=[0,255,0]
#iclr[6]=[128,255,0]
#iclr[7]=[255,255,0]
#iclr[8]=[255,128,0]
#iclr[9]=[255,0,0]


for fp in fs:
    cmd=f"./moon_dat.py -d {fp} -t {ts}"
    print(f"EXECUTE: {cmd}",end="")
    if redrawonly:
        print("...skipping",end="")
    else:
        os.system(cmd)
    print("\n")
    datfn = f"dat/{numtype}data-{fp}sec_{cleanstr(ts)}.dat"
    print(f"DATFILE: {datfn}")
    print("... reading  file")
    dat = open(datfn,"r")
    fmi = f"eps/{numtype}moon_im_{fp}_{cleanstr(ts)}_{height}x{width}.png"
    print(f"IMGFILE: {fmi}")
    img = np.zeros((width + 2, height + 2, 3), np.uint8)
    img = fillrec(img, width, height, [0, 0, 0])
    for line in dat:
        # print(f"{i}        ",end="\r")
        # i+=1
        stripped_line = line.strip()
        line_list = stripped_line.split()
        data = (line_list)
        tms = data[4]
        # type=data[7]


        # if type == "^P":
        if is_any(int(tms)):
            # clr = ipru(int(tms))
            img[newx, newy] = iclr[int(tms)]
            newx = newx + size
            if (newy == height) and (newx == width):
                cv2.imwrite(fmi, img)
                print(f"WIDTH: {newy}")
                newx = 0
                newy = 0
                break
            if (newx == width):
                newy = newy + size
                newx = 0
    print(f"end of data, {newy} of {height}")
    cv2.imwrite(fmi, img)
