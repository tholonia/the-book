import glob
import os

def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files

subfolders, files = run_fast_scandir("/home/jw/store/books/tholonia/code/hexani", [".txt"])

print(subfolders, flush=True)
print(files, flush=True)

#input file
fin = open("data.txt", "rt")
#output file to write the result to
fout = open("out.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('pyton', 'python'))
#close input and output files
fin.close()
fout.close()