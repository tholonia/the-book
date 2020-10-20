import os
import array as arr

limit_fr = 0
limit_to = 100

chapters_prod = [
    '00-Intro',
    '01-CHAOS',
    '02-ENERGY',
    '03-ORDER',
    '04-THE_LAWS',
    '05-REASON',
    '06-INFORMATION',
    '07-STRUCTURE',
    '08-MIND',
    '09-FIELDS',
    '10-RELEVANT_EXAMPLES',
    '11-PREDETERMINISM',
    '12-THE_NEW_MYTHOLOGY',
    '13-PART-II',
    '14-WAY_OF_CHANGE',
    '19-APPENDIX',
    '20-How_to_Make_Structured_Water',
    '21-Tholonic_Math',
    '22-An_Unexpected_Pattern',
    '23-New_Data',
    '24-Meaning_of_Squares_and_Square_Roots',
    '25-Greek_Gods',
    '26-Hidden_Images',
    '27-The_Tholonic_I-Ching',
    '28-About_This_Book'
]
# '40-References'

chapters_test = [
    '00-Intro',
    '01-CHAOS'
]

chapters_all = [
    'all'
]

chapters = chapters_prod
# chapters = chapters_test
# chapters = chapters_all

H = "/home/jw/books/tholonia"
S = "Latest"


def concat():

    # CX=f"{H}/bin/DELIMG.sh '{H}/chapters/*.pdf' "
    # print(CX)
    # os.system(CX)

    clist = ""
    for c in chapters:
        clist += f"{H}/chapters/{c}.pdf "
    # cmd = f"pdftk {clist} cat output {H}/{S}/THOLONIA_THE_BOOK.pdf"
    cmd = f"pdftk {clist} cat output {H}/chapters/THOLONIA_THE_BOOK.pdf"
    print(cmd)
    os.system(cmd)

    # CX=f"{H}/bin/DELIMG.sh '{H}/chapters/THOLONIA_THE_BOOK.pdf' "
    # print(CX)
    # os.system(CX)


def delpage():
    blank = arr.array = [1, 5, 11, 16, 24, 50, 82, 97, 197, 209, 248, 262, 280, 288, 292, 297, 302, 321, 328, 334, 340, 344, 420, 421]

    pre = "pdftk ~/books/tholonia/chapters/THOLONIA_THE_BOOK.pdf cat"
    pages = ""
    final = "output x.pdf"
    for i in range(len(blank) - 1):
        fr = blank[i] + 1
        to = blank[i + 1] - 1
        pages += f"{fr}-{to} "

    pages = pages.replace("-426", "-end")
    cmd = f"{pre} {pages} {final}"
    print(cmd)
    os.system(cmd)

