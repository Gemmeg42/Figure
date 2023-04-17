import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math as m

def work(h, w, quan, args, al=0):
    X = []
    for i in range(quan):
        X += [matplotlib.patches.Rectangle((args[0] + 2*h*i*m.cos(m.radians(al)), args[1] + 2*w*i*m.sin(m.radians(al))), h, w)]
    return X


def gener(X, h, w):
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    for i in X:
        hex = i
        ax.add_patch(hex)
    plt.autoscale(enable=True)
    plt.show()