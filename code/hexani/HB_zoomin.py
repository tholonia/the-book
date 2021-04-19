#!/bin/python

import getopt
import sys
from os import path
import os
import glob
# from shutil import copy2
import shutil
import random
import toml
sys.path.insert(1, '/home/jw/books/tholonia/code/hexani/')
import lapselib as ll

thisprog = os.path.basename(__file__)

argv = sys.argv[1:]

run = 0
try:
    opts, args = getopt.getopt(argv, "r:", ["run="])
except getopt.GetoptError as err:
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-r", "--run"):
        run = int(arg)




ll.banner(thisprog)

cwd = os.getcwd()

wpath = f"{cwd}"
C = toml.load(f"{wpath}/build.toml")
Z = toml.load(f"{C['def']['repo']}/inc_zoomdims.toml")
# -- end load -----------------------
quiet = ""  # > /dev/null 2>&1"
printonly = False
# ┌───────────────────────────────────────────────────
# │ 🟠 make subdir for new image an apply trx (make white arrows black)
# └───────────────────────────────────────────────────
# cd gif/
# WCD=f"{WCD}/gif"
#echo "------------- UPDATING COLORS"

zoomdir = Z['crop']['zoomdims'][run][0]
zoomdim = Z['crop']['zoomdims'][run][1]

image1 = f"{C['def']['name']}_{C['def']['series']}_{zoomdir}_UNI"
image2 = f"{C['def']['name']}_{C['def']['series']}_{zoomdir}_ALL"

WD = f"{C['def']['root']}/{zoomdir}"
REPO = C['def']['repo']

ll.wcmkdir(f"{WD}")
ll.wcmkdir(f"{WD}/prev")
ll.wcmkdir(f"{WD}/cropped")
ll.wcmkdir(f"{WD}/tmp")

shutil.copy2(f"{C['def']['root']}/gif/cropped/gex-000.gif",f"{WD}/cropped/gex-000.gif")

# ┌───────────────────────────────────────────────────
# │ 🟠 make subdir for cropped all 'hex*.gif' images and crop them
# └───────────────────────────────────────────────────
#
# ll.wcdel(f"{WD}/*")
# ll.wcdel(f"{WD}/cropped/*")
# ll.wcdel(f"{WD}/prev/*")

print("------------- CROP ZOOM IMAGES",flush=True)

# for file in ll.sortglob(f"{C['def']['root']}/gif/*.gif"):
#     print(f"cropping {file}", flush=True)
#     ll.runthis(f"convert {file} -crop {zoomdim} +repage {WD}/cropped/{os.path.basename(file)}","zoom-#25",thisprog)

print(f"cropping file", flush=True)
ll.runthis(f"mogrify  -verbose -crop {zoomdim} +repage -path {WD}/cropped/ {C['def']['root']}/gif/*.gif ","zooom-#25",thisprog)

# ┌───────────────────────────────────────────────────
# │ 🟠 create animated gif (and color map)
# └───────────────────────────────────────────────────
# # ┌───────────────────────────────────────────────────
# # │ 🟠 set to black
# # └───────────────────────────────────────────────────
# shutil.copy2(f"{REPO}/blackbg.gif",f"{WD}/cropped/gex-000.gif")
# ll.runthis(f"convert {WD}/cropped/gex-000.gif -crop {zoomdim} +repage {WD}/cropped/gex-000.gif", "zoom-#25", thisprog)
#
# ┌───────────────────────────────────────────────────
# │ 🟠 Alpha off
# └───────────────────────────────────────────────────
print(f"Removing ALPHA channel...", flush=True)
#for file in ll.sortglob(f"{WD}/cropped/?ex*.gif"):
#       print(f"cropping {file}", flush=True)
#      shutil.copy2(file,f"{WD}/cropped/nt_{os.path.basename(file)}")

for file in ll.sortglob(f"{WD}/cropped/?ex*.gif"):
      shutil.copy2(file,f"{WD}/cropped/nt_{os.path.basename(file)}")

print(f"alpha off file", flush=True)
ll.runthis(f"mogrify  -verbose -alpha Off -path {WD}/cropped {WD}/cropped/nt_hex*.gif","zoom-#29",thisprog)

# mogrify -verbose -crop 1024x1024+1298+1285 +repage -path /home/jw/books/tholonia/code/hexani/A_SELECTED/RUN/V2th_04/z0/cropped/ /home/jw/books/tholonia/code/hexani/A_SELECTED/RUN/V2th_04/gif/*.gif


# copy existing cropped black image to NT and disable its transparency
shutil.copy2(f"{WD}/cropped/gex-000.gif",f"{WD}/cropped/nt_gex-000.gif")
ll.runthis(f"convert {WD}/cropped/nt_gex-000.gif -alpha Off {WD}/cropped/nt_gex-000.gif","zoom-#31", thisprog)

# turn on alpha for all images except the first, which is the BG
print("------------- ADD ALPHA",flush=True)
ll.runthis(f"convert {WD}/cropped/gex-000.gif -alpha Set {WD}/cropped/gex-000.gif","zoom-#32", thisprog)        #enable transparency on trans-hex - this is deafult so don;t need to reun
ll.runthis(f"convert {WD}/cropped/nt_gex-000.gif -alpha Set {WD}/cropped/nt_gex-000.gif","zoom-#33", thisprog)  #disable transparency on NO-trans-hex


# 'unoptimize' so can edit thedelay later on
ll.runthis(f"gifsicle --colors 256 -V --unoptimize --careful --delay {C['def']['delay']} {C['def']['compression']} --loopcount {WD}/cropped/nt_?ex-*.gif --output {WD}/prev/{image1}.gif","zoom-#34", thisprog)
ll.runthis(f"gifsicle --colors 256 -V --unoptimize --careful --delay {C['def']['delay']} {C['def']['compression']} --loopcount {WD}/cropped/?ex-*.gif    --output {WD}/prev/{image2}.gif","zoom-#35", thisprog)

# add extra 3 second delay for the last frame  JWFIX - not working?
ll.runthis(f"gifsicle -U -V --careful {WD}/prev/{image1}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/prev/ANI_{image1}.gif","zoom-#36", thisprog)
ll.runthis(f"gifsicle -U -V --careful {WD}/prev/{image2}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/prev/ANI_{image2}.gif","zoom-#36", thisprog)

# ┌───────────────────────────────────────────────────
# │ 🟠 make videos from gifs
# └───────────────────────────────────────────────────
ll.runthis(f'ffmpeg -y -i {WD}/prev/ANI_{image1}.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" {WD}/prev/{image1}_SLOW.mp4',"zoom-#38fff", thisprog)
ll.runthis(f'ffmpeg -y -i {WD}/prev/ANI_{image2}.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" {WD}/prev/{image2}_SLOW.mp4',"zoom-#39fff", thisprog)

# for the no-longer used white background
#ffmpeg -i ${name}_series-${series}_image-3.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-3.mp4
#ffmpeg -i ${name}_series-${series}_image-4.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-4.mp4

# ll.runthis(f"{WD}/_HB_speedup.py","#39", thisprog)


##########################################################
# speedup section
##########################################################

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

SLOW1=f"{WD}/prev/{NAME}_{SERIES}_{zoomdir}_UNI_SLOW"   # {/home/jw/books/tholonis/code/hexani}/{TWIST_04}/{TWIST}_series-{04}_image1
FAST1=f"{WD}/prev/{NAME}_{SERIES}_{zoomdir}_UNI_FAST"

SLOW2=f"{WD}/prev/{NAME}_{SERIES}_{zoomdir}_ALL_SLOW"
FAST2=f"{WD}/prev/{NAME}_{SERIES}_{zoomdir}_ALL_FAST"

SP=10 # spped of video acceleration

# ll.wccopy(f"{WD}/gif/cropped/{SLOW1}.mp4",f"{WD}/prev/") #copy the two final videos from ffmpeg to {/home/jw/books/tholonis/code/hexani}/{TWIST_04}/prev
# ll.wccopy(f"{WD}/gif/cropped/{SLOW2}.mp4",f"{WD}/prev/")

# ┌───────────────────────────────────────────────────
# │ 🟠 make fast vversions withhout re-encoding
# └───────────────────────────────────────────────────
#
# #delete any old stuff
# ll.wcdel(f"{WD}/prev/*.mov")
# ll.wcdel(f"{WD}/prev/*.jpg")
#
# printonly = False
ll.runthis(f"ffmpeg -y -i {SLOW1}.mp4 -c copy -f h264 {WD}/tmp/tmp1.h264","speedup-#100",thisprog,True,printonly)
ll.runthis(f"ffmpeg -y -r {SP} -i {WD}/tmp/tmp1.h264 -c copy {FAST1}.mp4","speedup-#101",thisprog,True,printonly)  # creates {WD}/prev/T_1_UNI_FAST.mp4
#
ll.runthis(f"ffmpeg -y -i {SLOW2}.mp4 -c copy -f h264 {WD}/tmp/tmp2.h264","speedup-#102",thisprog,True,printonly)
ll.runthis(f"ffmpeg -y -r {SP} -i {WD}/tmp/tmp2.h264 -c copy {FAST2}.mp4","speedup-#103",thisprog,True,printonly)  # creates {WD}/prev/T_1_ALL_FAST.mp4
#
#

# ┌───────────────────────────────────────────────────
# │ 🟠 make thumbnails
# └───────────────────────────────────────────────────
#get which frame to grab
numFrames = os.popen(f"mediainfo --Output=\"Video;%FrameCount%\" {SLOW2}.mp4").read()

print(f"mediainfo --Output=\"Video;%FrameCount%\" {SLOW2}.mp4",numFrames)

iNumFrames = int(numFrames)
# framenum = int(iNumFrames * .3) # 30% into the video

# !! Alternate frame choice method... assume there are 360 frames.  These frams tend to have better images, in general
framenum = "000"
if iNumFrames>= 360:
    framenum = "060"

    try:
        if int(C['def']['zoomframenum']): # check that it exists and is a string
            framenum = C['def']['zoomframenum']
    except:
        framenum = str(random.choice([108, 264, 306, 325])).zfill(3)


# for SLOW videos, just copy an existing gif
# !!! this does not when there are mot 360 frames available
# ll.runthis(f"convert {WD}/gif/cropped/hex-{str(framenum).zfill(3)}.gif  {CWD}/thumbnail_SLOW_1.jpg","#104",thisprog)
# ll.wccopy(f"{CWD}/thumbnail_SLOW_1.jpg",f"{CWD}/thumbnail_FAST_1.jpg")

# get thumbnail from video

#make TH for slow anf fast combined
ll.runthis(f"ffmpeg -i {SLOW2}.mp4 -vf \"select=eq(n\\,{framenum})\" -vframes 1 {WD}/tmp/00000001.jpg","speedup-#106a",thisprog,True,printonly)
shutil.move(f"{WD}/tmp/00000001.jpg",f"{WD}/prev/zthumbnail_ALL_SLOW_{zoomdir}.jpg")
ll.wccopy(f"{WD}/prev/zthumbnail_ALL_SLOW_{zoomdir}.jpg",f"{WD}/prev/zthumbnail_ALL_FAST_{zoomdir}.jpg")

#make TH for fast/slor unique

# ll.runthis(f"ffmpeg -i {SLOW2}.mp4 -vf \"select=eq(n\\,{framenum})\" -vframes 1 {C['def']['root']}/tmp/00000001.jpg","speedup-#106b",thisprog,True,printonly)
# shutil.move(f"{WD}/tmp/00000001.jpg",f"{WD}/prev/zthumbnail_ALL_SLOW.jpg")

# dup them
ll.runthis(f"convert {WD}/cropped/hex-{framenum}.gif  {WD}/prev/zthumbnail_UNI_SLOW_{zoomdir}.jpg")
# ll.runthis(f"convert {WD}/gif/cropped/hex-{framenum}.gif  {WD}/prev/zthumbnail_UNI_SLOW_{zoomdir}.jpg")
ll.wccopy(f"{WD}/prev/zthumbnail_UNI_SLOW_{zoomdir}.jpg",f"{WD}/prev/zthumbnail_UNI_FAST_{zoomdir}.jpg")
# ll.wccopy(f"{WD}/prev/zthumbnail_UNI_SLOW_{zoomdir}.jpg",f"{WD}/prev/zthumbnail_UNI_FAST_{zoomdir}.jpg")

# ll.wcdel(f"{WD}/tmp/*")

# pH1=300
# pH2=250
# pH3=125
pH1=90
pH2=75
pH3=100
pH2pos="0,120"
pH1pos="0,20"

Da=[
    ["NORMAL SPEED (zoomed)",    f"{WD}/prev/zthumbnail_UNI_SLOW_{zoomdir}.jpg",  f"{NAME} {SERIES} - individual","Yellow"],
    ["FAST 10x SPEED (zoomed)",  f"{WD}/prev/zthumbnail_UNI_FAST_{zoomdir}.jpg",  f"{NAME} {SERIES} - individual","Red"],
    ["NORMAL SPEED (zoomed)",    f"{WD}/prev/zthumbnail_ALL_SLOW_{zoomdir}.jpg",  f"{NAME} {SERIES} - composite","Yellow"],
    ["FAST 10x SPEED (zoomed)",  f"{WD}/prev/zthumbnail_ALL_FAST_{zoomdir}.jpg",  f"{NAME} {SERIES} - composite","Red"]
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
    ll.runthis(f"convert {src} -resize 1280x720 {tgt}","speedup-#110ccx",thisprog) #3

    # ll.runthis(f"convert -size 1280x720 -resize 60% xc:black +swap  -gravity South -fill navy -stroke white  -strokewidth 4 -draw \"rectangle 40,1240 1215,900\"  {tgt}.JPG {WD}/tmp/tmp{i}_c{c[0]}.jpg")

    c=[1,2]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"

    ll.runthis(f"convert {src} -size 1280x720 -resize 60% xc:black +swap -gravity center -composite {tgt}","speedup-#111ccx",thisprog,True,printonly) #4
    # add text
    # add text

    # print(tgt)
    # if tgt == f"{WD}/tmp/tmp0_c2.jpg":
    #     ll.runthis(f"mogrify {tgt} -size 1280x720 -gravity South -fill navy -stroke white  -strokewidth 4 -draw \"rectangle 40,1240 1215,900\"","speedup-#111ccx",thisprog,True,printonly) #4
    #
    # exit()

    c=[2,3]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"
    ll.runthis(f"convert {src} -gravity North -pointsize {pH1}  -undercolor Black  -fill {tcolor} -font Times-Bold -draw \"text {pH1pos} '{title}'\" {tgt}","speedup-#108ccx",thisprog,True,printonly) #1

    c=[3,4]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"
    ll.runthis(f"convert {src} -gravity North  -pointsize {pH2} -undercolor Black  -fill cyan -font Helvetica-Bold -draw \"text {pH2pos} '{subtitle}'\" {tgt}","speedup-#109ccx",thisprog,True,printonly) #2
    #border

    c=[4,5]
    src=f"{WD}/tmp/tmp{i}_c{c[0]}.jpg"
    tgt=f"{WD}/tmp/tmp{i}_c{c[1]}.jpg"
    ll.runthis(f"convert {src}  -bordercolor \"{COLOR}\" -border 16 -undercolor Black  -pointsize {pH3} -fill white -font Times-Bold -gravity southwest -draw \"text 35,10 '{PSN}\"  {tgt}","speedup-#112ccx",thisprog,True,printonly) #5
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
ll.wcdel(f"/tmp/tmp*.jpg")
ll.wcdel(f"{WD}/tmp/*.h264")

ll.runthis(f"aplay /usr/lib/libreoffice/share/gallery/sounds/nature2.wav","zoom-#40", thisprog)