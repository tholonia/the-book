#!/usr/bin/bash

D=`date +%h-%d-%Y_%H:%m`
DS=`date +%H:%m:%S`
DR=`date +%c`
export DR
NAME="THOLONIA_THE_BOOK"
SRC="Latest/THOLONIA_THE_BOOK.md"

usage() {
	echo "usage:"
	echo "./MAKE <option>"
	
	echo "Options are:"
	echo "  EPUB	Create EPUB v2.0 file"
	echo "  HTML	Create HTML5 file"
	echo "  PDF	Create PDF"
	echo "  TEX	Create LaTex file"
}

make_epub() {
	TYPE="epub"
	BOOK=${NAME}.${TYPE}
#	CMD="pandoc --toc --standalone -H include.tex --top-level-division=chapter --to=${TYPE} -o ${BOOK} "
	CMD="pandoc --standalone -H include.tex --top-level-division=chapter --to=${TYPE} -o ${BOOK} "
	${CMD} ${SRC}
	exit;
}
 
make_html5() {
	TYPE="html"
	BOOK=${NAME}.${TYPE}
	CMD="pandoc --metadata pagetitle="..." --toc --standalone -H include.tex --top-level-division=chapter --to=${TYPE} -o ${BOOK} "
	${CMD} ${SRC}
	exit;
}

make_pdf() {
	TYPE="pdf"
	BOOK=${NAME}.${TYPE}
 	CMD="pandoc --toc --standalone -H include.tex --pdf-engine=xelatex --top-level-division=chapter -o ${BOOK} "
	${CMD} ${SRC}
	exit;
}

make_tex() {
	TYPE="tex"
	BOOK=${NAME}.${TYPE}
	CMD="pandoc --toc --standalone -H include.tex --pdf-engine=xelatex --top-level-division=chapter --to=latex -o ${BOOK} "
	${CMD} ${SRC}
	exit;
}


if [ "$#" == "0" ] ; then
	usage;
	exit;	
fi

if [ "$1" == "PDF" ] ; then
        make_pdf
fi

if [ "$1" == "TEX" ] ; then
        make_tex
fi

if [ "$1" == "EPUB" ] ; then
        make_epub
fi

if [ "$1" == "HTML" ] ; then
        make_html5
fi


echo "'${1}' is not a valid option"
usage;


