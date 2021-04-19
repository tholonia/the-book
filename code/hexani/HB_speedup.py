#!/usr/bin/env python

import getopt
import sys
from os import path
import toml, os, sys, random, shutil
sys.path.insert(1, '/home/jw/books/tholonia/code/hexani')
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

# ┌───────────────────────────────────────────────────
# │ 🟠 initial vars
# └───────────────────────────────────────────────────
colors=["#f3160c","#f39f0c","#dcf30c","#56f30c","#0ce6f3","#0c56f3","#e145fe"]
COLOR=random.choice(colors)

NAME=C['def']['name']
SERIES=C['def']['series']
PSN=C['def']['PSN']

# WD = f"{C['def']['root']}/{dir}"  # {/home/jw/books/tholonis/code}/hexani}/{TWIST_04}
# CWD = f"{C['def']['root']}/{dir}/prev" # {/home/jw/books/tholonis/code/hexani}/{TWIST_04}/prev

SLOW1=f"{WD}/prev/{NAME}_{SERIES}_UNI_SLOW"   # {/home/jw/books/tholonis/code/hexani}/{TWIST_04}/{TWIST}_series-{04}_image1
FAST1=f"{WD}/prev/{NAME}_{SERIES}_UNI_FAST"

SLOW2=f"{WD}/prev/{NAME}_{SERIES}_ALL_SLOW"
FAST2=f"{WD}/prev/{NAME}_{SERIES}_ALL_FAST"

SP=10 # spped of video acceleration

# ll.wccopy(f"{WD}/gif/cropped/{SLOW1}.mp4",f"{WD}/prev/") #copy the two final videos from ffmpeg to {/home/jw/books/tholonis/code/hexani}/{TWIST_04}/prev
# ll.wccopy(f"{WD}/gif/cropped/{SLOW2}.mp4",f"{WD}/prev/")

# ┌───────────────────────────────────────────────────
# │ 🟠 make fast vversions withhout re-encoding
# └───────────────────────────────────────────────────

#delete any old stuff
ll.wcdel(f"{WD}/prev/*.mov")
ll.wcdel(f"{WD}/prev/*.jpg")

printonly = False
ll.runthis(f"ffmpeg -y -i {SLOW1}.mp4 -c copy -f h264 {WD}/tmp/tmp1.h264","speedup-#100",thisprog,True,printonly)
ll.runthis(f"ffmpeg -y -r {SP} -i {WD}/tmp/tmp1.h264 -c copy {FAST1}.mp4","speedup-#101",thisprog,True,printonly)  # creates {WD}/prev/T_1_UNI_FAST.mp4

ll.runthis(f"ffmpeg -y -i {SLOW2}.mp4 -c copy -f h264 {WD}/tmp/tmp2.h264","speedup-#102",thisprog,True,printonly)
ll.runthis(f"ffmpeg -y -r {SP} -i {WD}/tmp/tmp2.h264 -c copy {FAST2}.mp4","speedup-#103",thisprog,True,printonly)  # creates {WD}/prev/T_1_ALL_FAST.mp4



# ┌───────────────────────────────────────────────────
# │ 🟠 make thumbnails
# └───────────────────────────────────────────────────
#get which frame to grab

numFrames = os.popen(f"mediainfo --Output=\"Video;%FrameCount%\" {SLOW2}.mp4").read()  # get number of frames from video
iNumFrames = 0
try:
    iNumFrames = int(numFrames)
    # framenum = int(iNumFrames * .3) # 30% into the video
except:
    print(f"FAILED to get numframes [{numFrames}]from {SLOW2}.mp4")
    pass
# !! Alternate frame choice method... assume there are 360 frames.  These frams tend to have better images, in general
framenum = "000"        # default, for testing anis that only have a few frames

if iNumFrames>= 360:    # if the ani is complete, default to frame 60
    framenum = "060"
    try:
        if int(C['def']['framenum']):       # if a framenum is defined in the toml file, use that
            framenum = C['def']['framenum']
    except:
        framenum = str(random.choice([108, 264, 306, 325])).zfill(3)  # if not, randomly choose a frame that will probably be OK

#
# test anis will have a frame number of 0
# finished anis will has a frame numner of 60, unless one is specifically defined


# for SLOW videos, just copy an existing gif
# !!! this does not when there are mot 360 frames available
# ll.runthis(f"convert {WD}/gif/cropped/hex-{str(framenum).zfill(3)}.gif  {CWD}/thumbnail_SLOW_1.jpg","#104",thisprog)
# ll.wccopy(f"{CWD}/thumbnail_SLOW_1.jpg",f"{CWD}/thumbnail_FAST_1.jpg")

# get thumbnail from video

#make TH for slow anf fast combined

# make for ALL
# first look for a prexisting thumbnail,
print(f"SEARCHING FOR THUMBNAIL: {WD}/zthumbnail_ALL_SLOW.jpg", flush=True)
if os.path.exists(f"{WD}/zthumbnail_ALL_SLOW.jpg"):
        ll.wccopy(f"{WD}/zthumbnail_ALL_SLOW.jpg", f"{WD}/prev/zthumbnail_ALL_SLOW.jpg")
        ll.wccopy(f"{WD}/zthumbnail_ALL_SLOW.jpg", f"{WD}/prev/zthumbnail_ALL_FAST.jpg")
else: # get one if not
    ll.runthis(f"ffmpeg -i {SLOW2}.mp4 -vf \"select=eq(n\\,{framenum})\" -vframes 1 {C['def']['root']}/tmp/00000001.jpg","speedup-#106a",thisprog,True,printonly)
    shutil.move(f"{WD}/tmp/00000001.jpg",f"{WD}/prev/zthumbnail_ALL_SLOW.jpg")
    ll.wccopy(f"{WD}/prev/zthumbnail_ALL_SLOW.jpg",f"{WD}/prev/zthumbnail_ALL_FAST.jpg")

#make TH for fast/slor unique

# ll.runthis(f"ffmpeg -i {SLOW2}.mp4 -vf \"select=eq(n\\,{framenum})\" -vframes 1 {C['def']['root']}/tmp/00000001.jpg","speedup-#106b",thisprog,True,printonly)
# shutil.move(f"{WD}/tmp/00000001.jpg",f"{WD}/prev/zthumbnail_ALL_SLOW.jpg")

# make for UNI
if os.path.exists(f"{WD}/zthumbnail_UNI_SLOW.jpg"):
        ll.wccopy(f"{WD}/zthumbnail_UNI_SLOW.jpg", f"{WD}/prev/zthumbnail_UNI_SLOW.jpg")
        ll.wccopy(f"{WD}/zthumbnail_UNI_SLOW.jpg", f"{WD}/prev/zthumbnail_UNI_FAST.jpg")
else: #
    ll.runthis(f"convert {WD}/gif/cropped/hex-{framenum}.gif  {WD}/prev/zthumbnail_UNI_SLOW.jpg")
    # ll.runthis(f"convert {WD}/gif/cropped/hex-{framenum}.gif  {WD}/prev/zthumbnail_UNI_SLOW.jpg")
    ll.wccopy(f"{WD}/prev/zthumbnail_UNI_SLOW.jpg",f"{WD}/prev/zthumbnail_UNI_FAST.jpg")
    # ll.wccopy(f"{WD}/prev/zthumbnail_UNI_SLOW.jpg",f"{WD}/prev/zthumbnail_UNI_FAST.jpg")
# ^^^^^^^^^^^^^^^^^^^^^


ll.wcdel(f"{WD}/tmp/*")

# pH1=300
# pH2=250
# pH3=125
pH1=100
pH2=75
pH3=100
pH2pos="0,120"
pH1pos="0,20"

Da=[
    ["NORMAL SPEED",    f"{WD}/prev/zthumbnail_UNI_SLOW.jpg",  f"{NAME} {SERIES} - individual","Yellow"],
    ["FAST 10x SPEED",  f"{WD}/prev/zthumbnail_UNI_FAST.jpg",  f"{NAME} {SERIES} - individual","Red"],
    ["NORMAL SPEED",    f"{WD}/prev/zthumbnail_ALL_SLOW.jpg",  f"{NAME} {SERIES} - composite","Yellow"],
    ["FAST 10x SPEED",  f"{WD}/prev/zthumbnail_ALL_FAST.jpg",  f"{NAME} {SERIES} - composite","Red"]
]

# F=f"{CWD}/thumbnail_SLOW_1.jpg"
# title="NORMAL SPEED"
# iname=f"{NAME} {SERIES} - individual"


for i in range(0,4):
    c=[0,1]
    src=f"{Da[i][1]}"
    tgt=f"{WD}/tmp/tmp{i}_c1.jpg"
    # copy original to first step
    shutil.copy2(src,tgt)

    title=Da[i][0]
    fname=Da[i][1]
    subtitle=Da[i][2]
    tcolor=Da[i][3]

    # resize
    ll.runthis(f"convert {src} -resize 1280x {tgt}","speedup-#110ccx",thisprog) #3

    c=[1,2]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"

    ll.runthis(f"convert {src} -size 1280x720 -resize 60% xc:black +swap -gravity center  -composite {tgt}","speedup-#111ccx",thisprog,True,printonly) #4
    # add text

    c=[2,3]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"
    ll.runthis(f"convert {src} -gravity North  -pointsize {pH1} -fill {tcolor} -font Times-Bold -draw \"text {pH1pos} '{title}'\" {tgt}","speedup-#108ccx",thisprog,True,printonly) #1

    c=[3,4]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"
    ll.runthis(f"convert {src} -gravity North  -pointsize {pH2} -fill cyan -font Helvetica-Bold -draw \"text {pH2pos} '{subtitle}'\" {tgt}","speedup-#109ccx",thisprog,True,printonly) #2
    #border

    c=[4,5]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"
    ll.runthis(f"convert {src}  -bordercolor \"{COLOR}\" -border 16 -pointsize {pH3} -fill white -font Times-Bold -gravity southwest -draw \"text 35,10 '{PSN}\"  {tgt}","speedup-#112ccx",thisprog,True,printonly) #5
    ll.wccopy(f"{tgt}",f"{fname}")

# rm ./tmp.mp4  > /dev/null 2>&1

if (iNumFrames > 300):
    ll.runthis(f"HandBrakeCLI -i {SLOW1}.mp4 -o {WD}/tmp/tmp6.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O","speedup-#128",thisprog,True,printonly)
    shutil.copy2(f"{WD}/tmp/tmp6.mp4",f"{SLOW1}.mp4")

    ll.runthis(f"HandBrakeCLI -i {SLOW2}.mp4 -o {WD}/tmp/tmp7.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O","speedup-#129",thisprog,True,printonly)
    shutil.copy2(f"{WD}/tmp/tmp7.mp4",f"{SLOW2}.mp4")

    ll.runthis(f"HandBrakeCLI -i {FAST1}.mp4 -o {WD}/tmp/tmp8.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O","speedup-#130",thisprog,True,printonly)
    shutil.copy2(f"{WD}/tmp/tmp8.mp4",f"{FAST1}.mp4")

    ll.runthis(f"HandBrakeCLI -i {FAST2}.mp4 -o {WD}/tmp/tmp9.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O","speedup-#131",thisprog,True,printonly)
    shutil.copy2(f"{WD}/tmp/tmp9.mp4",f"{FAST2}.mp4")

# ll.wcdel(f"{FAST1}.mov")
# ll.wcdel(f"{FAST2}.mov")
ll.wcdel(f"{WD}/prev/*.mov")

# ll.wcdel(f"{WD}/prev/*.gif")
# ll.wcdel(f"{WD}/gif/[hg]*.gif")
ll.wcdel(f"{WD}/tmp/*.gif")
ll.wcdel(f"/tmp*.jpg")
ll.wcdel(f"{WD}/prev/*.h264")
