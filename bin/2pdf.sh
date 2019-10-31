
wkhtmltopdf \
--header-html file:///home/jw/sites/the-book/header.html \
--footer-html file:///home/jw/sites/the-book/footer.html \
--page-height 244mm \
--page-width 170mm \
--margin-left .375in \
--margin-right .375in \
--margin-bottom .5in \
--margin-top .5in \
--load-error-handling ignore \
--javascript-delay 3333 \
~/sites/the-book/Latest/THOLONIA_THE_BOOK.html \
~/sites/the-book/Latest/THOLONIA_THE_BOOK.pdf

wkhtmltopdf \
--header-html file:///home/jw/sites/the-book/header.html \
--footer-html file:///home/jw/sites/the-book/footer.html \
--page-height 244mm \
--page-width 170mm \
--margin-left .375in \
--margin-right .375in \
--margin-bottom .5in \
--margin-top .5in \
--load-error-handling ignore \
--javascript-delay 3333 \
--user-style-sheet file:///home/jw/sites/the-book/print-only.css \
~/sites/the-book/Latest/THOLONIA_THE_BOOK.html \
~/sites/the-book/Latest/THOLONIA_THE_BOOK_print-only.pdf



