#!/usr/bin/python3.7

import numpy as np
from pprint import *
import os, sys, getopt
from math import sqrt
import cv2
from itertools import count, islice

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hi:", ["help=","inputfile="])
except getopt.GetoptError:
    print('-h -i <inputfile>')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('-h -i <inputfile> ')
        sys.exit()
    if opt in ("-i", "--inputfile"):
        inputfile = arg


datfn = f"{inputfile}"
data = open(datfn,"r")

for d in data:
    print("{0:b}".format(int(d)),end="")