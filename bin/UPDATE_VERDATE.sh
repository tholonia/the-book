#!/bin/bash

cd /home/jw/sites/the-book
echo `head -1 version.txt` | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}' > vtmp
tail -n +2 version.txt >> vtmp

mv vtmp version.txt
git add version.txt

V=`head -1 version.txt`

DR=`date +%c`

DRV="${DR} v.${V}"

#update vesion date in MD file
perl -pi -e 's/\{!.*\}/\{\!$ENV{'DRV'}$2\}/' README.md
perl -pi -e 's/\{!.*\}/\{\!$ENV{'DRV'}$2\}/' Latest/THOLONIA_THE_BOOK.md

#update vesion date _layouts/default.html
perl -pi -e 's/current version:.*/current version: $ENV{'DRV'}/' /home/jw/sites/the-book/docs/_layouts/default.html




