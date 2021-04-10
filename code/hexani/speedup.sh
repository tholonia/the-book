#!/bin/bash -x

#-----------------------------------
#declare -a colors=("#f3160c" "#f39f0c","#dcf30c","#56f30c","#oce6f3","#0c56f3,","#e145fe")
colors=("f3160c" "f39f0c" "dcf30c" "56f30c" "0ce6f3" "0c56f3" "e145fe")
FLOOR=0;
CEILING=6;
RANGE=$(($CEILING-$FLOOR+1));
RESULT=$RANDOM;
let "RESULT %= $RANGE";
RESULT=$(($RESULT+$FLOOR));
COLOR=${colors[$RESULT]}
#C0=${colors[0]}
#C1=${colors[1]}
#C2=${colors[2]}
#echo "result: $RESULT, C0=$C0 C1=$C1 C2=$C2"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo ${COLOR}
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

#------------------------------------

NAME=$1 #"CACTUS"
SERIES=$2 #"09"
PSN=$3

#SLOW1=${NAME}_series-${SERIES}_image-1.mp4
#SLOW2=${NAME}_series-${SERIES}_image-2.mp4
#
#FAST1=${NAME}_series-${SERIES}_image-1_FAST.mov
#FAST2=${NAME}_series-${SERIES}_image-2_FAST.mov


SLOW1=${NAME}_series-${SERIES}_image-1
SLOW2=${NAME}_series-${SERIES}_image-2

FAST1=${NAME}_series-${SERIES}_image-1_FAST
FAST2=${NAME}_series-${SERIES}_image-2_FAST

cp ../gif/cropped/${SLOW1}.mp4 ./
cp ../gif/cropped/${SLOW2}.mp4 ./

SP=10

cd ${NAME}_${SERIES}/prev

#With re-encoding:
#ffmpeg -y -i ${IN}.mp4 -vf "setpts=1.25*PTS" -r 24 tmp.h264
#ffmpeg -y -r ${SP} -i tmp.h264 -c copy re_${OUT}.mov

#Without re-encoding:
rm *.mov > /dev/null 2>&1
rm tmp*.jpg > /dev/null 2>&1

ffmpeg -y -i ${SLOW1}.mp4 -c copy -f h264 tmp.h264
ffmpeg -y -r ${SP} -i tmp.h264 -c copy ${FAST1}.mov
rm ${FAST1}.mov
ffmpeg -y -i ${SLOW2}.mp4 -c copy -f h264 tmp.h264
ffmpeg -y -r ${SP} -i tmp.h264 -c copy ${FAST2}.mov
rm ${FAST2}.mov


convert ../gif/cropped/hex-072.gif  ./thumbnail_SLOW_1.jpg
cp thumbnail_SLOW_1.jpg thumbnail_FAST_1.jpg

mplayer -vo jpeg -ss 00:03:00 -frames 1 ${SLOW2}.mp4
mv 00000001.jpg thumbnail_SLOW_2.jpg
cp thumbnail_SLOW_2.jpg thumbnail_FAST_2.jpg

rm tmp.jpg tmp1.jpg tmp2.jpg > /dev/null 2>&1

F="thumbnail_SLOW_1.jpg"
convert ${F} -gravity North  -pointsize 300 -fill Yellow -font Times-Bold -annotate 0 'NORMAL SPEED' tmp.jpg
convert tmp.jpg -gravity North  -pointsize 250 -fill cyan -font Helvetica-Bold -annotate 0 "\n${NAME} ${SERIES} - individual" tmp1.jpg
convert tmp1.jpg -resize 1280x tmp2.jpg
convert tmp2.jpg -size 1280x720 -resize 60% xc:black +swap -gravity center  -composite tmp3.jpg
convert tmp3.jpg  -bordercolor "#${COLOR}" -border 16 -pointsize 125 -fill white -font Times-Bold -gravity southwest -draw "text 35,10 '${PSN}'"  ${F}

F="thumbnail_FAST_1.jpg"
convert ${F} -gravity North  -pointsize 300 -fill Orange -font Times-Bold -annotate 0 'FAST 10x SPEED' tmp.jpg
convert tmp.jpg -gravity North  -pointsize 250 -fill cyan -font Helvetica-Bold -annotate 0 "\n${NAME} ${SERIES} - individual" tmp1.jpg
convert tmp1.jpg -resize 1280x tmp2.jpg
convert tmp2.jpg -size 1280x720 -resize 60% xc:black +swap -gravity center  -composite tmp3.jpg
convert tmp3.jpg  -bordercolor "#${COLOR}" -border 16 -pointsize 125 -fill white -font Times-Bold -gravity southwest -draw "text 35,10 '${PSN}'"  ${F}

F="thumbnail_SLOW_2.jpg"
convert ${F} -gravity North  -pointsize 300 -fill Yellow -font Times-Bold -annotate 0 'NORMAL SPEED' tmp.jpg
convert tmp.jpg -gravity North  -pointsize 250 -fill cyan -font Helvetica-Bold -annotate 0 "\n${NAME} ${SERIES} - composite" tmp1.jpg
convert tmp1.jpg -resize 1280x tmp2.jpg
convert tmp2.jpg -size 1280x720 -resize 60% xc:black +swap -gravity center  -composite tmp3.jpg
convert tmp3.jpg  -bordercolor "#${COLOR}" -border 16 -pointsize 125 -fill white -font Times-Bold -gravity southwest -draw "text 35,10 '${PSN}'"  ${F}

F="thumbnail_FAST_2.jpg"
convert ${F} -gravity North  -pointsize 300 -fill Orange -font Times-Bold -annotate 0 'FAST 10x SPEED' tmp.jpg
convert tmp.jpg -gravity North  -pointsize 250 -fill cyan -font Helvetica-Bold -annotate 0 "\n${NAME} ${SERIES} - composite" tmp1.jpg
convert tmp1.jpg -resize 1280x tmp2.jpg
convert tmp2.jpg -size 1280x720 -resize 60% xc:black +swap -gravity center  -composite tmp3.jpg
convert tmp3.jpg  -bordercolor "#${COLOR}" -border 16 -pointsize 125 -fill white -font Times-Bold -gravity southwest -draw "text 35,10 '${PSN}'"  ${F}

rm ./tmp.mp4  > /dev/null 2>&1

HandBrakeCLI -i ./${SLOW1}}.mp4 -o ./tmp.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O
mv ./tmp.mp4 ./${SLOW1}.mp4

HandBrakeCLI -i ./${SLOW2}}.mp4 -o ./tmp.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O
mv ./tmp.mp4 ./${SLOW2}.mp4

HandBrakeCLI -i ./${FAST1}.mov -o ./tmp.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O
mv ./tmp.mp4 ./${FAST1}.mp4

HandBrakeCLI -i ./${FAST2}.mov -o ./tmp.mp4 -e x264 -q 28 -r 15 -B 64 -X 1280 -O
mv ./tmp.mp4 ./${FAST2}.mp4


rm *.gif > /dev/null 2>&1
rm tmp*.jpg > /dev/null 2>&1
rm *.h264 > /dev/null 2>&1
