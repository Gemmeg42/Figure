import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import math as m


def work(c, r, step, al, rat=0):
    X = []
    for i in range(step):
        X += [RegularPolygon((c[0] + 3*r*i*m.cos(m.radians(al)), c[1]+ 3*r*i*m.sin(m.radians(al))), numVertices=6, radius=r, edgecolor='red', orientation=rat)]
    return X
def gener(X):
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    for i in X:
        hex = i
        ax.add_patch(hex)
    plt.autoscale(enable=True)
    plt.show()