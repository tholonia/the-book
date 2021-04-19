#!/usr/bin/python

import os,sys,getopt, time, datetime, subprocess
import os.path
from os import path

import toml
sys.path.insert(1, '/home/jw/books/tholonia/code/hexani/')
import lapselib as ll
thisprog = os.path.basename(__file__)
ll.banner(thisprog)

# -- load config data ------------
cwd = os.getcwd()

# try:
#     opts, args = getopt.getopt(argv, "d:", ["dir="])
# except getopt.GetoptError as err:
#     sys.exit(2)
# for opt, arg in opts:
#     if opt in ("-d", "--dir"):
#         dir = arg
#         tmp = dir.split("_")
#         name = tmp[0]
#         series = tmp[1]

wpath = f"{cwd}"

C = toml.load(f"{wpath}/build.toml")
WD = C['def']['root']
# -- end load -----------------------

angDev	        = C['args']['angDev']
lenDev	        = C['args']['lenDev']
usecolor	    = C['args']['usecolor'][0]
use_alt_color	= C['args']['usecolor'][1]
ncount	        = C['args']['ncount']
name		    = C['def']['name']
length	        = C['args']['length']
angle	        = C['args']['angle']
style	        = C['args']['style']
flowersize	    = C['args']['flowersize']
desklock	    = C['def']['desklock']
outline	        = C['args']['outline'][0]
growflower	    = C['args']['growflower']
series	        = C['def']['series']
syncpoints	    = C['args']['syncpoints']
cores	        = C['args']['cores']
randclr	        = C['args']['randclr']

start = C['args']['SES'][0]
end = C['args']['SES'][1]
step = C['args']['SES'][2]

lengthr = C['args']['length'][0][0]
lrsub = int(C['args']['length'][0][1])
lrfun = C['args']['length'][0][2]
# lAry = tmp[1].split(",")
lengthl = C['args']['length'][1][0]
llsub = int(C['args']['length'][1][1])
llfun = C['args']['length'][1][2]

ldets = C['args']['angDev'][0] #lenDev.split(":")
adets = C['args']['angDev'][1] #angDev.split(":")


ares = "(random)" if C['args']['angDev'][1] == 1 else "(fixed)"
lres = "(random)" if C['args']['lenDev'][1] == 1 else "(fixed)"
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
desc = desc + f"Line (left) length: {lengthl}px\n"
desc = desc + f"Line (right) length: {lengthr}px\n"
desc = desc + f"Length deviation: { C['args']['lenDev'][1] * 100 }% {lres}\n"

desc = desc + f"Cores: {cores}\n"
desc = desc + f"Resolution: 3020px x 2691px\n"
desc = desc + f"Outline: {outline}\n"
desc = desc + f"From {start} deg. To {end}, Stepped by: {step} deg.\n"
desc = desc + f"Angular deviation: { C['args']['angDev'][1] * 100 }% {ares}\n"

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
dline = "(i.e, 0 length means only the arrowhead exist)" if ((int(lengthl) == 0) or (int(lengthr) == 0)) else ""




predescfile= f"{WD}/predescription.txt"
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
md = md + f"This animated GIF (or video) is made up of {end-1} images, each separated by {step} "
md = md + f"degree (with a deviation of { adets*100 }%).  Each image is 3020px x 2691px, and shows {ncount} "
md = md + f"levels of bifurcation of lines that are {lengthr}px long for the right, and {lengthl}px long for the left {dline}, which can change by { ldets*100 }%.  Each "
md = md + f"line is terminated with an arrowhead in the 'starboard' side of the line, "
md = md + f"thus indicating the line's direction.  The arrowheads are {flowersize}px long, and "
md = md + f"given that they are geometrically created relative to the line, they will be "
md = md + f"different shapes at different degrees.  They are perfect and accurate arrowheads at 60 "
md = md + f"degrees.  The colors, widths, angels, and lengths and determined  algorithmically. \n"
md = md + f"\n"
md = md + f"The Background \n"
md = md + f"----------------- \n"
md = md + f"This animated GIF is based on quaternary math and "
md = md + f"synergetic geometry as described in the book 'Tholonia: The mechanics of existential "
md = md + f"awareness.', by Duncan Stroud. Briefly, this image is the result of a single line that splits "
md = md + f"itself into two lines, {ncount} times.  The variables and the colors, line widths and lengths, and angles, and the amount "
md = md + f"of unpredictability allowed. \n"
md = md + f"\n"
md = md + f"This animation (and many more) was specifically created to be used as a "
md = md + f"'brain hacking' tool.  Simply watching it (over time, of course) will cause "
md = md + f"the brain to form new pattern recognition abilities, new neural connections, "
md = md + f"and as a result, new physiologically based cognitive abilities. \n"
md = md + f"\n"
md = md + f"Each frame is paused for 600 milliseconds (in the original GIF animation) as this the amount of time it "
md = md + f"takes the brain to instantiate a concept, such as thoughts to words, "
md = md + f"intention to movement, etc.  Each image is one degree apart deliberately to "
md = md + f"allow the brain the register a fixed image rather than see a continuously "
md = md + f"moving image. "
md = md + f"\n"

filename = f"{WD}/DESCRIPTION.txt"
# print(">>>>>>>>",flush=True)
# print(f"{filename}",flush=True)
# print("<<<<<<<<",flush=True)
f = open(filename, "w")
f.write(md)
f.close()

