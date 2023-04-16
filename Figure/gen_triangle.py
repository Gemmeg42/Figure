import numpy as np
import matplotlib.pyplot as plt
import math as m

def gener(quan, args, al=0):
    X = []
    t = [i[0] for i in args]
    t = max(t) - min(t)
    for i in range(quan):
        for j in args:
            X += [np.array(([j[0] + 2*t*i*m.cos(m.radians(al)), (j[1]) + 2*t*i*m.sin(m.radians(al))]))]
    X = np.array(X)
    Y = ['red'] * 3*quan
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], s=0, color='red')
    for j in range(quan):
        t = plt.Polygon(X[j*3:j*3+3], color='red')
        plt.gca().add_patch(t)

    plt.show()