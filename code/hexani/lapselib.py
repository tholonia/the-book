import sys, os
import subprocess
import glob
import shutil
import functools

thisprog = os.path.basename(__file__)


def degidx(type):
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    for i in range(0,361):
        l0.append(i)
        l1.append(i*2)
        l2.append(i * 3)
        l3.append(i * 4)
        l4.append(i * 5)
        l5.append(i * 6)
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]


def sortglob(path):
    g=[]
    for file in glob.glob(path):
        g.append(file)
    g.sort()
    return(g)


def wccopy(src,dst):
    for file in glob.glob(src):
        print(f"copying: {file} -> {dst}", flush=True)
        try:
            shutil.copy2(file,dst)
        except OSError as error:
            print(f"ERROR copying: {error}", flush=True)

def wcdel(path):
    for file in glob.glob(path):
        if os.path.exists(file):
            print(f"deleting {file}", flush=True)
            try:
                os.remove(file)
            except OSError as error:
                print(f"ERROR deleting: {error}", flush=True)

def banner(str):
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("*******************************************************************************")
    print(f"             {str}")
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("*******************************************************************************")

def wcremove(file):
    if os.path.exists(file):
        print(f"deleting {file}", flush=True)
        try:
            os.remove(file)
        except OSError as error:
            print(f"ERROR deleting: {error}", flush=True)


def rm_rf(path):
    print(f"deleting tree: {path}", flush=True)
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
        except OSError as error:
            print(f"ERROR rmdir: {error}", flush=True)

def wcmkdir(path):
    if not os.path.exists(path):
        print(f"make dir: {path}", flush=True)
        try:
            os.mkdir(path)
        except OSError as error:
            print(f"ERROR mkdir: {error}", flush=True)

def runthis(cmd,id="#XX", thatprog="UNKNOWN", nohup=True, printonly=False):
    cmd = cmd.strip()
    if nohup:
        cmd = "nohup "+cmd


    # lst = cmd.split(" ")
    # command =[]
    # command.append(lst[0])
    #
    # lst.reverse()
    # lst.pop()
    # lst.reverse()
    # command.extend(lst)

    print( "┌───────────────────────────────────────────────────", flush=True)
    print(f"│PREPARING TO RUN [{id}]: '{cmd}'", flush=True)
    print( "└───────────────────────────────────────────────────", flush=True)
    exitcode = 0
    
    if (printonly == False):
        if os.system(cmd) == 0:
            pass
        else:
            print(f"ERROR (exitstatus != 0 for {cmd}", flush=True)
    else:
        print(f"PRINTONLY: \n\n{cmd}\n\n")
    # os.system(cmd)
    # try:
    #     # output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     output = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     output = subprocess.check_output(command, stderr=subprocess.PIPE)
    #     output = output.decode("utf-8")
    #     print(f"=[{str(output)}]=",flush=True)
    # except subprocess.CalledProcessError as e:
    #     exitcode = e.returncode
    #     print('exit code: {}'.format(e.returncode))
    #     print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
    #     print('stderr: {}'.format(e.stderr.decode(sys.getfilesystemencoding())))


    # if (exitcode == 0):
    #     print( ">>>┌───────────────────────────────────────────────────", flush=True)
    #     print(f">>>│SUCCESS [{id}]: {cmd}", flush=True)
    #     print( ">>>└───────────────────────────────────────────────────", flush=True)
    # else:
    #     print("\t!!!┌───────────────────────────────────────────────────", flush=True)
    #     print(f"\t!!!│ SCRIPT ({thatprog}) CRASHED [{id}] with exitcode ({exitcode})>>> {cmd}", flush=True)
    #     print("\t!!!└───────────────────────────────────────────────────", flush=True)
    #     exit()
    # return(exitcode)



def argstring(C):
    argstr = ""
    for key in C['args']:
        v = C['args'][key]
        a = f" --{key} {v}"
        argstr = argstr + a
    return(argstr)


def get_complementary(color):
    rd = 255 - color[0]
    gd = 255 - color[1]
    bd = 255 - color[2]

    rh = hex(int(rd))[2:].zfill(2)
    gh = hex(int(gd))[2:].zfill(2)
    bh = hex(int(bd))[2:].zfill(2)

    color = f"#{rh}{gh}{bh}"

    # strip the # from the beginning
    color = color[1:]

    # convert the string into hex
    color = int(color, 16)

    # invert the three bytes
    # as good as substracting each of RGB component by 255(FF)
    comp_color = 0xFFFFFF ^ color

    # convert the color back to hex by prefixing a #
    comp_color = "#%06X" % comp_color

    # return the result
    return comp_color


def get_constrast_color(color):
    r, g, b = color >> 16, color >> 8, color
    return functools.reduce(
        lambda a, b: (a << 8) | b,
        map(lambda x: 0xff - (x & 0xff), [r, g, b]),
    )

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def int2hex(i,places):
    hv = hex(int(i))[2:]
    hs = str(hv[2:]).zfill(places)
    return [hv,hs]


def listArgs(C):
    desc = ""
    for key in C:
        desc = desc + f"{key}\n"
        for key2 in C[key]:
            if (key2 != "root") and (key2 != "repo"):
                desc = desc + f"\t{key2}: {C[key][key2]}\n"
    return(desc)
