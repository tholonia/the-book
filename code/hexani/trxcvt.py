#!/bin/python
import time
import base32_crockford as bc
import base64
import random
import shutil
import sys, os
sys.path.insert(1, '/home/jw/books/tholonia/code/hexani/')
import lapselib as ll

trxid = "98e9442ffc7bc3561adca48f026c4d7fcf3d143f46ae200ebd72952024aa26b9"

split_strings = []
n = 6
for index in range(0, len(trxid), 4):
    split_strings.append(trxid[index: index + n])

# print(split_strings)

for i in range(0, 10):
    print(split_strings[i])

lastnum = i = int(split_strings[10], 16)
print(f"dec: {lastnum}")

print(str(lastnum).split())


def get_name():
    # ts = int(time.time())
    # # tsc = ts.replace(".","")
    # name = bc.encode(int(ts))
    # return (name)

    x = random.randint(0, 16777215)
    rs = hex(x)
    return(f"a{rs[2:]}")

def convert_to_base(decimal_number, base):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return ''.join(new_digits)

def makecfg(updates):
    defvalary = {
        'repo': "\"/home/jw/books/tholonia/code/hexani/\""
        , 'root': "\"/home/jw/books/tholonia/code/hexani/tmp\""
        , 'name': "\"NAME\""
        , 'series': "\"SERIES\""
        , 'PSN': "0"
        , 'delay': 60
        , 'status': "\"generated\""
        , 'compression': "\"\""
        , 'background': "[false,true]"
        , 'framenum': "\"060\""
        , 'desklock': 1
        , 'update': "true"
        , 'zoomframenum': "\"select\""
        , 'NODELETE': "false"
        , 'DESCRIPTOR_ONLY': "false"
        , 'RUNGIFONLY': "false"
    }

    argvalary = {
        'ncount': 6
        , 'SES': "[0, 361, 1]"
        , 'angle': 60
        , 'length': "[ [\"40\",\"0\",\"NULL\"],[\"40\",\"0\",\"NULL\"] ]"
        , 'hardangle': "[0,0]"
        , 'lenDev': "[0.0,0.0]"
        , 'angDev': "[0.0,0.0]"
        , 'floDev': "true"
        , 'syncpoints': 0
        , 'usecolor': "[\"blues\",\"yellows\"]"
        , 'outline': "[\"0\",\"0\"]"
        , 'stempalette': 0
        , 'flowerpalette': 1
        , 'style': f"[9,8,7,6,5,4,3]"
        , 'flowersize': 24
        , 'growflower': 0
        , 'cores': 1
        , 'randclr': "false"
        , 'show_right': "true"
        , 'show_left': "true"
        , 'dot': "[0,0]"
    }

    for key in defvalary:
        try:
            defvalary[key] = updates[key]
        except:
            pass
    for key in argvalary:
        try:
            argvalary[key] = updates[key]
        except:
            pass

    cfg = ""
    cfg = cfg + "[def]\n"
    for key in defvalary:
        cfg = cfg + f"{key} = {defvalary[key]}\n"
    cfg = cfg + "# -------------------------------\n"
    cfg = cfg + "[arg]\n"
    for key in argvalary:
        cfg = cfg + f"{key} = {argvalary[key]}\n"

    return (cfg)


name = get_name()


def get_hardangle():
    a1 = random.randint(-60, 60)
    a2 = random.randint(-60, 60)
    str = f"[{a1},{a2}]"
    return (str)


def get_length():
    len1 = random.randint(20, 40)
    len2 = random.randint(20, 40)
    typeary = ["stop_at_60", "osc_aLL_big", "osc_aLL_small", "big_osc", "osc_btn_20_and_80", "NULL"]
    inc1 = 0 #random.randint(0, 3)
    inc2 = 0 #random.randint(0, 3)
    type1 = typeary[random.randint(0, len(typeary) - 1)]
    type2 = typeary[random.randint(0, len(typeary) - 1)]
    lenstr = f"[ [\"{len1}\",\"{inc1}\",\"{type1}\"],[\"{len2}\",\"{inc2}\",\"{type2}\"] ]"
    return (lenstr)


def get_lenDev():
    l1 = random.randint(0, 10)
    a1 = 1 if l1 == 1 else 0
    str = f"[0.{l1},{a1}.0]"
    return (str)


def get_angDev():
    l1 = random.randint(0, 10)
    a1 = 1 if l1 == 1 else 0
    str = f"[0.{l1},{a1}.0]"
    return (str)


def get_floDev():
    l1 = random.randint(0, 1)
    str = "true" if l1 == 1 else "false"
    return (str)


def get_syncpoints():
    return random.choice([0, 30, 45, 60, 90, 180])


def get_usecolor():
    colors = [
        "denimbamboo",
        "yellows",
        "blues",
        "greens",
        "browns",
        "darkgrays",
        "lightgrays",
        "default",
        "medical_gray",
        "medical_gray_3",
        "aura_red",
        "prog_A",
        "prog_B",
        "prog_C",
        "prog_C_fast",
        "prog_C_medium",
        "SinSinSin",
        "SinSinSinFast",
        "SinCosSin",
        "SinCosDelta",
        "SinCosDeltaFast",
        "pi",
        "progressive3",
        "progressive4",
    ]
    c1 = colors[random.randint(0, len(colors) - 1)]
    c2 = colors[random.randint(0, len(colors) - 1)]
    str = f"[\"{c1}\",\"{c2}\"]"
    return (str)


def get_outline():
    "[\"0\",\"0\"]"

    contrast = random.randint(0, 360)
    width = random.randint(0, 6)

    str = f"[\"{contrast}\",\"{width}\"]"
    return (str)


def get_growflower():
    return random.randint(0, 1)


def get_stempalette():
    return random.randint(0, 1)


def get_flowerpalette():
    return random.randint(0, 1)


def get_cores():
    return random.randint(1, 2)


def get_style():
    l0 = random.randint(1, 12)
    l1 = random.randint(1, 12)
    l2 = random.randint(1, 12)
    l3 = random.randint(1, 12)
    l4 = random.randint(1, 12)
    l5 = random.randint(1, 12)
    str = f"[{l0},{l1},{l2},{l3},{l4},{l5}]"
    return (str)


def get_flowersize():
    return random.randint(0, 40)


def get_show_right():
    l1 = random.randint(0, 1)
    str = "true" if l1 == 1 else "false"
    return (str)


def get_show_left():
    l1 = random.randint(0, 1)
    str = "true" if l1 == 1 else "false"
    return (str)


def get_randomcolors(n):
    import matplotlib.pyplot as plt
    import random

    number_of_colors = n

    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    return (color)


def get_dot():
    color = get_randomcolors(1)
    size = random.randint(10, 30)
    on = random.randint(0, 1)

    str = "[0,0]"
    if on == 0:
        return (str)
    else:
        str = f"[\"{color[0]}\",\"{size}\"]"
        return (str)

# ll.runthis(f"/home/jw/books/tholonia/code/hexani/Xnextpsn","trxcvt",True,False)
# psn = 0
#with open('/home/jw/books/tholonia/code/hexani/Xnextpsn') as f:
#    psn = int(f.readline())

script = ""
i=1
while (i < 6):
    name = get_name()

    updates = {
        'root': f"\"/home/jw/books/tholonia/code/hexani/{name}_x\""
        , 'name': f"\"{name}\""
        , 'series': "\"x\""
        , 'length': get_length()
        , 'hardangle': get_hardangle()  # "[0,0]"
        , 'lenDev': get_lenDev()  # "[0.0,0.0]"
        , 'angDev': get_angDev()  # "[0.0,0.0]"
        , 'floDev': get_floDev()  # "true"
        , 'syncpoints': get_syncpoints()
        , 'usecolor': get_usecolor()  # "[\"blues\",\"yellows\"]"
        , 'outline': get_outline()  # "[\"0\",\"0\"]"
        , 'stempalette': get_stempalette()  # 0
        , 'flowerpalette': get_flowerpalette()  # 1
        , 'style': get_style()  # "[9,8,7,6,5,4,3]"
        , 'flowersize': get_flowersize()  # 24
        , 'growflower': get_growflower()
        , 'cores': get_cores()
        , 'randclr': "false"
        , 'show_right': "true"
        , 'show_left': "true"
        # , 'show_right': get_show_right()
        # , 'show_left': get_show_left()
        , 'dot': f"{get_dot()}"
    }

    dir = f"/home/jw/books/tholonia/code/hexani/{name}_x"

    ll.runthis(f"/home/jw/books/tholonia/code/hexani/Xmake {name} x> /dev/null 2>&1 ", "trxcvt", True, False)
    file = f"/home/jw/books/tholonia/code/hexani/{name}_x/build.toml"
    print(f"CREATING CONFIG FILE: {file}")
    toml = open(file, 'w')
    data = makecfg(updates)
    toml.write(data)
    toml.close()


    script = script + f"\n#---------------------------------\n"
    script = script + f"cd {name}_x\n"
    script = script + "./RUN\n"
    script = script + "cd -\n"
    script = script + f"#---------------------------------\n"

    i = i + 1


print(script)