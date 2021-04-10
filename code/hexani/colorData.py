#!/bin/python

import random
from itertools import count, islice
from math import sqrt
import os
import numpy as np

# sample rate | "resolution" of the sampling
Sample_Rate = 1700

# the frequency of the signal, lower = slower
# frequency = 8  # very short spectrum of brown and blue
# frequency = 31  # higher greq of 8
# frequency = 8  # vert psychedelic
# Sample_Rate = 1700
# frequency = 20  # vert psychedelic


amplitude = 234  # max/shift value
time_counter = 0  # time counter | postion along the 'x'/horizontal axis


def getPi(i):
    pn = "243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89452821E638D01377BE5466CF34E90C6CC0AC29B7C97C50DD3F84D5B5B54709179216D5D98979FB1BD1310BA698DFB5AC2FFD72DBD01ADFB7B8E1AFED6A267E96BA7C9045F12C7F9924A19947B3916CF70801F2E2858EFC16636920D871574E69A458FEA3F4933D7E0D95748F728EB658718BCD5882154AEE7B54A41DC25A59B59C30D5392AF26013C5D1B023286085F0CA417918B8DB38EF8E79DCB0603A180E6C9E0E8BB01E8A3ED71577C1BD314B2778AF2FDA55605C60E65525F3AA55AB945748986263E8144055CA396A2AAB10B6B4CC5C341141E8CEA15486AF7C72E993B3EE1411636FBC2A2BA9C55D741831F6CE5C3E169B87931EAFD6BA336C24CF5C7A325381289586773B8F48986B4BB9AFC4BFE81B6628219361D809CCFB21A991487CAC605DEC8032EF845D5DE98575B1DC262302EB651B8823893E81D396ACC50F6D6FF383F442392E0B4482A484200469C8F04A9E1F9B5E21C66842F6E96C9A670C9C61ABD388F06A51A0D2D8542F68960FA728AB5133A36EEF0B6C137A3BE4BA3BF0507EFB2A98A1F1651D39AF017666CA593E82430E888CEE8619456F9FB47D84A5C33B8B5EBEE06F75D885C12073401A449F56C16AA64ED3AA62363F77061BFEDF72429B023D37D0D724D00A1248DB0FEAD349F1C09B075372C980991B7B25D479D8F6E8DEF7E3FE501AB6794C3B976CE0BD04C006BAC1A94FB6409F60C45E5C9EC2196A246368FB6FAF3E6C53B51339B2EB3B52EC6F6DFC511F9B30952CCC814544AF5EBD09BEE3D004DE334AFD660F2807192E4BB3C0CBA85745C8740FD20B5F39B9D3FBDB5579C0BD1A60320AD6A100C6402C7279679F25FEFB1FA3CC8EA5E9F8DB3222F83C7516DFFD616B152F501EC8AD0552AB323DB5FAFD23876"
    pna = list(pn)
    pns = f"{pna[i]}{pna[i + 1]}{pna[i + 2]}{pna[i + 3]}{pna[i + 4]}{pna[i + 5]}"
    return (pns)


def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


def get_sine(SAMPLE_RATE, FREQUENCY, TIME):
    "Calculate a sine wave"
    return np.sin(2 * np.pi * FREQUENCY * TIME / SAMPLE_RATE)


def get_cosine(SAMPLE_RATE, FREQUENCY, TIME):
    "Calculate a cosine wave"
    return np.cos(2 * np.pi * FREQUENCY * TIME / SAMPLE_RATE)


def shift(NUMBER, AMPLITUDE):
    "Shift the value according to the Amplitude"
    shift_val = (AMPLITUDE / 2) + 0.5
    return (shift_val * NUMBER) + shift_val


def clean_round(NUMBER):
    "Round off and remove trailing decimals"
    return int(NUMBER)


def sine(TIME, buf, tweak, Sample_Rate, frequency):
    amplitude = 254 - buf  # max/shift value
    "Calculate and return the final sine value"
    v = clean_round(shift(get_sine(Sample_Rate, frequency, TIME), amplitude)) + int(buf / 2)

    if (tweak == 1):
        if v > 180:
            v = v * 1 - (amplitude / v)
        if v < 180:
            v = v * 1 + (v / amplitude)
    if (tweak == 2):
        v = 100

    return (round(v))


def cosine(TIME, buf, tweak, Sample_Rate, frequency):
    amplitude = 254 - buf  # max/shift value
    "Calculate and return the final cosine value"
    return clean_round(shift(get_cosine(Sample_Rate, frequency, TIME), amplitude)) + int(buf / 2)


def getwaves(type, buf, Sample_Rate, frequency):
    R = []
    G = []
    B = []

    if type == "SinSinSin":
        for i in range(0, 361):
            R.append(sine(i, buf, 1, Sample_Rate, frequency))
            G.append(sine(i + 120, buf, 1, Sample_Rate, frequency))
            B.append(sine(i + 240, buf, 1, Sample_Rate, frequency))
    if type == "SinCosSin":
        for i in range(0, 361):
            R.append(sine(i, buf, 1, Sample_Rate, frequency))
            G.append(sine(i, buf, 1, Sample_Rate, frequency))
            B.append(sine(i + 180, buf, 1, Sample_Rate, frequency))
    if type == "SinCosDelta":
        for i in range(0, 361):
            s = sine(i, buf, 0, Sample_Rate, frequency)
            c = cosine(i, buf, 0, Sample_Rate, frequency)
            d = abs(c - s)
            R.append(s)
            G.append(c)
            B.append(d)
    if type == "prog_A":
        for i in range(0, 361):
            R.append(sine((i), buf, 1, Sample_Rate, frequency))
            G.append(sine((i + 120) * 1.618, buf, 1, Sample_Rate, frequency))
            B.append(sine((i + 240) * 0.610, buf, 1, Sample_Rate, frequency))
    if type == "prog_B":
        for i in range(0, 361):
            R.append(sine((i), buf, 0, Sample_Rate, frequency))
            G.append(sine((i + 60) * 2, buf, 0, Sample_Rate, frequency))
            B.append(sine((i + 120) * .5, buf, 0, Sample_Rate, frequency))
    if type == "prog_C":
        for i in range(0, 361):
            a = sine((i), buf, 0, Sample_Rate, frequency)
            b = sine((i + 120) * 1.414, buf, 0, Sample_Rate, frequency)
            c = sine((i + 240) * 0.707, buf, 0, Sample_Rate, frequency)
            # b = sine(i*1.618,buf,0,,Sample_Rate, frequency)
            # c = sine(i*0.618,buf,0,,Sample_Rate, frequency)
            R.append(a)
            G.append(b)
            B.append(c)
    S = []
    for j in range(0, 361):
        rs = str(hex(R[j] % 255))[2:].zfill(2)
        gs = str(hex(G[j] % 255))[2:].zfill(2)
        bs = str(hex(B[j] % 255))[2:].zfill(2)
        # print(f"{j}\t{rs}\t{gs}\t{bs}")
        S.append(f"#{rs}{gs}{bs}")
    return (S)


def rndClr():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = hex_number[2:]
    hex_number = hex_number.zfill(6)
    return ("#" + hex_number)


def progClr2(i):  # liner division from 000000 to FFFFFF, step 46000
    a = getPi(i)  # convert to decimal
    return (f"#{a}")


def progClr3(i):  # liner division from 000000 to FFFFFF, step 4600
    clr = []
    for a in range(0, 16777215, 4600):
        # convert to decimal
        # if (ssum(a) == 9):
        dc = hex(a)
        dc = dc[2:]
        dc = dc.zfill(6)
        clr.append(f"#{dc}")
    return (clr[i % len(clr)])


def progClr4(i):  # liner division from FFFFFF to 000000, step 46000
    clr = []
    for a in range(0, 16777215, 70000):
        # convert to decimal
        dc = hex(a)
        dc = dc[2:]
        dc = dc.zfill(6)
        clr.append(f"#{dc}")
    return (clr[i % len(clr)])


def progClr5(i, flag="slow"):
    Sample_Rate = 1700
    frequency = 20
    if flag == "fast":
        Sample_Rate = 700
        frequency = 80
    clr = getwaves("SinSinSin", 10, Sample_Rate, frequency)
    return (clr[i % len(clr)])


def progClr6(i):
    Sample_Rate = 1700
    frequency = 20
    clr = getwaves("SinCosSin", 10, Sample_Rate, frequency)
    return (clr[i % len(clr)])


def progClr7(i, flag="slow"):
    Sample_Rate = 1700
    frequency = 20
    if flag == "fast":
        Sample_Rate = 700
        frequency = 80
    clr = getwaves("SinCosDelta", 10, Sample_Rate, frequency)
    return (clr[i % len(clr)])


def progClr8(i):
    Sample_Rate = 1700
    frequency = 20
    clr = getwaves("prog_A", 10, Sample_Rate, frequency)
    return (clr[i % len(clr)])


def progClr9(i):
    Sample_Rate = 1700
    frequency = 20
    clr = getwaves("prog_B", 10, Sample_Rate, frequency)
    return (clr[i % len(clr)])


def progClr10(i, flag="slow"):
    Sample_Rate = 1700
    frequency = 20
    if (flag == "fast"):
        Sample_Rate = 700
        frequency = 80
    if (flag == "medium"):
        Sample_Rate = 1200
        frequency = 50
    clr = getwaves("prog_C", 10, Sample_Rate, frequency)
    return (clr[i % len(clr)])


def getColors():
    jump = 1
    for i in range(0, 361, 1):
        ANGLE = int(i * 0.71111111111)  # i % 256
        # ANGLE = i % 256
        # ANGLE = int(i * 0.5)
        print(f"----------------------------------------------------{ANGLE} ({i})")
        colors = {
            'random': [rndClr(), rndClr(), rndClr(), rndClr(), rndClr(), rndClr()],
            'denimbamboo': ["#3a5065", "#e7d5ad","#3a5065", "#e7d5ad","#3a5065", "#e7d5ad"],
            'greens': ["#68bb59", "#acdf87", "#4c9a2a", "#76ba1b", "#a4de02", "#1e5631"],
            'browns': ["#33190b", "#672400", "#a14415", "#a95815", "#c69552", "#d7b17e"],
            'darkgrays': ["#000000", "#111111", "#222222", "#333333", "#444444", "#555555"],
            'lightgrays': ["#ffffff", "#eeeeee", "#dddddd", "#cccccc", "#bbbbbb", "#aaaaaa"],
            'default': ["#5a3313", "#a86f3b", "#7d8558", "#cecc06", "#cb7d98", "#ca4c25", "#d4db37"],
            'medical_gray': ["#567097", "#6291d8", "#aed4c4", "#6ed0eb"],
            'medical_gray_3': ["#567097", "#6291d8", "#6ed0eb"],
            'aura_red': ["#F51720", "#FA26A0", "#F8D210", "#2FF3E0"],
            'pi': [progClr2(ANGLE), progClr2(ANGLE + 1), progClr2(ANGLE + 2), progClr2(ANGLE + 3), progClr2(ANGLE + 4), progClr2(ANGLE + 5)],
            'progressive3': [progClr3(ANGLE), progClr3(ANGLE + 1), progClr3(ANGLE + 2), progClr3(ANGLE + 3), progClr3(ANGLE + 4), progClr3(ANGLE + 5)],
            'progressive4': [progClr4(ANGLE), progClr4(ANGLE + 1), progClr4(ANGLE + 2), progClr4(ANGLE + 3), progClr4(ANGLE + 4), progClr4(ANGLE + 5)],
            'SinSinSin': [progClr5(ANGLE + jump * 0), progClr5(ANGLE + jump * 1), progClr5(ANGLE + jump * 2), progClr5(ANGLE + jump * 3), progClr5(ANGLE + jump * 4), progClr5(ANGLE + jump * 5)],
            'SinSinSinFast': [progClr5(ANGLE + jump * 0, "fast"), progClr5(ANGLE + jump * 1, "fast"), progClr5(ANGLE + jump * 2, "fast"), progClr5(ANGLE + jump * 3, "fast"), progClr5(ANGLE + jump * 4, "fast"), progClr5(ANGLE + jump * 5, "fast")],
            'SinCosSin': [progClr6(ANGLE + jump * 0), progClr6(ANGLE + jump * 1), progClr6(ANGLE + jump * 2), progClr6(ANGLE + jump * 3), progClr6(ANGLE + jump * 4), progClr6(ANGLE + jump * 5)],
            'SinCosDelta': [progClr7(ANGLE + jump * 0), progClr7(ANGLE + jump * 1), progClr7(ANGLE + jump * 2), progClr7(ANGLE + jump * 3), progClr7(ANGLE + jump * 4), progClr7(ANGLE + jump * 5)],
            'SinCosDeltaFast': [progClr7(ANGLE + jump * 0, "fast"), progClr7(ANGLE + jump * 1, "fast"), progClr7(ANGLE + jump * 2, "fast"), progClr7(ANGLE + jump * 3, "fast"), progClr7(ANGLE + jump * 4, "fast"), progClr7(ANGLE + jump * 5, "fast")],
            'prog_A': [progClr8(ANGLE + jump * 0), progClr8(ANGLE + jump * 1), progClr8(ANGLE + jump * 2), progClr8(ANGLE + jump * 3), progClr8(ANGLE + jump * 4), progClr8(ANGLE + jump * 5)],
            'prog_B': [progClr9(ANGLE + jump * 0), progClr9(ANGLE + jump * 1), progClr9(ANGLE + jump * 2), progClr9(ANGLE + jump * 3), progClr9(ANGLE + jump * 4), progClr9(ANGLE + jump * 5)],
            'prog_C': [progClr10(ANGLE + jump * 0), progClr10(ANGLE + jump * 1), progClr10(ANGLE + jump * 2), progClr10(ANGLE + jump * 3), progClr10(ANGLE + jump * 4), progClr10(ANGLE + jump * 5)],
            'prog_C_fast': [progClr10(ANGLE + jump * 0, "fast"), progClr10(ANGLE + jump * 1, "fast"), progClr10(ANGLE + jump * 2, "fast"), progClr10(ANGLE + jump * 3, "fast"), progClr10(ANGLE + jump * 4, "fast"), progClr10(ANGLE + jump * 5, "fast")],
            'prog_C_medium': [progClr10(ANGLE + jump * 0, "medium"), progClr10(ANGLE + jump * 1, "medium"), progClr10(ANGLE + jump * 2, "medium"), progClr10(ANGLE + jump * 3, "medium"), progClr10(ANGLE + jump * 4, "fast"), progClr10(ANGLE + jump * 5, "medium")],
        }
        # print(colors)
        np.save(f"colordata/{i}", colors)


spec = {'pi': [],
        'progressive3': [],
        'progressive4': [],
        'SinSinSin': [],
        'SinSinSinFast': [],
        'SinCosSin': [],
        'SinCosDelta': [],
        'SinCosDeltaFast': [],
        'prog_A': [],
        'prog_B': [],
        'prog_C': [],
        'prog_C_fast': [],
        'prog_C_medium': [],
        }


def getSpectrums():
    jump = 1
    for i in range(0, 361, 1):
        ANGLE = int(i * 0.71111111111)  # i % 256
        print(f"----------------------------------------------------{ANGLE} ({i})")
        spec['pi'].append(progClr2(ANGLE))
        spec['progressive3'].append(progClr3(ANGLE))
        spec['progressive4'].append(progClr4(ANGLE))
        spec['SinSinSin'].append(progClr5(ANGLE))
        spec['SinSinSinFast'].append(progClr5(ANGLE, "fast"))
        spec['SinCosSin'].append(progClr6(ANGLE))
        spec['SinCosDelta'].append(progClr7(ANGLE))
        spec['SinCosDeltaFast'].append(progClr7(ANGLE, "fast"))
        spec['prog_A'].append(progClr8(ANGLE))
        spec['prog_B'].append(progClr9(ANGLE))
        spec['prog_C'].append(progClr10(ANGLE))
        spec['prog_C_fast'].append(progClr10(ANGLE, "fast"))
        spec['prog_C_medium'].append(progClr10(ANGLE, "medium"))
        np.save(f"colordata/spectrums", spec)
    print(spec)


cmd = "rm colordata/*"
os.system(cmd)
getColors()

getSpectrums()
