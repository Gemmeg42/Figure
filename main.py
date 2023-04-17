import itertools
from Figure import triangle
from Figure import rectangle
from Figure import hexagon



def base(t=0):
    while t in [1, 2, 3]:
        t = int(input('Какую фигуру вы хотите построить?\n1.Треугольник\n2.Прямоугольник\n3.Шестиугольник '))
        m = input('включить поворот? (y/n)')
        if t == 1:
            a = (int(input('x - ')), int(input('y - ')))
            r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
            triangle.gener(triangle.work(a, r, s, al=al))
        elif t == 2:
            a = (int(input('x - ')), int(input('y - ')))
            h, w, i, al = int(input('длина - ')), int(input('высота - ')), int(input('кол-во: ')), int(input('угол наклона: '))
            rectangle.gener(rectangle.work(h, w, i, a, al=al), h, w)
        else:
            a = (int(input('x - ')), int(input('y - ')))
            r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
            hexagon.gener(hexagon.work(a, r, s, al=al))

base(t=2)