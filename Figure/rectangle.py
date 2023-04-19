import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math as m
import itertools as it

def work(h, w, quan, args, al=0):
    X = []
    move1, move2 = it.count(args[0], 2*h*m.cos(m.radians(al))), it.count(args[1], 2*w*m.sin(m.radians(al)))
    for i in range(quan):
        X += [matplotlib.patches.Rectangle((next(move1), next(move2)), h, w)]
    return X


def gener(X, h, w):
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    for i in X:
        hex = i
        ax.add_patch(hex)
    plt.autoscale(enable=True)
    plt.show()