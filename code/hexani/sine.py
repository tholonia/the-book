#!/usr/bin/python
from math import pi, sin, cos
from time import sleep, time

Sample_Rate = 1000  # sample rate | "resolution" of the sampling
frequency = 30  # the frequency of the signal, lower = slower
amplitude = 254  # max/shift value
time_counter = 0  # time counter | postion along the 'x'/horizontal axis


def get_sine(SAMPLE_RATE, FREQUENCY, TIME):
    "Calculate a sine wave"
    return sin(2 * pi * FREQUENCY * TIME / SAMPLE_RATE);


def get_cosine(SAMPLE_RATE, FREQUENCY, TIME):
    "Calculate a cosine wave"
    return cos(2 * pi * FREQUENCY * TIME / SAMPLE_RATE);


def shift(NUMBER, AMPLITUDE):
    "Shift the value according to the Amplitude"
    shift_val = (AMPLITUDE / 2) + 0.5
    return (shift_val * NUMBER) + shift_val;


def clean_round(NUMBER):
    "Round off and remove trailing decimals"
    return int(NUMBER);


def sine(TIME):
    "Calculate and return the final sine value"
    return clean_round(shift(get_sine(Sample_Rate, frequency, TIME), amplitude));


def cosine(TIME):
    "Calculate and return the final cosine value"
    return clean_round(shift(get_cosine(Sample_Rate, frequency, TIME), amplitude));


######
# Print a co/sine wave set of values

Rs = []
Rc = []
i = 0
while i <= 360:
    # Use the timer counter:
    sval = sine(i)
    Rs.append(sval)
    sval = cosine(i)
    Rc.append(sval)
    i += 1

Gs = []
Gc = []
i = 0
while i <= 360:
    # Use the timer counter:
    sval = sine(i)
    Gs.append(sval)
    sval = cosine(i)
    Gc.append(sval)
    i += 1

Bs = []
Bc = []
i = 0
while i <= 360:
    # Use the timer counter:
    sval = sine(i+180)
    Bs.append(sval)

    sval = cosine(i)
    Bc.append(sval)
    i += 1


i = 0
S=[]
C=[]
while i <= 360:
    rds = Rs[i]
    gds = Gs[i]
    bds = Bs[i]

    rdc = Rc[i]
    gdc = Gc[i]
    bdc = Bc[i]

    rs = str(hex(Rs[i]))[2:].zfill(2)
    gs = str(hex(Gs[i]))[2:].zfill(2)
    bs = str(hex(Bs[i]))[2:].zfill(2)

    S.append(f"#{rs}{gs}{bs}")

    rc = str(hex(Rc[i]))[2:].zfill(2)
    gc = str(hex(Gc[i]))[2:].zfill(2)
    bc = str(hex(Bc[i]))[2:].zfill(2)

    C.append(f"#{rc}{gc}{bc}")

    return([S, C])


    print(f"{rd} - {gd} - {bd} = {r}:"
          f""
          f"{g}:{b}")
    i += 1

print("clr = [", end="")
for i in range(0,400):
    r = str(hex(R[i]))[2:].zfill(2)
    g = str(hex(G[i]))[2:].zfill(2)
    b = str(hex(B[i]))[2:].zfill(2)

    print(f"'#{r}{g}{b}',", end="")

print("]", end="")
