#!/bin/bash

H=/home/jw/books/tholonia

echo `head -1 ${H}/inc/version.txt` | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}' > ${H}/inc/vtmp
tail -n +2 ${H}/inc/version.txt >> ${H}/inc/vtmp

mv ${H}/inc/vtmp ${H}/inc/version.txt
git add ${H}/inc/version.txt

V=`head -1 ${H}/inc/version.txt`
DR=`date +%c`
DRV="${DR} v.${V}"
VV="v.${V}"
export DRV #export needed fpr perl script
export VV
#update vesion date in MD file
perl -pi -e 's/\{!.*\}/\{\!$ENV{'DRV'}$2\}/' ${H}/README.md
#perl -pi -e 's/\{!.*\}/\{\!$ENV{'DRV'}$2\}/' ${H}/inc/Latest/THOLONIA_THE_BOOK.md

#update vesion in metadata fpor pandoc
#perl -pi -e 's/^(.*VERSION: ).*(.)$/$1$ENV{'DRV'}\x27/' ${H}/inc/metadata.yaml

#update vesion date _layouts/default.html
perl -pi -e 's/current version:.*/current version: $ENV{'DRV'}/' ${H}/docs/_layouts/default.html

#update vesion in PUB make_pdf() function
perl -pi -e 's/--pdf-title=\"THOLONIA .*$/--pdf-title=\"THOLONIA $ENV{'VV'}\" \\/' ${H}/bin/PUB

#update vesion in PUB make_pdf() function
perl -pi -e 's/version:.*/version:  $ENV{'VV'}/'  ${H}/inc/metadata.yaml

#relink MD file

rm ${H}/Latest/THOLONIA_THE_BOOK_*.md>>${H}/log 2>&1
ln -fs ${H}/Latest/THOLONIA_THE_BOOK.md ${H}/Latest/THOLONIA_THE_BOOK_${V}.md
