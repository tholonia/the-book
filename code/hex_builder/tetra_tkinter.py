from pprint import pprint
try:
    from tkinter import *  # python 3
except ImportError:
    from Tkinter import *  # python 2
from math import *


def createZeroMat(m, n):
    """Return a matrix (m x n) filled with zeros."""

    ret = [0] * m
    for i in range(m):
        ret[i] = [0] * n
    return ret


def matMul(mat1, mat2):
    """Return mat1 x mat2 (mat1 multiplied by mat2)."""

    m = len(mat1)
    n = len(mat2[0])
    common = len(mat2)

    ret = createZeroMat(m, n)
    if len(mat1[0]) == len(mat2):
        for i in range(m):
            for j in range(n):
                for k in range(common):
                    ret[i][j] += mat1[i][k] * mat2[k][j]
    return ret


def matTrans(mat):
    """Return mat (n x m) transposed (m x n)."""

    m = len(mat[0])
    n = len(mat)

    ret = createZeroMat(m, n)
    for i in range(m):
        for j in range(n):
            ret[i][j] = mat[j][i]
    return ret


def translate(x, y, dx, dy):
    """Translate vector(x,y) by (dx,dy)."""

    return x + dx, y + dy

def revtranslate(x, y, dx, dy):
    """Translate vector(x,y) by (dx,dy)."""
    # x = (x * cos(90)) - (y * sin(90))
    # x + dx
    #
    # y = (y * cos(90)) + (x * sin(90))
    # y + dy

    X = (x * cos(60)) - (dx * sin(60))
    Y = (y * cos(dy)) + (dy * sin(60))

    X = x + dx
    Y = y + dy

    return X,Y


def drawTet(tet, rtet, col):



    # return()
    """Draw a tetrahedron."""
    w = canvas.winfo_width() / 2
    h = canvas.winfo_height() / 2
    canvas.delete(ALL)  # delete all edges
    nv = len(tet[0])  # number of vertices in tet (4)
    # draw the 6 edges of the tetrahedron


    for p1 in range(nv):
        for p2 in range(p1 + 1, nv):
            col="black"
            if p1==0:
                if p2==1:
                    col="red"
                if p2==2:
                    col="green"
                if p2==3:
                    col="blue"

            x1=tet[0][p1]
            y1=tet[1][p1]
            x2=tet[0][p2]
            y2=tet[1][p2]

            lFrom = translate(x1,y1,w,h)
            lTo = translate(x2,y2,w,h)

            print ("FROM= [",lFrom,"] TO= [",lTo,"] ")
            print ("FROM: [",x1,"] [",y1,"]  TO: [",x2,"] [",y2,"]")
            canvas.create_line(lFrom,lTo,fill=col,width=3)


    for p1 in range(nv):
        for p2 in range(p1 + 1, nv):
            col = "black"
            if p1 == 0:
                if p2 == 1:
                    col = "red"
                if p2 == 2:
                    col = "green"
                if p2 == 3:
                    col = "blue"

            x1 = rtet[0][p1]
            y1 = rtet[1][p1]
            x2 = rtet[0][p2]
            y2 = rtet[1][p2]

            lFrom = translate(x1, y1, w, h)
            lTo = translate(x2, y2, w, h)

            pprint(lFrom)

            print("FROM= [", lFrom, "] TO= [", lTo, "] ")
            print("FROM: [", x1, "] [", y1, "]  TO: [", x2, "] [", y2, "]")
            canvas.create_line(lFrom, lTo, fill=col, width=3)


def init():
    """Initialize global variables."""

    global ROT_X, ROT_Y, ROT_Z
    global eps, EPS, tet,rtet
    global lastX, lastY, tetColor, bgColor

    tet  = matTrans([[   0, -100,  0],   [-100,  100,  0], [100, 100,    0], [    0,    0, 200]])
    rtet = matTrans([[-100  -200, -100], [-200,   -0,  0], [  0,   0, -100], [ -100, -100, 100]])

    # rtet = matTrans([[10, -110, 10], [-110, 110, 10], [110, 110, 10], [10, 10, 200]])

    # counter-clockwise rotation about the X axis
    ROT_X = lambda x: matTrans([[1, 0, 0], [0, cos(x), -sin(x)], [0, sin(x), cos(x)]])

    # counter-clockwise rotation about the Y axis
    ROT_Y = lambda y: matTrans([[cos(y), 0, sin(y)], [0, 1, 0], [-sin(y), 0, cos(y)]])

    # counter-clockwise rotation about the Z axis
    ROT_Z = lambda z: matTrans([[cos(z), sin(z), 0], [-sin(z), cos(z), 0], [0, 0, 1]])

    eps = lambda d: pi / 300 if (d > 0) else -pi / 300
    EPS = lambda d: d * pi / 300

    lastX = 0
    lastY = 0
    tetColor = 'black'
    bgColor = 'white'


def cbClicked(event):
    """Save current mouse position."""

    global lastX, lastY

    lastX = event.x
    lastY = event.y


def cbMottion(event):
    """Map mouse displacements in Y direction to rotations about X axis,
       and mouse displacements in X direction to rotations about Y axis."""

    global tet
    global rtet

    # Y coordinate is upside down
    dx = lastY - event.y
    tet = matMul(ROT_X(EPS(-dx)), tet)
    rtet = matMul(ROT_X(EPS(-dx)), rtet)

    dy = lastX - event.x
    tet = matMul(ROT_Y(EPS(dy)), tet)
    rtet = matMul(ROT_Y(EPS(dy)), rtet)

    drawTet(tet, rtet , tetColor)
    cbClicked(event)


def wheelUp(event):
    """Map mouse wheel up displacements to rotations about Z axis."""

    global tet,rtet
    tet = matMul(ROT_Z(EPS(1)), tet)
    rtet = matMul(ROT_Z(EPS(1)), rtet)
    drawTet(tet, rtet, tetColor)


def wheelDown(event):
    """Map mouse wheel down displacements to rotations about Z axis."""

    global tet,rtet
    tet = matMul(ROT_Z(EPS(-1)), tet)
    rtet = matMul(ROT_Z(EPS(-1)), rtet)
    drawTet(tet,rtet, tetColor)


def wheel(event):
    """Map mouse wheel displacements to rotations about Z axis."""

    global tet,rtet
    tet = matMul(ROT_Z(EPS(event.delta / 120)), tet)
    rtet = matMul(ROT_Z(EPS(event.delta / 120)), rtet)
    drawTet(tet, rtet, tetColor)


def resize(event):
    """Redraw the tetrahedron, in case of a window change due to user resizing it."""

    drawTet(tet, rtet, tetColor)


def main():
    global canvas
    root = Tk()
    root.title('Tetrahedron')
    root.geometry('+0+0')

    init()

    canvas = Canvas(root, width=800, height=800, background=bgColor)
    canvas.pack(fill=BOTH, expand=YES)
    canvas.bind("<Button-1>", cbClicked)
    canvas.bind("<B1-Motion>", cbMottion)
    canvas.bind("<Configure>", resize)

    from platform import uname
    os = uname()[0]
    if (os == "Linux"):
        canvas.bind('<Button-4>', wheelUp)  # X11
        canvas.bind('<Button-5>', wheelDown)
    elif (os == "Darwin"):
        canvas.bind('<MouseWheel>', wheel)  # MacOS
    else:
        canvas.bind_all('<MouseWheel>', wheel)  # windows

    drawTet(tet, rtet, tetColor)
    mainloop()


if __name__ == '__main__':
    sys.exit(main())