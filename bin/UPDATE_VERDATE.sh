#!/bin/bash

H=/home/jw/sites/the-book

echo `head -1 ${H}/version.txt` | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}' > ${H}/vtmp
tail -n +2 ${H}/version.txt >> ${H}/vtmp

mv ${H}/vtmp ${H}/version.txt
git add ${H}/version.txt

V=`head -1 ${H}/version.txt`
DR=`date +%c`
DRV="${DR} v.${V}"
export DRV #export needed fpr perl script

#update vesion date in MD file
perl -pi -e 's/\{!.*\}/\{\!$ENV{'DRV'}$2\}/' ${H}/README.md
#perl -pi -e 's/\{!.*\}/\{\!$ENV{'DRV'}$2\}/' ${H}/Latest/THOLONIA_THE_BOOK.md
perl -pi -e 's/^(.*VERSION: ).*(.)$/$1$ENV{'DRV'}\x27/' ${H}/metadata.yaml

#update vesion date _layouts/default.html
perl -pi -e 's/current version:.*/current version: $ENV{'DRV'}/' ${H}/docs/_layouts/default.html


#relink MD file

rm ${H}/Latest/THOLONIA_THE_BOOK_*.md>>${H}/log 2>&1
ln -fs ${H}/Latest/THOLONIA_THE_BOOK.md ${H}/Latest/THOLONIA_THE_BOOK_${V}.md

