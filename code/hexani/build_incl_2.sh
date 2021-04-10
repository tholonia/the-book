
Xcmd="/usr/bin/xvfb-run -w 3 -d -a -e ${ROOT}/${name}_${series}/Xerrors.txt"

${ROOT}/_${name}_${series}_HB_descriptor.py ${a01} ${a02} ${a03} ${a04} ${a05} ${a06} ${a07} ${a08} ${a09} ${a10} ${a11} ${a12} ${a13} ${a14} ${a15} ${a16} ${a17} ${a18} ${a19} ${a20}

if [[ ! -f "${ROOT}/DESCRIPTOR_ONLY" ]]
then
    ${Xcmd} ${ROOT}/_${name}_${series}_HB_frames.py ${a01} ${a02} ${a03} ${a04} ${a05} ${a06} ${a07} ${a08} ${a09} ${a10} ${a11} ${a12} ${a13} ${a14} ${a15} ${a16} ${a17} ${a18} ${a19} ${a20}
    ${ROOT}/_${name}_${series}_RUN_GIF.sh ${name} ${series} ${delay} ${psn}
fi

rm ${ROOT}/_${name}_${series}_hex_builder_lapse.py > /dev/null 2>&1
rm ${ROOT}/_${name}_${series}_RUN_GIF.sh > /dev/null 2>&1
rm ${ROOT}/_${name}_${series}_HB_frames.py > /dev/null 2>&1
rm ${ROOT}/_${name}_${series}_HB_descriptor.py > /dev/null 2>&1

if [[ ! -f "${ROOT}/DESCRIPTOR_ONLY" ]]
then
    cp ${WD}/gif/cropped/${name}* ${WD}/prev > /dev/null 2>&1
    ${ROOT}/SET_running2finished.sh ${WD}/build.dat.sh
fi

