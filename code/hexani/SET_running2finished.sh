#!/bin/bash

if [ $# -eq 0 ]; then
    echo "$0 <path_to_dat_file>"
    echo "   ex: $0 CACTUS_08/build.dat.sh"
    exit 1
fi


perl -pi -e 's/status=running/status=finished/gmi' ${1}
