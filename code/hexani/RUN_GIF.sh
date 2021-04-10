#!/bin/bash

name=$1
series=$2
delay=$3
psn=$4


DIR="$1_$2"

#compression="-O3"
compression=""


cd /home/jw/books/tholonia/code/hexani/${DIR}
rm -rf gif > /dev/null 2>&1

D="/home/jw/books/tholonia/code/hexani/${DIR}"
################################################
# make subdir for image type and cope all type images into it
################################################
mkdir gif > /dev/null 2>&1
cp ${D}/ORG/hex*.gif gif/

################################################
# make subdir for new image an apply trx (make white arrows black)
################################################
cd gif/
#echo "------------- UPDATING COLORS"
#for a in hex*.gif;do echo $a && ../CH_CLR.sh $a; done

################################################
# make pause frames
################################################
echo "------------- CREATE PAUSE FRAMES"

cp ${D}/../blackbg.gif gex-000.gif
#cp hex-000.gif hex-000b.gif
#cp hex-000.gif hex-000c.gif
#cp hex-000.gif hex-000d.gif
#
#cp hex-030.gif hex-030a.gif
#cp hex-030.gif hex-030b.gif
#cp hex-030.gif hex-030c.gif
#
#cp hex-060.gif hex-060a.gif
#cp hex-060.gif hex-060b.gif
#cp hex-060.gif hex-060c.gif
#
#cp hex-090.gif hex-090a.gif
#cp hex-090.gif hex-090b.gif
#cp hex-090.gif hex-090c.gif
#
#cp hex-120.gif hex-120a.gif
#cp hex-120.gif hex-120b.gif
#cp hex-120.gif hex-120c.gif
#
#cp hex-180.gif hex-180a.gif
#cp hex-180.gif hex-180b.gif
#cp hex-180.gif hex-180c.gif
#
#cp hex-210.gif hex-210a.gif
#cp hex-210.gif hex-210b.gif
#cp hex-210.gif hex-210c.gif
#
#cp hex-240.gif hex-240a.gif
#cp hex-240.gif hex-240b.gif
#cp hex-240.gif hex-240c.gif
#
#cp hex-270.gif hex-270a.gif
#cp hex-270.gif hex-270b.gif
#cp hex-270.gif hex-270c.gif
#
#cp hex-300.gif hex-300a.gif
#cp hex-300.gif hex-300b.gif
#cp hex-300.gif hex-300c.gif
#
#cp hex-330.gif hex-330a.gif
#cp hex-330.gif hex-330b.gif
#cp hex-330.gif hex-330c.gif
#
#cp hex-360.gif hex-360a.gif
#cp hex-360.gif hex-360b.gif
#cp hex-360.gif hex-360c.gif


# to suspend the last frome for 3.6 seconds

cp hex-360.gif iex-360.1.gif
cp hex-360.gif iex-360.2.gif
cp hex-360.gif iex-360.3.gif
cp hex-360.gif iex-360.4.gif
cp hex-360.gif iex-360.5.gif




################################################
# make subdir for cropped images and crop them
################################################
mkdir cropped/ > /dev/null 2>&1

echo "------------- CROP IMAGES"
for a in *.gif;do echo "${DIR} $a" && convert $a -crop 3020x2691+368+150 +repage cropped/$a;done

################################################
# create animated gif (and color map)
################################################
cd cropped
rm ${name}*.gif > /dev/null 2>&1

# remove trans
echo "------------- REMOVE ALPHA and COPY"
# turn off alpha - remove tranparency - for "nt*"
rm nt_* > /dev/null 2>&1


# ----------------------------------
# set to black
# ----------------------------------
cp ${D}/../blackbg.gif gex-000.gif
for a in ?ex*.gif;do echo "${DIR} $a" && convert $a -alpha Off nt_$a;done
cp ${D}/../blackbg.gif nt_gex-000.gif
convert nt_gex-000.gif -alpha Off nt_gex-000.gif

# turn on alpha for all images except the first, which is the BG
echo "------------- ADD ALPHA"
convert gex-000.gif -alpha Set gex-000.gif        #enable transparency on trans-hex
convert nt_gex-000.gif -alpha Set nt_gex-000.gif  #disable transparency on NO-trans-hex

echo "gifsicle --colors 256 -V --careful --delay ${delay} ${compression} --loopcount nt_?ex-*.gif > ${name}_series-${series}_image-1.gif"
echo "gifsicle --colors 256 -V --careful --delay ${delay} ${compression} --loopcount    ?ex-*.gif > ${name}_series-${series}_image-2.gif"

gifsicle --colors 256 -V --careful --delay ${delay} ${compression} --loopcount nt_?ex-*.gif > ${name}_series-${series}_image-1.gif
gifsicle --colors 256 -V --careful --delay ${delay} ${compression} --loopcount    ?ex-*.gif > ${name}_series-${series}_image-2.gif

## ----------------------------------
## set to white
## ----------------------------------
#cp ${D}/../whitebg.gif gex-000.gif
#for a in ?ex*.gif;do echo $a && convert $a -alpha Off nt_$a;done
#cp ${D}/../whitebg.gif nt_gex-000.gif
#convert nt_gex-000.gif -alpha Off nt_gex-000.gif
#
## turn on alpha for all images except the first, which is the BG
#echo "------------- ADD ALPHA"
#convert gex-000.gif -alpha Set gex-000.gif        #enable transparency on trans-hex
#convert nt_gex-000.gif -alpha Set nt_gex-000.gif  #disable transparency on NO-trans-hex
#for a in nt_?ex*.gif;do echo $a && convert $a -fill white -opaque black $a; done
#
#echo "------------- CREATE ANIMATION - FRAME - WHITE"
#gifsicle --colors 256 -V --careful --conserve-memory --delay ${delay} ${compression} --loopcount nt_hex-*.gif > tholonic_series-${series}_image-3.gif
##gwenview  ./ani_frame-black_series1_image1.gif
#
#echo "------------- CREATE ANIMATION - OVERLAY = WHITE"
#gifsicle --colors 256 -V --careful --conserve-memory --delay ${delay} ${compression} --loopcount hex-*.gif > tholonic_series-${series}_image-4.gif
##gwenview  ./ani_overlay-black_series1_image2.gif
#
#--------------------------------------------
ffmpeg -i ${name}_series-${series}_image-1.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-1.mp4
ffmpeg -i ${name}_series-${series}_image-2.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-2.mp4
#ffmpeg -i ${name}_series-${series}_image-3.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-3.mp4
#ffmpeg -i ${name}_series-${series}_image-4.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${name}_series-${series}_image-4.mp4

./speedup.sh ${name} ${series} ${psn}

aplay /usr/lib/libreoffice/share/gallery/sounds/curve.wav

echo "============================================================================="
echo "${DIR}"
echo "============================================================================="

#ffmpeg -i video.mp4 -map 0:v -c:v copy -bsf:v h264_mp4toannexb raw.h264
#ffmpeg -fflags +genpts -r 30 -i raw.h264 -c:v copy output.mp4
