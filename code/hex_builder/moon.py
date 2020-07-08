# coding: utf-8
"""
====================================
Planet Positions in the Solar System
====================================

The purpose of this demo is to demonstrate the ability of sunpy
to get the position of planetary bodies im the solar system.
"""

##############################################################################
# First the imports
# from astropy.coordinates import SkyCoord
# from sunpy.coordinates import get_body_heliographic_stonyhurst
from astropy.time import Time
# import matplotlib.pyplot as plt
import numpy as np
from pprint import *
import ephem
import datetime
import time
import sys
import os
from math import sqrt
from itertools import count, islice
from colored import fg, bg, attr
from turtleplus import *
from pprint import pprint

bg_hyin = bg('blue_3b') # dark red
bg_yin = bg('red_3b') # red

bg_yang = bg('green_3b') # yellow
bg_hyang = bg('light_yellow') # dark yellow

bgdefault = bg(0)
cc = 0




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
        # print(f"[{jn}]")
        s = s + jn
    return s

def overprint(text,repl, t=5):
    print(text, end="\r")
    print('\r{0:{1}<{2}}'.format(repl, char, len(text)))

def reduce(ni):
    n = f'{ni}'
    m = n.replace('.', '')
    m = list(m)
    mas = ssum(m)
    # print("---",mas)`
    if (mas>9):
        mas = reduce(mas)
    return int(f'{mas}')

def hyin(out):
    global bg_yin
    global bg_yang
    global bg_hyin
    global bg_hyang
    global bgdefault
    # print('{0} {1} {2} {3}'.format(bg_hyin, bgdefault, bg_hyin, bgdefault),end="", file=out, flush=True)
    print('{0} {1}'.format(bg_hyin, bgdefault, ), end="", file=out, flush=True)


def yang(out):
    global bg_yin
    global bg_yang
    global bg_hyin
    global bg_hyang
    global bgdefault
    # print('{0}   {1}'.format(bg_yang, bgdefault),end="", file=out, flush=True)
    print('{0} {1}'.format(bg_yang, bgdefault), end="", file=out, flush=True)


def yin(out):
    global bg_yin
    global bg_yang
    global bg_hyin
    global bg_hyang
    global bgdefault
    # print('{0} {1} {2} {3}'.format(bg_yin, bgdefault, bg_yin, bgdefault), end="", file=out, flush=True)
    print('{0} {1}'.format(bg_yin, bgdefault),end="", file=out, flush=True)
def hyang(out):
    global bg_yin
    global bg_yang
    global bg_hyin
    global bg_hyang
    global bgdefault
    # print('{0}   {1}'.format(bg_hyang, bgdefault),end="", file=out, flush=True)
    print('{0} {1}'.format(bg_hyang, bgdefault),end="", file=out, flush=True)

def pru(c):
    # # print('%s Hello World !!! %s') % (red, default)
    # colored.bg(39)
    # print('{0} {1} {2} {3}'.format(red, default, red, default))
    #
    # return
    if (c == 2): #hyper yin
        hyin(sys.stdout)
        yang(sys.stderr)

    if (c == 3): #yang
        yang(sys.stdout)
        yang(sys.stderr)

    if (c == 5): #yin
        yin(sys.stdout)
        yin(sys.stderr)

    if (c == 7): #hyper yang
        hyang(sys.stdout)
        yin(sys.stderr)
def tpru(c):
    global newx
    global newy
    if (c == 2): #hyper yin
        t.color('blue')
        t.penup()
        t.setposition(newx,newy)
        t.pendown
        t.dot(size)

    if (c == 3): #yang
        t.color('red')
        t.penup()
        t.setposition(newx,newy)
        t.pendown
        t.dot(size)

    if (c == 5): #yin
        t.color('green')
        t.penup()
        t.setposition(newx,newy)
        t.pendown
        t.dot(size)

    if (c == 7): #hyper yang
        t.color('yellow')
        t.penup()
        t.setposition(newx,newy)
        t.pendown
        t.dot(size)


##############################################################################
# Lets grab the positions of each of the planets in stonyhurt coordinates.
# obstime = Time(datetime.datetime.now())
# planet_list = ['earth','mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus']
# planet_list = ['earth','earth']
# planet_coord = [get_body_heliographic_stonyhurst(this_planet, time=obstime) for this_planet in planet_list]
# pprint(planet_coord)




# for i in range(100):
#     print(i,end="\r")
# exit()

# overprint("The bomb will explode in one sec...")
# overprint("BOOM")
# exit()


t = Turtle()
t.speed(0)
t.color(255,255,255)
size=2

width=720
height=720
newx = int(width/2-width)
newy = int(height/2-height)+7
screen = Screen()
screen.setup(width,height)
screen.bgcolor('black')
savedata = open('set1-new.dat', 'w')
prevut = ""
ut = ""

idx=0

ForL = "F"


while True:
    if (ForL == 'L'):
        obstime = Time(datetime.datetime.now())
        home = ephem.Observer()
        # home.lat, home.lon = -38.42, -63.58 #la pampa
        home.lat, home.lon = -34.61262, -58.41048 #alsona
        home.date = datetime.datetime.utcnow()

        moon = ephem.Moon()
        moon.compute(home)
        sun = ephem.Sun()
        sun.compute(home)

        maz = f"{repr(moon.az)}"
        saz = f"{repr(sun.az)}"

        mas = reduce(repr(moon.az))
        sas = reduce(repr(sun.az))
        ut = f"{repr(moon.az)}.{repr(sun.az)}"
        tms = reduce(mas+sas)

        # str = f"\r Moon: {mas}   Sun: {sas}  [{tms}]"
        str = f"{tms}"

        # print(str, end="",flush=True)
        if (is_prime(tms)):
            if (prevut != ut):
                print(f"{ut} {str} {datetime.datetime.now()}", file=savedata, flush=True)
                print(f"{maz}  {mas}  {saz}  {sas}  {tms}  {datetime.datetime.now()} ", file=savedata,flush=True)
                tpru(tms)
                cc = cc+1
                if (cc == 216):
                    cc = 0;
                    # print("\n",flush=True, file=sys.stdout,end="")
                    # print("\n", flush=True, file=sys.stderr,end="")

                # time.sleep(.01)
                newx = newx+size
                if (newx > width/2):
                    newy = newy+size
                    newx= width/2-width

                if (newy > height/2):
                    ts = t.getscreen()
                    ts.getcanvas().postscript(file=f"eps/moon-{size}.eps")

                    cmd = f"epstopdf eps/moon-{size}.eps"
                    print(cmd)
                    os.system(cmd)

                    cmd = f"convert -rotate -90 -density 300 -trim eps/moon-{size}.pdf -quality 100 eps/moon-{size}.png "
                    print(cmd)
                    os.system(cmd)

                    exit
                prevut=ut
    if (ForL == "F"):
#        dat = open("set1.dat", "r")
        dat = open("savedata4-0.5sec.dat", "r")

        data = []
        for line in dat:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            data.append(line_list)

        for d in data:

            mas = reduce(d[0])
            sas = reduce(d[1])
            # ut = f"{repr(moon.az)}.{repr(sun.az)}"
            tms = reduce(mas + sas)

            # str = f"\r Moon: {mas}   Sun: {sas}  [{tms}]"
            str = f"{tms}"

            # print(str, end="",flush=True)
            if (is_prime(tms)):
                # print(f"{ut     },{str},{datetime.datetime.now()}", file=savedata, flush=True)
                tpru(tms)
                cc = cc + 1
                if (cc == 216):
                    cc = 0;
                    # print("\n",flush=True, file=sys.stdout,end="")
                    # print("\n", flush=True, file=sys.stderr,end="")

                # time.sleep(.01)
                newx = newx + size
                if (newx > width / 2):
                    newy = newy + size
                    newx = width / 2 - width

                if (newy > height / 2):
                    ts = t.getscreen()
                    ts.getcanvas().postscript(file=f"eps/moon-{size}.eps")

                    cmd = f"epstopdf eps/moon-{size}.eps"
                    print(cmd)
                    os.system(cmd)

                    cmd = f"convert -rotate -90 -density 300 -trim eps/moon-{size}.pdf -quality 100 eps/moon-{size}.png "
                    print(cmd)
                    os.system(cmd)

                    exit()

##############################################################################
# Now lets make a plot.
# fig = plt.figure()
# ax1 = plt.subplot(1, 1, 1, projection='polar')
# tdeg = 0;
# for this_planet, this_coord in zip(planet_list, planet_coord):
#     tdeg = tdeg + this_coord.lon
#     plt.polar(np.deg2rad(this_coord.lon), this_coord.radius, 'o', label=this_planet)
# plt.legend()
# plt.show()
