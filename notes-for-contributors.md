The markdown used for this book is not fully compatible with the Github flavor of markdown.  This book was assembled with Typora (https://typora.io/), and, as you will see if you look at the markdown pages directly on Github, there are some formatting options that do not display correctly.  The Github flavor of markdown is far too restrictive for this book.  If you are going to submit changes, you may want to use Typora.

One way to create an EPUB version of the books requires `typora` and `sigil` (https://github.com/Sigil-Ebook/Sigil/releases) 

>  0) [optional] Run ./UPDATE_VERDATE.sh to update the DRAFT date in the documents to the current time.

> 1) Open `THELONIA_THE_BOOK.md` in `typora` and then `File->Export->HTML`.

>  2) Open `THELONIA_THE_BOOK.html` in `sigil` then save as EPUB.

Any questions can be sent to duncan.stroud@gmail.com

_Notes:_

- Endnotes are support in the following manner (until we come up with a better way):

  Reference numbers (in the text) are input as: ```<sup>[1](#ref_001)</sup>```

  References (at the bottom) are input as : ```<a name="ref_001">1</a>:  reference info here```

  To add a return link to the reference that brings you back to the text,:

  In text:   ```<sup>[143](#ref_143)</sup><a name="rev_143">&nbsp;</a>```
  
  In references: ```<a name="ref_143">143</a> [(src)](#rev_143):```
  
  Unfortunately, you have to manually enter the next ref number, and currently there is not way to reorder them consecutively.

- Any custom formatting is contained in the CSS file `github.user.css.`  If you are using Typora, this file should be copied to `~/.config/Typora/themes/` (on Linux), and requires that you use Typora's the built-in Github theme.

- The `include.txt` file is only relevant if you plan to convert to LaTex format.

- Arch Linux/TeX_Live at https://wiki.archlinux.org/index.php/TeX_Live


This was the original MAKE file that created various formats
```
#!/usr/bin/bash

D=`date +%h-%d-%Y_%H:%m`
DS=`date +%H:%m:%S`
DR=`date +%c`
export DR
DCHAP="Chapters/"
DLAST="Latest/"
ORDER="	README.md ${DCHAP}000-INTRO.md ${DCHAP}010-TOC.md ${DCHAP}020-CHAOS.md ${DCHAP}030-ENERGY.md ${DCHAP}040-ORDER.md ${DCHAP}050-LAWS.md ${DCHAP}060-INFORMATION.md ${DCHAP}070-REASON.md ${DCHAP}080-STRUCTURE.md ${DCHAP}090-CASES.md ${DCHAP}100-PREDETER.md ${DCHAP}110-UNBOUND.md ${DCHAP}120-XA-WATER.md ${DCHAP}130-XB-TMATH.md ${DCHAP}140-REFS.md"
 

NORMAL=`echo -e '\033[0m'`
RED=`echo -e '\033[31m'`
GREEN=`echo -e '\033[0;32m'`
LGREEN=`echo -e '\033[1;32m'`
BLUE=`echo -e '\033[0;34m'`
LBLUE=`echo -e '\033[1;34m'`
YELLOW=`echo -e '\033[0;33m'`

# This makes one large markdown file, but there is really no reason to use this as the edits are made in the chapters.
# this does not generate a time stamp



make_md() {
	TYPE="md"
	echo "${YELLOW}MAKING >>> ${TYPE}${NORMAL}"
	#create a versioned filename
	BOOK="versions/THOLONIA_THE_BOOK_${DS}.${TYPE}"
	echo "${GREEN}OUTPUT >>> ${BOOK}${NORMAL}"
	
	CMD="cat "
        
	echo "${BLUE}CMD >>> ${CMD}${NORMAL}"

	echo -n ${RED}	
	#replace datestamp with new datestamp in README.md
	perl -pi -e 's/\{!.*\}/\{\!$ENV{'DR'}$2\}/' README.md
	
	echo "${LGREEN}${CMD} ${ORDER} > ${BOOK}${NORMAL}"

	${CMD} ${ORDER} > ${BOOK}
	# copy versioned filename to final name	
	rm ${DLAST}THOLONIA_THE_BOOK.${TYPE}
#	perl -pi -e 's/media/file:\/\/\/home\/jw\/Documents\/Projects\/mindfields\/tholonia-md\/media/gmi' ${BOOK} 
	cp ${BOOK} ${DLAST}THOLONIA_THE_BOOK.${TYPE}
	echo -n ${NORMAL}	
	echo "=============================================================="
}

make_epub() {
	TYPE="epub"
	echo "${YELLOW}MAKING >>> ${TYPE}${NORMAL}"
	#create a versioned filename
	BOOK="versions/THOLONIA_THE_BOOK_${DS}.epub"
	echo "${GREEN}OUTPUT >>> ${BOOK}${NORMAL}"
	
#	CMD="pandoc --toc --standalone -H include.tex --top-level-division=chapter --to=${TYPE} -o ${BOOK} "
	CMD="pandoc --standalone -H include.tex --top-level-division=chapter --to=${TYPE} -o ${BOOK} "
        
	echo "${BLUE}CMD >>> ${CMD}${NORMAL}"
	
	echo -n ${RED}	
	#replace datestamp with new datestamp in README.md
	perl -pi -e 's/\{!.*\}/\{\!$ENV{'DR'}$2\}/' README.md
	
	echo "${LGREEN}${CMD} ${ORDER}${NORMAL}"
	${CMD} ${ORDER}
	
	# copy versioned filename to final name	
	rm ${DLAST}THOLONIA_THE_BOOK.${TYPE} 
	cp ${BOOK} ${DLAST}THOLONIA_THE_BOOK.${TYPE} 
	echo -n ${NORMAL}	
	echo "=============================================================="
}

make_html5() {
	TYPE="html"
	echo "${YELLOW}MAKING >>> ${TYPE}${NORMAL}"
	#create a versioned filename
	BOOK="versions/THOLONIA_THE_BOOK_${DS}.${TYPE}"
	echo "${GREEN}OUTPUT >>> ${BOOK}${NORMAL}"
	
	CMD="pandoc --metadata pagetitle="..." --toc --standalone -H include.tex --top-level-division=chapter --to=${TYPE} -o ${BOOK} "
        
	echo ${RED}	
	echo "${BLUE}CMD >>> ${CMD}${NORMAL}"
	
	echo -n ${RED}	
	#replace datestamp with new datestamp in README.md
	perl -pi -e 's/\{!.*\}/\{\!$ENV{'DR'}$2\}/' README.md
	
	echo "${LGREEN}${CMD} ${ORDER}${NORMAL}"
	${CMD} ${ORDER}
	
	#fix broken links
	perl -pi -e 's/src=\"media/src=\"file:\/\/\/home\/jw\/Documents\/Projects\/mindfields\/tholonia-md\/media/gmi' ${BOOK} 
	# copy versioned filename to final name	
	rm ${DLAST}THOLONIA_THE_BOOK.${TYPE} 
	cp ${BOOK} ${DLAST}THOLONIA_THE_BOOK.${TYPE} 
	echo -n ${NORMAL}	
	echo "=============================================================="
}

make_pdf() {
	TYPE="pdf"
	echo "${YELLOW}MAKING >>> ${TYPE}${NORMAL}"
	#create a versioned filename
	BOOK="versions/THOLONIA_THE_BOOK_${DS}.${TYPE}"
	echo "${GREEN}OUTPUT >>> ${BOOK}${NORMAL}"
	
	CMD="pandoc --toc --standalone -H include.tex --pdf-engine=xelatex --top-level-division=chapter -o ${BOOK} "
        
	echo "${BLUE}CMD >>> ${CMD}${NORMAL}"

	echo -n ${RED}	
	#replace datestamp with new datestamp in README.md
	perl -pi -e 's/\{!.*\}/\{\!$ENV{'DR'}$2\}/' README.md
	
	echo "${LGREEN}${CMD} ${ORDER}${NORMAL}"

	${CMD} ${ORDER}
	
	# copy versioned filename to final name	
	rm ${DLAST}THOLONIA_THE_BOOK.${TYPE}
	cp ${BOOK} ${DLAST}THOLONIA_THE_BOOK.${TYPE}
	echo -n ${NORMAL}	
	echo "=============================================================="
}

make_tex() {
	TYPE="tex"
	echo "${YELLOW}MAKING >>> ${TYPE}${NORMAL}"
	#create a versioned filename
	BOOK="versions/THOLONIA_THE_BOOK_${DS}.${TYPE}"
	echo "${GREEN}OUTPUT >>> ${BOOK}${NORMAL}"
	
#	CMD="pandoc --toc --standalone -V lang:he -H include.tex --pdf-engine=xelatex --top-level-division=chapter -o ${BOOK}"
	CMD="pandoc --toc --standalone -H include.tex --pdf-engine=xelatex --top-level-division=chapter --to=latex -o ${BOOK} "
        
	echo "${BLUE}CMD >>> ${CMD}${NORMAL}"
	
	echo -n ${RED}	
	#replace datestamp with new datestamp in README.md
	perl -pi -e 's/\{!.*\}/\{\!$ENV{'DR'}$2\}/' README.md
	
	echo "${LGREEN}${CMD} ${ORDER}${NORMAL}"
	${CMD} ${ORDER}
	
	# copy versioned filename to final name	
	rm ${DLAST}THOLONIA_THE_BOOK.${TYPE}
	cp ${BOOK} ${DLAST}THOLONIA_THE_BOOK.${TYPE}
	echo -n ${NORMAL}	
	echo "=============================================================="

}


if [ "$#" == "0" ] ; then
	echo "You need to decale MD, EPUB, HTML  (not working PDF, TEX)"
fi

if [ "$1" == "PDF" ] ; then
        make_pdf
fi

if [ "$1" == "TEX" ] ; then
        make_tex
fi

if [ "$1" == "MD" ] ; then
        make_md
fi

if [ "$1" == "EPUB" ] ; then
        make_epub
fi

if [ "$1" == "HTML" ] ; then
        make_html5
fi

if [ "$1" == "ALL" ] ; then
	make_md  	# OK
	# the following do not really work well
	make_epub  	# OK, but missing CSS
	make_html5 	# OK, but missing CSS
	make_pdf 	# no HTML images, must use pandoc format
	make_tex   	# lots of errors when tryiong to compile with luatex, xetex, latex, pdflatex!!
fi

```