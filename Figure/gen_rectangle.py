import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math as m


def gener(h, w, quan, args, al=0):
    X = []
    for i in range(quan):
        X += [([args[0] + 2*h*i*m.cos(m.radians(al)), args[0] + 2*w*i*m.sin(m.radians(al))])]
    X = np.array(X)
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], s=0, color='red')
    for j in range(len(X)):
        print(X[j*2:j*2+2])
        t = matplotlib.patches.Rectangle(X[j],h,w, color='red')
        plt.gca().add_patch(t)

    plt.show()