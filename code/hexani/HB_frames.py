#!/usr/bin/python

import os,sys,getopt, time, datetime, subprocess

def makeArgs(myargs):
    longargs = []
    for k in myargs.keys():
        longargs.append(k)

    shortargs = ""
    for k in myargs.values():
        shortargs = shortargs +  k

    sargs = ""
    shortargsAry = []
    for a in  myargs.values():
        a = a.replace(":","")
        a = f"-{a}"
        shortargsAry.append(a)
        sargs = sargs +  a

    largs = []
    for a in  myargs.keys():
        a = a.replace("=","")
        a = f"--{a}"
        largs.append(a)

    comp = {}
    for i in range(0,len(largs)):
        # print(largs[i])
        # print(shortargsAry[i])
        comp[largs[i]] = shortargsAry[i]
    # print(comp)
    # print(sargs)
    # print(largs)
    #
    return longargs,shortargs, comp

argv = sys.argv[1:]

angDev      = "1:1"
lenDev      = "0:0"
usecolor    = "medical_gray"
use_alt_color = usecolor
ncount      = 6
name        = "MISSING"
SES         =[0,361,1]
length      = 60
angle       = 27
style       = 0
flowersize  = 15
locked      = 1
outline     = "no"
growflower  = 0
series      ="MISSING"
syncpoints  = 0
cores       = 1
randclr     = 0

myargs = {
         "angDev="	        :"-a",
         "lenDev="	        :"-l",
         "usecolor="	    :"-c",
         "use_alt_color="	:"-z",
         "ncount="	        :"-n",
         "name="		    :"-N",
         "SES="		        :"-t",
         "length="	        :"-L",
         "angle="	        :"-A",
         "style="	        :"-S",
         "flowersize="	    :"-F",
         "desklock="	    :"-D",
         "outline="	        :"-o",
         "growflower="	    :"-g",
         "series="	        :"-s",
         "syncpoints="	    :"-w",
         "cores="	        :"-C",
         "randclr="	        :"-r",
}

longargs, shortargs, comp = makeArgs(myargs)

try:
    opts, args = getopt.getopt(argv, shortargs, longargs)
except getopt.GetoptError as err:
    print("--------------------------------------------------")
    print(f"HB_frames.py: {err}")
    print("--------------------------------------------------")
    sys.exit(2)
for opt, arg in opts:
    if opt in (comp['--angDev'], "--angDev"):
        angDev = arg
    if opt in (comp['--lenDev'], "--lenDev"):
        lenDev = arg
    if opt in (comp['--usecolor'], "--usecolor"):
        usecolor = arg
    if opt in (comp['--use_alt_color'], "--use_alt_color"):
        use_alt_color = arg
    if opt in (comp['--ncount'], "--ncount"):
        ncount = int(arg)
    if opt in (comp['--name'], "--name"):
        name = arg
    if opt in (comp['--SES'], "--SES"):
        _SES = arg.split(',')
        SES[0] = int(_SES[0])
        SES[1] = int(_SES[1])
        SES[2] = int(_SES[2])
    if opt in (comp['--length'], "--length"):
        length = arg
    if opt in (comp['--angle'], "--angle"):
        angle = arg
    if opt in (comp['--style'], "--style"):
        style = arg
    if opt in (comp['--flowersize'], "--flowersize"):
        flowersize = arg
    if opt in (comp['--desklock'], "--desklock"):
        locked = int(arg)
    if opt in (comp['--outline'], "--outline"):
        outline = arg
    if opt in (comp['--growflower'], "--growflower"):
        growflower = int(arg)
    if opt in (comp['--series'], "--series"):
        series = arg
    if opt in (comp['--syncpoints'], "--syncpoints"):
        syncpoints = int(arg)
    if opt in (comp['--cores'], "--cores"):
        cores = int(arg)
    if opt in (comp['--randclr'], "--randclr"):
        randclr = int(arg)

ldets = lenDev.split(":")
adets = angDev.split(":")

ares = "(random)" if adets[1] == 1 else "(fixed)"
lres = "(random)" if ldets[1] == 1 else "(fixed)"
rclr = "Yes" if randclr == 1 else "No"


desc = f"Name: {name}\n"
desc = desc + f"Series: {series}\n"
desc = desc + f"Number of levels: {ncount}\n"
desc = desc + f"Syncpoints: {syncpoints} degress\n"
desc = desc + f"Flower size: {flowersize}px\n"
desc = desc + f"Expanding 'flowers': {growflower}\n"
desc = desc + f"Color Palette: {usecolor}\n"
desc = desc + f"Alt Color Palette: {use_alt_color}\n"
desc = desc + f"Random pallete colors: {rclr}\n"

desc = desc + f"Line style: Style {style}\n"
desc = desc + f"Line length: {length}px\n"
desc = desc + f"Length deviation: { int( float(ldets[0])*100 ) }% {lres}\n"

desc = desc + f"Cores: {cores}\n"
desc = desc + f"Resolution: 3020px x 2691px\n"
desc = desc + f"Outline: {outline}\n"
desc = desc + f"From {SES[0]} deg. To {SES[1]}, Stepped by: {SES[2]} deg.\n"
desc = desc + f"Angular deviation: { int( float(adets[0])*100 ) }% {ares}\n"

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(desc, flush=True)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

start = SES[0]
end = SES[1]
step = SES[2]

for angle in range(start,end,step):
    fromangle = angle
    toangle = angle

    cmd = f"./_{name}_{series}_hex_builder_lapse.py   "
    cmd = cmd + f" --length {length}"
    cmd = cmd + f" --angle {angle}"
    cmd = cmd + f" --ANGdeviation {angDev}"
    cmd = cmd + f" --LENdeviation {lenDev}"
    cmd = cmd + f" --count {ncount}"
    cmd = cmd + f" --usecolor {usecolor}"
    cmd = cmd + f" --use_alt_color {use_alt_color}"
    cmd = cmd + f" --subdir {name}"  # unecesary??
    cmd = cmd + f" --style {style}"
    cmd = cmd + f" --flowersize {flowersize}"
    cmd = cmd + f" --desklock {locked}"
    cmd = cmd + f" --outline {outline}"
    cmd = cmd + f" --growflower {growflower}"
    cmd = cmd + f" --name {name}"
    cmd = cmd + f" --series {series}"
    cmd = cmd + f" --syncpoints {syncpoints}"
    cmd = cmd + f" --cores {cores}"
    cmd = cmd + f" --randclr {randclr}"
    cmd = cmd + " > /dev/null"



    output = subprocess.getoutput(cmd)
    print(f"{name} {output} {cmd}", flush=True)

    t = datetime.datetime.fromtimestamp(time.time())
    ts = t.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)")

    xdesc = desc + f"Created: {ts}\n"
    xdesc = xdesc + f"Base angle: {angle}\n"
    xdesc = xdesc + f"Command: {cmd}"

    f = open(f"/home/jw/books/tholonia/code/hexani/{name}_{series}/ORG/details/{name}_{angle}.txt", "a")
    f.write(xdesc)
    f.close()

