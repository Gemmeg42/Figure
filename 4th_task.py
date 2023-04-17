import dif_types
from Figure import triangle


def task_1():
    a = [20, 40, 60]
    dif_types.tr_rotate('tr', [20, 40, 60])

def task_2():
    a = [40, 0]
    b = [0, 20]
    r, s = 5, 10
    al1, al2 = 0, 60
    X = triangle.work(b, r, s, al=al1)
    X += triangle.work(a, r, s, al=al2)
    triangle.gener(X)

def task_3():


task_2()