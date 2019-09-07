The markdown used for this book is not fully compatible with the Github flavor of markdown.  This book was assembled with Typora (https://typora.io/), and, as you will see if you look at the markdown directly on Github, there are some formatting options that do not display correctly.  The Github flavor of markdown is far too restrictive for this book.  If you are going to submit changes, you may want to use Typora.

Any custom formatting is contained in the CSS file `github.user.css.`  If you are using Typora, this file should be copied to `~/.config/Typora/themes/` (on Linux), and requires that you use Typora's the built-in Github theme.



There is a `MAKE` script to produce a PDF (and other formats) from the MD files.  Fot this I needed (on Manjaro/Arch Linux) the following packages: `pandoc`, `pdflatex`,`textlive-most`, `texlive-latexextra`.  I also installed (but may not have been necessary) `texlive-fontsextra`, `culmus`, `polyglossia`,`texlive-most`, `texlive-langextra`, `texlive-langcyrillic`, `texlive-langgreek`.  However, the outputs are not perfect at best, or fail, at worse.  

In my case I referred to the Arch Linux page on TeX_Live  at https://wiki.archlinux.org/index.php/TeX_Live

The commands used to produce various output formats are detailed in the MAKE file.

**The best way to output to other formats is with the export option of Typora.**

```
?> ./MAKE MD
?> typora THOLONIA_THE_BOOK.md

(File->Export->PDF)

```

Only changes to the chapters will be recorded.  The final **THOLONIA_THE_BOOK.md** is generated from the chapters (using `./MAKE MD`, or simply catting all the files together in the correct order (see `MAKE` file)), so any changes made to that file are destroyed when regenerated.

Any questions can be sent to duncan.stroud@gmail.com

