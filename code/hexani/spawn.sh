uxterm -e "$1 > $1.log &; bash -c 'tail -f $1.log'" &   