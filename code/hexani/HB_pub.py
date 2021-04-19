#!/bin/python

import os,sys,subprocess,datetime,time

DIR="tholonic_01"
series=1
D=f"/home/jw/books/tholonia/code/hexani/{DIR}"

def run(cmd):
    # print(f">>> {cmd}")
    os.system(cmd)
def rrun(cmd):
    # print(f">>> {cmd}")
    output = subprocess.getoutput(cmd)
    return(output)


run(f"rm -rf {D}/final  > /dev/null 2>&1")
run(f"mkdir  {D}/final  > /dev/null 2>&1")
run(f"mkdir  {D}/final/video  > /dev/null 2>&1")
run(f"mkdir  {D}/final/details  > /dev/null 2>&1")


total_issues=1

for issue_number in range(1,(total_issues+1)):
    number_of_images=4
    for image_number in range(1,(number_of_images+1)):
        print(f"PREPARING: cp {D}/gif/cropped/tholonic_series-{series}_image-{image_number}.gif for issue {issue_number} of {total_issues}")

        filename = f"{D}/final/details/authenticity-s1i{image_number}_{issue_number}_of_{total_issues}.txt"
        f = open(filename, "a+")

        t = datetime.datetime.fromtimestamp(time.time())
        ts = t.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)")

        f.write(f"This animated GIF is issue {issue_number} of {total_issues} issued in Series {series}.\n")
        f.write(f"This was created by Duncan Stroud and published {ts}.\n")
        f.write("I, Duncan Stroud, verify this animation as being original and authentic.\n")
        f.close()

        run(f"cp {D}/gif/cropped/*.mp4 {D}/final/video")

        SRC=f"{D}/gif/cropped/tholonic_series-{series}_image-{image_number}.gif"
        TGT=f"{D}/final/ISSUE_{issue_number}_of_{total_issues}_tholonic_series-{series}_image-{image_number}.gif"

        run(f"cp {SRC} {TGT}")

        DAT=f"Duncan Stroud, Series {series}, image {image_number} of {total_issues} published {ts}"
        TGT=f"{D}/final/ISSUE_{issue_number}_of_{total_issues}_tholonic_series-{series}_image-{image_number}.gif"

        run(f'exiftool -artist="{DAT}"  {TGT}  > /dev/null 2>&1')

        # tmp=rrun(f"sha256sum {D}/final/ISSUE_{issue_number}_of_{total_issues}_tholonic_series-{series}_image-{image_number}.gif")
        # A01 = tmp.split(" ")[0]
        A01="test"

        filename = f"{D}/final/details/authenticity_series-{series}_image-{image_number}_sigs.txt"
        f = open(filename, "a+")
        line = f"Tholonic Series {series} Image {image_number}, {issue_number} of {total_issues}: {A01}\n"
        f.write(line)
        f.close()

        ZIPOUTPUT=f"{D}/final/authenticity_s1i{image_number}_{issue_number}_of_{total_issues}.zip"
        TXT=f"{D}/final/details/authenticity-s1i{image_number}_{issue_number}_of_{total_issues}.txt"
        PNG=f"fingerprint.png"
        MP4=f"{D}/final/video/tholonic_series-{series}_image-{image_number}.mp4"
        GIF=f"{D}/final/ISSUE_{issue_number}_of_{total_issues}_tholonic_series-{series}_image-{image_number}.gif"

        run(f"zip -j -r {ZIPOUTPUT}  {TXT} {PNG} {GIF} {MP4} ") # > /dev/null 2>&1")

        GIFSRC=f"{D}/final/ISSUE_{issue_number}_of_{total_issues}_tholonic_series-{series}_image-{image_number}.gif"
        ZIPSRC=f"{D}/final/authenticity_s1i{image_number}_{issue_number}_of_{total_issues}.zip"
        ZIPGIFOUT=f"{D}/final/tholonic_series-{series}_image-{image_number}_{issue_number}_of_{total_issues}.zip.gif"

        run(f"cat {GIFSRC} {ZIPSRC} > {ZIPGIFOUT}")

        TXTS=f"{D}/final/details/authenticity-s1i{image_number}_{issue_number}_of_{total_issues}.txt"
        ZIPS=f"{D}/final/authenticity_s1i{image_number}_{issue_number}_of_{total_issues}.zip"
        ISSS=f"{D}/final/ISSUE*"

        run(f"rm {TXTS} {ZIPS} {ISSS}")

