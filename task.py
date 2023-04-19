import dif_types
from Figure import triangle
from dif_types import tr_symmetry


def task_1():
    dif_types.tr_translate(3, 20, 'tr')

def task_2():
    a = [40, 0]
    b = [0, 20]
    r, s = 5, 10
    al1, al2 = 0, 60
    X = triangle.work(b, r, s, al=al1)
    X += triangle.work(a, r, s, al=al2)
    triangle.gener(X)

def task_3():
    dif_types.tr_symmetry('tr')

def task_4():
    dif_types.tr_homothety('re')