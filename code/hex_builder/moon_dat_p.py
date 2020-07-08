#!/usr/bin/python

# coding: utf-8
from astropy.time import Time
from datetime import datetime
# import matplotlib.pyplot as plt
import numpy as np
from pprint import *
import ephem
import datetime
import time
import os, sys, getopt
from math import sqrt
from itertools import count, islice
from colored import fg, bg, attr

argv = sys.argv[1:]

# pprint(argv)

tdelta=".005"
ts = "2020-06-24 17:31:07.0"
try:
    opts, args = getopt.getopt(argv, "hd:t:", ["help=","delta=","timestamp="])
except getopt.GetoptError:
    print('-h -d <time delta> -t <timestamp>')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('-h -d <timedelta> ')
        sys.exit()
    if opt in ("-d", "--delta"):
        tdelta = arg
    if opt in ("-t", "--timestamp"):
        ts = arg

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
        try:
            jn = int(i)
        except:
            continue
        s = s + jn
    return s

def totimestamp(dt):
    epoch = datetime.date(1970, 1, 1)
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

def cleanstr(s):
    remove_characters = [":", " ", "."]

    for character in remove_characters:
        s = s.replace(character, "_")

    return s

def argfix(s):
    return s.replace("_", " ")

def reduce(ni):
    n = f'{ni}'
    m = n.replace('.', '')
    m = n.replace('e', '')
    m = n.replace('-', '')
    m = list(m)
    mas = ssum(m)
    # print("---",mas)`
    if (mas>9):
        mas = reduce(mas)
    return int(f'{mas}')

def show(c,v):
    if c=='BL':
        C = bg('blue_3b')
    if c=='YE':
        C = bg('yellow_3b')
    if c=='RE':
        C = bg('red_3b')
    if c=='GR':
        C = bg('green_3b')
    DEFAULT = bg('black')
    print('{0}{1}{2}'.format(C,v,DEFAULT), end="", flush=True, file=sys.stderr)

prevut = ""
filename=f'dat/rdata-{tdelta}sec_{cleanstr(argfix(ts))}.dat'
savedata = open(filename, 'w')

obstime = Time(argfix(ts))

ct = 0

primes = 1
nonprimes = 1
dups = 0
valid = 0

decdata = open("dat/pi.dat","r")

for tmsbig in decdata:
    tms = reduce(tmsbig)
    str = f"{tms}"

    flag = "N"
    if (is_prime(tms)):
        flag="P"
        primes +=1
        show('BL',tms)

        valid +=1
        # print(f"{ut     },{str},{datetime.datetime.now()}", file=savedata, flush=True)
        print(f"0  0  0  0  {tms} 0 ^{flag}", file=savedata, flush=True)
    else:
        show('YE', tms)
        nonprimes +=1
    try:
        rs = "P: %8d NP: %8d %8.2f %40s C: %8d D: %8d V: %6d/%d" % (primes,nonprimes,primes/nonprimes, filename, ct, dups, valid, int(valid/216) )
        print(rs, flush=True, end="\n")
    except:
        print("not data...")

    ct = ct +1
    # print(f"{filename}  {ct}             ",end="\r",flush=True)

    if valid >= 216*720:
        print(f"PRIMES: {primes} {(primes/ct)*100}%     NON-PRIMES: {nonprimes}  {(nonprimes/ct)*100}%              ")
        exit()
