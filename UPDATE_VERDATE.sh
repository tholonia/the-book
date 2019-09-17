#!/bin/bash
DR=`date +%c`
export DR
#update vesion date in MD file
perl -pi -e 's/\{!.*\}/\{\!$ENV{'DR'}$2\}/' README.md
perl -pi -e 's/\{!.*\}/\{\!$ENV{'DR'}$2\}/' Latest/THOLONIA_THE_BOOK.md
