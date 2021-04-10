
ROOT="/home/jw/books/tholonia/code/hexani"
WD="${ROOT}/${name}_${series}"

if [[ ! -f "${ROOT}/DESCRIPTOR_ONLY" ]]
then
    ${ROOT}/SET_pending2running.sh ${WD}/build.dat.sh
    rm -rf ${WD}/gif > /dev/null 2>&1
    rm -rf ${WD}/ORG > /dev/null 2>&1
    mkdir ${WD} > /dev/null 2>&1
    mkdir ${WD}/ORG > /dev/null 2>&1
    mkdir ${WD}/ORG/details > /dev/null 2>&1
    mkdir ${WD}/prev > /dev/null 2>&1
    cp ${ROOT}/hex_builder_lapse.py ${ROOT}/_${name}_${series}_hex_builder_lapse.py
    cp ${ROOT}/RUN_GIF.sh ${ROOT}/_${name}_${series}_RUN_GIF.sh
    cp ${ROOT}/HB_frames.py ${ROOT}/_${name}_${series}_HB_frames.py
fi

# to only build descriptors, "touch DESCRIPTOR_ONLY"
cp ${ROOT}/HB_descriptor.py ${ROOT}/_${name}_${series}_HB_descriptor.py

