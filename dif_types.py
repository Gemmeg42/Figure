import itertools
import numpy as np
from Figure import triangle
from Figure import rectangle
from Figure import hexagon


def tr_translate(num, size, typ):
    a = [int(input('x - ')), int(input('y - '))]
    X = []
    if typ == 'tr':
        r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
        for i in range(num):
            b = [a[0], a[1] + size * i]
            X += triangle.work(b, r, s, al=al)
        triangle.gener(X)
    elif typ == 're':
        h, w, kol, al = int(input('длина - ')), int(input('высота - ')), int(input('кол-во: ')), int(input('угол наклона: '))
        for i in range(num):
            b = [a[0], a[1] + size * i]
            X += rectangle.work(h, w, kol, b, al=al)
        rectangle.gener(X, h, w)
    else:
        r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
        for i in range(num):
            b = [a[0], a[1] + size * i]
            X += hexagon.work(b, r, s, al=al)
        hexagon.gener(X)

def tr_rotate(typ, al):
    if typ == 'tr':
        X = []
        a = [int(input('x - ')), int(input('y - '))]
        r, s = int(input('радиус - ')), int(input('кол-во - '))
        for i in range(len(al)):
            X += triangle.work(a, r, s, al=al[i])
        triangle.gener(X)
    elif typ == 're':
        X = []
        a = (int(input('x - ')), int(input('y - ')))
        h, w, kol = int(input('длина - ')), int(input('высота - ')), int(input('кол-во: '))
        for i in range(len(al)):
            X += rectangle.work(h, w, kol, a, al=al[i])
        rectangle.gener(X, h, w)
    else:
        X = []
        a = (int(input('x - ')), int(input('y - ')))
        r, s = int(input('радиус - ')), int(input('кол-во - '))
        for i in range(len(al)):
            X += hexagon.work(a, r, s, al=al[i])
        hexagon.gener(X)