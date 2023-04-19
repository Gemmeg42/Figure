import itertools as it
import numpy as np
import math as m
from Figure import triangle
from Figure import rectangle
from Figure import hexagon


def tr_translate(num, size, typ):
    a = [int(input('x - ')), int(input('y - '))]
    X = []
    move = it.count(a[1],size)
    if typ == 'tr':
        r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
        for i in range(num):
            b = [a[0], next(move)]
            X += triangle.work(b, r, s, al=al)
        triangle.gener(X)
    elif typ == 're':
        h, w, kol, al = int(input('длина - ')), int(input('высота - ')), int(input('кол-во: ')), int(input('угол наклона: '))
        for i in range(num):
            b = [a[0], next(move)]
            X += rectangle.work(h, w, kol, b, al=al)
        rectangle.gener(X, h, w)
    else:
        r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
        for i in range(num):
            b = [a[0], next(move)]
            X += hexagon.work(b, r, s, al=al)
        hexagon.gener(X)

def tr_rotate(typ, al):
    X = []
    a = [int(input('x - ')), int(input('y - '))]
    al = it.cycle(al)
    if typ == 'tr':
        r, s = int(input('радиус - ')), int(input('кол-во - '))
        for i in range(len(al)):
            X += triangle.work(a, r, s, al=next(al))
        triangle.gener(X)
    elif typ == 're':
        h, w, kol = int(input('длина - ')), int(input('высота - ')), int(input('кол-во: '))
        for i in range(len(al)):
            X += rectangle.work(h, w, kol, a, al=next(al))
        rectangle.gener(X, h, w)
    else:
        r, s = int(input('радиус - ')), int(input('кол-во - '))
        for i in range(len(al)):
            X += hexagon.work(a, r, s, al=next(al))
        hexagon.gener(X)


def tr_symmetry(typ):
    X = []
    a = [int(input('x - ')), int(input('y - '))]
    if typ == 'tr':
        r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
        X += triangle.work(a, r, s, al=al)
        a[1] = a[1] + 2*r + 1
        X += triangle.work(a, r, s, al=al, rat=m.radians(180))
        triangle.gener(X)
    elif typ == 're':
        h, w, i, al = int(input('длина - ')), int(input('высота - ')), int(input('кол-во: ')), int(input('угол наклона: '))
        X += rectangle.work(h, w, i, a, al=al)
        a[1] = a[1] + 2*h + 1
        X += rectangle.work(h, w, i, a, al=al)
        triangle.gener(X)
    else:
        r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
        X += hexagon.work(a, r, s, al=al)
        a[1] = a[1] + 2*r + 1
        X += hexagon.work(a, r, s, al=al, rat=m.radians(180))
        hexagon.gener(X)


def tr_homothety(typ):
    X = []
    a, al = [int(input('x - ')), int(input('y - '))], int(input('угол наклона: '))
    if typ == 'tr':
        r, s = int(input('радиус - ')), 1
        t = 3
        for i in range(1, t+1):
            X += triangle.work(a, r, s, al=al)
            X += triangle.work([-i for i in a], r, s, al=(180+al))
            r = r*t
            a[0], a[1] = 2*a[0]*t, 2*a[1]*t
        triangle.gener(X)
    elif typ == 're':
        h, w, kol = int(input('длина - ')), int(input('высота - ')), 1
        t = 3
        for i in range(1, t+1):
            X += rectangle.work(h, w, kol, a, al=al)
            X += rectangle.work(h, w, kol, [-i for i in a], al=(al + 180))
            h, w = h*t, w*t
            a[0], a[1] = 2 * a[0] * t, 2 * a[1] * t
        rectangle.gener(X, h, w)
    else:
        r, s = int(input('радиус - ')), 1
        t = 3
        for i in range(1, t+1):
            X += hexagon.work(a, r, s, al=al)
            X += hexagon.work([-i for i in a], r, s, al=(180 + al))
            r = r*t
            a[0], a[1] = 2*a[0]*t, 2*a[1]*t
        hexagon.gener(X)

tr_homothety('tr')