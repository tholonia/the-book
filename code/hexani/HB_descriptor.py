#!/usr/bin/python

import os,sys,getopt, time, datetime, subprocess
import os.path
from os import path


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

start = SES[0]
end = SES[1]
step = SES[2]


descriptions = {
            'random': "randomly chosen",
            'denimbamboo': "manually selected",
            'greens': "selections of green",
            'browns': "selections of brown",
            'darkgrays': "dark grayscale",
            'lightgrays': "light grayscale",
            'default': "manually selected",
            'medical_gray': "manually selected",
            'medical_gray_3': "manually selected",
            'aura_red': "manually selected",
            'pi': "determined by the first 1,000 digits of PI",
            'progressive3': "algorithmically determine spectrum",
            'progressive4': "algorithmically determine spectrum",
            'SinSinSin': "determined by three (slow) sine waves",
            'SinSinSinFast': "determined by three (fast) sine waves",
            'SinCosSin': "determined by three (slow) sine and cosine waves",
            'SinCosDelta': "determined by a (slow) sine and cosine wave, and their difference",
            'SinCosDeltaFast': "determined by a (fast) sine and cosine wave, and their difference",
            'prog_A': "determined by 3 (slow) sine waves seperated by the Golden Mean (1.618/0.618)",
            'prog_B': "determined by 3 (slow) sine waves seperated by harmonics of 60 degrees",
            'prog_C': "determined by 3 (slow) sine waves seperated by harmonics of the SQRT(2)",
            'prog_C_fast': "determined by 3 (fast) sine waves seperated by harmonics of the SQRT(2)",
            'prog_C_medium':"determined by 3 (medium) sine waves seperated by harmonics of the SQRT(2)",
}
dline = "(i.e, the lines do not exist at all, only the arrowheads... in this version)" if (int(length) == 0) else ""




predescfile= f"/home/jw/books/tholonia/code/hexani/{name}_{series}/predescription.txt"
pre = ""
if path.exists(predescfile):
    with open(predescfile, 'r') as file:
        pre = file.read().replace('\n', '')
else:
    f = open(predescfile, "w")
    f.write("")
    f.close()

md = ""
md = md + f"{pre}\n"
md = md + f"\n"
md = md + f"'{name}', series {series}, image 1 (seperate images, black background)\n"
md = md + f"'{name}', series {series}, image 2 (overlaid images, black background)\n"
md = md + f"'{name}', series {series}, image 3 (seperate images, white background)\n"
md = md + f"'{name}', series {series}, image 4 (overlaid images, white background)\n"
md = md + f"\n"
md = md + f"Details\n"
md = md + f"------------ \n"
md = md + f"This animated GIF (or video) is made up of {int(SES[1])-1} images, each separated by 1 "
md = md + f"degree (with a deviation of { int( float(adets[0])*100 ) }%).  Each image is 3020px x 2691px, and shows {ncount} "
md = md + f"levels of bifurcation of lines {length}px each {dline}, which can change by { int( float(ldets[0])*100 ) }%.  Each "
md = md + f"line is terminated with an arrowhead in the 'starboard' side of the line, "
md = md + f"thus indicating the line's direction.  The arrowheads are {flowersize}px long, and "
md = md + f"given that they are geometrically created relative to the line, they will be "
md = md + f"different shapes at different degrees.  They are perfect arrowheads at 60 "
md = md + f"degrees.  The {ncount} generations of lines are drawn with the line "
md = md + f"widths of {style}, and the colors are {descriptions[usecolor]}. \n"
md = md + f"\n"
md = md + f"The Background \n"
md = md + f"----------------- \n"
md = md + f"This video is made from an animated GIF that is based on quaternary math and "
md = md + f"synergetic geometry as described in the book 'Tholonia: The mechanics of existential "
md = md + f"awareness.', by Duncan Stroud. Briefly, this image is the result of a single line that splits "
md = md + f"itself into two lines, six times.  The variables are the colors, the amount "
md = md + f"of unpredictability allowed, the length and thickness of the lines, the "
md = md + f"artifact at the end of each line, and a few other small details. \n"
md = md + f"\n"
md = md + f"This animation (and many more) was specifically created to be used as a "
md = md + f"'brain hacking' tool.  Simply watching it (over time, of course) will cause "
md = md + f"the brain to form new pattern recognition abilities, new neural connections, "
md = md + f"and as a result, new perspectives of reality. \n"
md = md + f"\n"
md = md + f"Each frame is paused for 600 milliseconds as this the amount of time it "
md = md + f"takes the brain to instantiate a concept, such as thoughts to words, "
md = md + f"intention to movement, etc.  Each image is one degree apart deliberately to "
md = md + f"allow the brain the register a fixed image rather than see a continuously "
md = md + f"moving image. "
md = md + f"\n"

filename = f"/home/jw/books/tholonia/code/hexani/{name}_{series}/DESCRIPTION.txt"
print("---------------------------------------------")
print(f"{filename}")
print("---------------------------------------------")
f = open(filename, "w")
f.write(md)
f.close()

