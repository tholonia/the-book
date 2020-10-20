The markdown used for this book is not fully compatible with the Github flavor of markdown.  This book was assembled with Typora (https://typora.io/), and, as you will see if you look at the markdown pages directly on Github, there are some formatting options that do not display correctly.    If you are going to make edits, you'll probably need Typora.

If you want to create the PDF, ePub, and HTML output from the markdown, you''' need 



One way to create an EPUB version of the books requires `typora` and `sigil` (https://github.com/Sigil-Ebook/Sigil/releases) .  Unfortunately the Typora export of ePub or PDF seems to not be working too well. 

> 1) Open `THELONIA_THE_BOOK.md` in `typora` and then `File->Export->HTML`.

> 2) Open `THELONIA_THE_BOOK.html` in `sigil` then save as EPUB.  You won't need to import any images because ```sigil``` expects the images to be in ```../Images```, which they are.

Another way is to use the shell script (if you are running Linux) ```./bin/PUB ```.  ```cd``` to the ```./bin``` folder and run ```./PUB -X```  (or ```-?``` to see the options available).  

Any questions can be sent to duncan.stroud@gmail.com

_Notes:_

- Any custom formatting is contained in the CSS file `./Styles/THOLONIA_THE_BOOK.css.`  If you are using Typora, this file should be copied  or symlinked  to `~/.config/Typora/themes/git.user.base.css` (on Linux), and requires that you use Typora's the built-in Github theme.
- I tried various PDF formatters, such as ```pandoc```, ```wkhtmltopdf```, and a few others.  They all failed to produce the correct output for one reason or another.  The only one that worked properly was PrinceXML's ```prince-book``` (freeware, not opensouce, and leaves a small logo on the upper right corner of the first page).  You can see all the commands in the ```./bin/PUB``` script.  If you can't tolerate the small logo, then use ```wkhtmltopdf```, but make sure you don't have more that 99 footnotes, as ```wkhtmltopdf``` only prints the two digit footnotes.
- The template that controls the title page for each format is located in ```./Styles/default.*```
- Use 6.69in x 9.61in (16.99cm x 24.4cm) book size.
- In Typora, curly brackets, ellipses, and just about anything that is not specifically alphanumeric needs to be represented with HTML codes, such as ```&rdquo; &ldquo; &rsquo; &lsquo; &pi; &hellips; &times; ```, etc., because sometimes Typora gets confused and rewrites these characters if you type them in directly.
- I had a few Greek, Hebrew and Chinese characters in the text which Typora had no problem supporting.  However, they did not appear in the PDF.  They did appear in the HTML, but when uploaded to Kindle they generated errors.  Ultimately I had to use only HTML entities for some of the Greek characters and abandon the Hebrew and Chinese.
- Sadly, I never found a way to have larger gutter margins for the book.  I could only adjust margins in general.  This was surprising as prince-books is specifically made for making books.   To their credit, they claim to support the CSS attribute ".margin-inside", but I could not get that to do anything and apparently nor could anyone else as it failed in conversions.  Typora was especially useful in tweaking the CSS as it is essentially a version of Chromium so it comes with the developer tools (which occasionally crashes).
- All the larger images (those not in sentences, for example) are their own paragraphs, centered and full width.  Sizing images and floating left or right created huge problems when trying to maintain consistency and readability across various formats. I am sure there is a way to do that, but I could not get it to work, mainly due to Typora's limitation of not allowing ```class``` or ```id``` in the tags.

