The markdown used for this book is not fully compatible with the Github flavor of markdown.  This book was assembled with Typora (https://typora.io/), and, as you will see if you look at the markdown pages directly on Github, there are some formatting options that do not display correctly.  The Github flavor of markdown is far too restrictive for this book.  If you are going to submit changes, you may want to use Typora.

One way to create an EPUB version of the books requires `typora` and `sigil` (https://github.com/Sigil-Ebook/Sigil/releases) 

> 0) [optional] Run ./UPDATE_VERDATE.sh to update the DRAFT date in the documents to the current time.

> 1) Open `THELONIA_THE_BOOK.md` in `typora` and then `File->Export->HTML`.

> 2) Open `THELONIA_THE_BOOK.html` in `sigil` then save as EPUB.

Any questions can be sent to duncan.stroud@gmail.com

_Notes:_

- Endnotes are support in the following manner (until we come up with a better way):

  Reference numbers (in the text) are input as: ```<sup>[1](#ref_001)</sup>```

  References (at the bottom) are input as : ```<a name="ref_001">1</a>:  reference info here```

  To add a return link to the reference that brings you back to the text,:

  In text:   ```<sup>[143](#ref_143)</sup><a name="rev_143">&nbsp;</a>```
  
  In references: ```<a name="ref_143">143</a> [(src)](#rev_143):```
  
  Unfortunately, you have to manually enter the next ref number, and currently there is no way to reorder them consecutively.

- Any custom formatting is contained in the CSS file `github.user.css.`  If you are using Typora, this file should be copied to `~/.config/Typora/themes/` (on Linux), and requires that you use Typora's the built-in Github theme.

- The `include.txt` file is only relevant if you plan to convert to LaTex format.

- Arch Linux/TeX_Live at https://wiki.archlinux.org/index.php/TeX_Live


## Technical Notes

### This is the contents of include.tex which is needed to pandoc convserions
```
%\setmainfont{Bitstream Vera Serif}
%\newfontfamily{\hebrewfont}{Noto Serif Hebrew}

\usepackage{fontspec}
\setmainfont{FreeSerif}
\setsansfont{FreeSans}
\setmonofont{FreeMono}
 
\usepackage{polyglossia}
\setdefaultlanguage{english}
\setotherlanguages{english,hebrew,greek}

```
The pandoc command (which ultimately did not make acceptable outputs) are:

ePub: pandoc --standalone -H include.tex --top-level-division=chapter --to=epub -o output.epub THOLONIA_THE_BOOK.md
HTML5: pandoc --metadata pagetitle="..." --toc --standalone -H include.tex --top-level-division=chapter --to=html -o output.html THOLONIA_THE_BOOK.md
PDF: pandoc --toc --standalone -H include.tex --pdf-engine=xelatex --top-level-division=chapter -o output.pdf THOLONIA_THE_BOOK.md
Tex: pandoc --toc --standalone -H include.tex --pdf-engine=xelatex --top-level-division=chapter --to=latex -o output.tex THOLONIA_THE_BOOK.md

## To create a PDF version suitable for book publishing

Using 6.69 x 9.61 in (16.99 x 24.4 cm) book size.

The script bin/2pdf.sh converts to PDF book format nicely using wkhtmltopdf.  
For more on this see https://www.nickvahalik.com/blog/finally-html-pdf-workflow-works

