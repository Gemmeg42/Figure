import itertools
from Figure import gen_triangle
from Figure import gen_rectangle
from Figure import gen_hexagon



def base():
    t = 1
    while t in [1, 2, 3]:
        t = int(input('Какую фигуру вы хотите построить?\n1.Треугольник\n2.Прямоугольник\n3.Шестиугольник '))
        m = input('включить поворот? (y/n)')
        if t == 1:
            a = [(int(input('x - ')), int(input('y - '))) for i in range(3)]
            i, al = int(input('кол-во: ')), int(input('угол наклона: ')) if m=='y' else 0
            gen_triangle.gener(i, a, al=al)
        elif t == 2:
            a = (int(input('x - ')), int(input('y - ')))
            h, w, i, al = int(input('длина - ')), int(input('высота - ')), int(input('кол-во: ')), int(input('угол наклона: '))
            gen_rectangle.gener(h, w, i, a, al=al)
        else:
            a = (int(input('x - ')), int(input('y - ')))
            r, s, al = int(input('радиус - ')), int(input('кол-во - ')), int(input('угол наклона: '))
            gen_hexagon.gener(a, r, s, al=al)

base()