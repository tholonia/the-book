#!/bin/python
from pprint import pprint
import numpy as np
import random
from tkinterx import *
import os, sys, getopt, random
import subprocess

cary = []
for a in range(0,16777215,4660):
    # convert to decimal
    dc =  hex(a)
    dc = dc[2:]
    dc = dc.zfill(6)
    cary.append(f"#{dc}")

for a in range(0,16777215,4660):
    # convert to decimal
    dc =  hex(a)
    dc = dc[2:]
    dc = dc.zfill(6)
    print(f"'#{dc}',",end="")
