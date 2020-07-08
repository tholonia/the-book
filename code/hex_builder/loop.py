#!/bin/python
import os

# os.system("rm -rf eps/*")

# fixed length
s = 1/100/60
b = .60

for i in range(0,61):
    cmd = f"python ./hex_builder_lapse.py -l 25 -e 0 -f {i} -t {i}"
    print(cmd)
    os.system(cmd)
#
