import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import itertools as it
import math as m


def work(c, r, step, al, rat=0):
    X = []
    move1, move2 = it.count(c[0], 3 * r * m.cos(m.radians(al))), it.count(c[1], + 3 * r * m.sin(m.radians(al)))
    for i in range(step):
        X += [RegularPolygon((next(move1), next(move2)), numVertices=6, radius=r, edgecolor='red', orientation=rat)]
    return X
def gener(X):
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    for i in X:
        hex = i
        ax.add_patch(hex)
    plt.autoscale(enable=True)
    plt.show()