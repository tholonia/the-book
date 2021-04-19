#!/usr/bin/env python

import getopt
import sys
from os import path
import os
import glob
from shutil import copy2

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
Z = toml.load(f"{C['def']['repo']}/inc_zoomdims.toml")
# -- end load -----------------------
WD = C['def']['root']
REPO = C['def']['repo']
quiet = ""  # > /dev/null 2>&1"

# dir = f"{C['def']['name']}_{C['def']['series']}"
# wpath = f"{C['def']['root']}/{dir}"


# D=f"{wpath}"

# WCD = D

# cd ${D}
#-------------------------------------------------------------------------------DELETE
# os.remove(f"{C['def']['root']}/nohup.out")
ll.runthis(f"echo \"\" > {C['def']['root']}/nohup.out")
ll.wcdel(f"{C['def']['root']}/tmp/*")


# ======= START premovie stuff =======================================================

ll.wcdel(f"{WD}/gif/*")

# ┌───────────────────────────────────────────────────
# │ 🟠 make subdir for image type and cope all type images into it
# └───────────────────────────────────────────────────
ll.wcmkdir(f"{WD}/gif")
# ll.runthis(f"cp {WCD}/ORG/hex*.gif {WCD}/gif/","#22",thisprog)
# print(f"{WCD}/ORG/hex*.gif",f"{WCD}/gif/")
# copy2(f"{WCD}/ORG/hex*.gif",f"{WCD}/gif/")

ll.wccopy(f"{WD}/ORG/hex*.gif",f"{WD}/gif/")

# ┌───────────────────────────────────────────────────
# │ 🟠 make subdir for new image an apply trx (make white arrows black)
# └───────────────────────────────────────────────────
# cd gif/
# WCD=f"{WCD}/gif"
#echo "------------- UPDATING COLORS"
copy2(f"{REPO}/blackbg.gif",f"{WD}/gif/gex-000.gif")

# ┌───────────────────────────────────────────────────
# │ 🟠 make subdir for cropped all 'hex*.gif' images and crop them
# └───────────────────────────────────────────────────
ll.wcmkdir(f"{WD}/gif/cropped/")

print("------------- CROP IMAGES",flush=True)
# for file in ll.sortglob(f"{WD}/gif/*.gif"):
#     print(f"cropping {file}", flush=True)
#     ll.runthis(f"convert {file} -crop {Z['crop']['cropto']} +repage {WD}/gif/cropped/{os.path.basename(file)}","gif-#25",thisprog)

print(f"cropping file", flush=True)
ll.runthis(f"mogrify  -verbose -crop {Z['crop']['cropto']} +repage -path {WD}/gif/cropped {C['def']['root']}/gif/*.gif","gif-#25",thisprog)

# ┌───────────────────────────────────────────────────
# │ 🟠 move to 'cropped' dir, create animated gif (and color map)
# └───────────────────────────────────────────────────
# cd cropped
# WCD=f"{WCD}/cropped"
# # delete any old copies in gif/cropped/*.gif
# ll.wcdel(f"{WCD}/{C['def']['name']}*.gif")

#delete all previous processed 'nt*.gif' images
ll.wcdel(f"{WD}/gif/cropped/nt_*")

# ┌───────────────────────────────────────────────────
# │ 🟠 set to black
# └───────────────────────────────────────────────────
copy2(f"{REPO}/blackbg.gif",f"{WD}/gif/cropped/gex-000.gif")
# ┌───────────────────────────────────────────────────
# │ 🟠 Alpha off
# └───────────────────────────────────────────────────
print(f"Removing ALPHA channel...", flush=True)
# for file in ll.sortglob(f"{WD}/gif/cropped/?ex*.gif"):
#     print(f"cropping {file}", flush=True)
#     ll.runthis(f"convert {file} -alpha Off {WD}/gif/cropped/nt_{os.path.basename(file)}","gif-#29",thisprog)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(f"COPYING all files ({WD}/gif/cropped/?ex*.gif) to nt_")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for file in ll.sortglob(f"{WD}/gif/cropped/?ex*.gif"):
      print(f">> COPYING: {file} to {WD}/gif/cropped/nt_{os.path.basename(file)}")
      copy2(file,f"{WD}/gif/cropped/nt_{os.path.basename(file)}")

print(f"alpha off file", flush=True)
ll.runthis(f"mogrify  -verbose -alpha Off -path {WD}/gif/cropped {WD}/gif/cropped/nt_hex*.gif","gif-#29",thisprog)



# copy existing cropped black image to NT and disable its transparency
copy2(f"{WD}/gif/cropped/gex-000.gif",f"{WD}/gif/cropped/nt_gex-000.gif")
ll.runthis(f"convert {WD}/gif/cropped/nt_gex-000.gif -alpha Off {WD}/gif/cropped/nt_gex-000.gif","gif-#31", thisprog)

# turn on alpha for all images except the first, which is the BG
print("------------- ADD ALPHA",flush=True)
ll.runthis(f"convert {WD}/gif/cropped/gex-000.gif -alpha Set {WD}/gif/cropped/gex-000.gif","gif-#32", thisprog)        #enable transparency on trans-hex - this is deafult so don;t need to reun
ll.runthis(f"convert {WD}/gif/cropped/nt_gex-000.gif -alpha Set {WD}/gif/cropped/nt_gex-000.gif","gif-#33", thisprog)  #disable transparency on NO-trans-hex

# echo "gifsicle --colors 256 -V --unoptimize --careful --delay ${delay} ${compression} --loopcount nt_?ex-*.gif > ${name}_series-${series}_image-1.gif"
# echo "gifsicle --colors 256 -V --unoptimize --careful --delay ${delay} ${compression} --loopcount    ?ex-*.gif > ${name}_series-${series}_image-2.gif"



image1 = f"{C['def']['name']}_{C['def']['series']}_UNI"
image2 = f"{C['def']['name']}_{C['def']['series']}_ALL"

# 'unoptimize' so can edit thedelay later on
ll.runthis(f"gifsicle --colors 256 -V --unoptimize --careful --delay {C['def']['delay']} {C['def']['compression']} --loopcount {WD}/gif/cropped/nt_?ex-*.gif --output {WD}/prev/{image1}.gif","gif-#34", thisprog)
ll.runthis(f"gifsicle --colors 256 -V --unoptimize --careful --delay {C['def']['delay']} {C['def']['compression']} --loopcount {WD}/gif/cropped/?ex-*.gif    --output {WD}/prev/{image2}.gif","gif-#35", thisprog)

# add extra 3 second delay for the last frame  JWFIX - not working?
ll.runthis(f"gifsicle -U -V --careful {WD}/prev/{image1}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/prev/ANI_{image1}.gif","gif-#36", thisprog)
ll.runthis(f"gifsicle -U -V --careful {WD}/prev/{image2}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/prev/ANI_{image2}.gif","gif-#36", thisprog)

os.remove(f"{WD}/prev/{image1}.gif")
os.remove(f"{WD}/prev/{image2}.gif")


# ll.runthis(f"gifsicle -U -V --careful {image1}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/tmp/tmp.gif","gif-#36", thisprog)
# ll.runthis(f"gifsicle -U -V --careful {image1}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/tmp/tmp.gif && mv {WD}/tmp/tmp.gif {image1}.gif","gif-#36", thisprog)
# ll.runthis(f"gifsicle -U -V --careful {image1}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/tmp/tmp.gif && mv {WD}/tmp/tmp.gif {image1}.gif","gif-#36", thisprog)

# ll.runthis(f"gifsicle -U -V --careful {image2}.gif \"#0--1\" -d300 \"#-1\" --output {WD}/tmp/tmp.gif && mv {WD}/tmp/tmp.gif {image2}.gif","gif-#37", thisprog)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !! This is the final 'art' product
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# =================== END premovie =====================================================


# ┌───────────────────────────────────────────────────
# │ 🟠 make videos from gifs
# └───────────────────────────────────────────────────

# target1 = f"{WD}/prev/{C['def']['name']}_series-{C['def']['series']}_image-1.mp4"
# target2 = f"{WD}/prev/{C['def']['name']}_series-{C['def']['series']}_image-2.mp4"
#
# source1 = f"{WD}/prev/{C['def']['name']}_series-{C['def']['series']}_image-1.gif"
# source2 = f"{WD}/prev/{C['def']['name']}_series-{C['def']['series']}_image-2.gif"
ll.runthis(f'ffmpeg -y -i {WD}/prev/ANI_{image1}.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" {WD}/prev/{image1}_SLOW.mp4',"gif-#38fff", thisprog)
ll.runthis(f'ffmpeg -y -i {WD}/prev/ANI_{image2}.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" {WD}/prev/{image2}_SLOW.mp4',"gif-#39fff", thisprog)

# for the no-longer used white background
#ffmpeg -i ${name}_series-${series}_image-3.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-3.mp4
#ffmpeg -i ${name}_series-${series}_image-4.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-4.mp4

ll.runthis(f"{WD}/_HB_speedup.py","#39", thisprog)
ll.runthis(f"aplay /usr/lib/libreoffice/share/gallery/sounds/curve.wav","gif-#40", thisprog)

print("=============================================================================",flush=True)
print(f"FINISHED: {WD}",flush=True)
print("=============================================================================",flush=True)
