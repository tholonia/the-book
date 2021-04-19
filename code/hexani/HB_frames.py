#!/usr/bin/python

import os,sys,getopt, subprocess


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
#
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

lengthl = C['args']['length'][1][0]
llsub = int(C['args']['length'][1][1])
llfun = C['args']['length'][1][2]

ldets = C['args']['angDev'][0]
adets = C['args']['angDev'][1]


ares = "(random)" if C['args']['angDev'][1] == 1 else "(fixed)"
lres = "(random)" if C['args']['lenDev'][1] == 1 else "(fixed)"
rclr = "Yes" if randclr == 1 else "No"

# desc = f"Name: {name}\n"
# desc = desc + f"Series: {series}\n"
# desc = desc + f"Number of levels: {ncount}\n"
# desc = desc + f"Syncpoints: {syncpoints} degress\n"
# desc = desc + f"Flower size: {flowersize}px\n"
# desc = desc + f"Expanding 'flowers': {growflower}\n"
# desc = desc + f"Color Palette: {usecolor}\n"
# desc = desc + f"Alt Color Palette: {use_alt_color}\n"
# desc = desc + f"Random pallete colors: {rclr}\n"
#
# desc = desc + f"Line style: Style {style}\n"
# desc = desc + f"Line length: {length}px\n"
# desc = desc + f"Length deviation: { ldets*100 }% {lres}\n"
#
# desc = desc + f"Cores: {cores}\n"
# desc = desc + f"Resolution: 3020px x 2691px\n"
# desc = desc + f"Outline: {outline}\n"
# desc = desc + f"From {start} deg. To {end}, Stepped by: {step} deg.\n"
# desc = desc + f"Angular deviation: { adets*100  }% {ares}\n"
#
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",flush=True)
# print(desc, flush=True)
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",flush=True)



Xcmd = ""
if (C['def']['background'][1]):
    Xcmd = f"/usr/bin/xvfb-run -noreset -w 3 -d -e {WD}/Xerrors.txt"


for angle in range(start,end,step):
    fromangle = angle
    toangle = angle


    cmd = f"{Xcmd} ./_HB_lapse.py --angle {angle}"
    ll.runthis(cmd, "#50", thisprog)

    # t = datetime.datetime.fromtimestamp(time.time())
    # ts = t.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)")
    #
    # xdesc = desc + f"Created: {ts}\n"
    # xdesc = xdesc + f"Base angle: {angle}\n"
    # xdesc = xdesc + f"Command: {cmd}"
    #
    # f = open(f"{WD}/ORG/details/details_{name}_{series}_{angle}.txt", "a")
    # f.write(xdesc)
    # f.close()

