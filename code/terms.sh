nohup ./runall.sh
mv nohup.out x
perl -pi -e 's/\[/\n~/gmi' x
perl -pi -e 's/\]/\n/gmi' x
grep \~ x|sort -u |perl -p -e 's/\~//gmi' > out

grep -v "DEPARTING 0" out > x; mv x out
grep -v "DEPLOYING 1" out > x; mv x out
grep -v "EMERGING 0" out > x; mv x out
grep -v "INCEPTION 1" out > x; mv x out
grep -v "SPECIFICATION 0" out > x; mv x out
grep -v "SYNTHESIZING 1" out > x; mv x out

mv out terms.txt
