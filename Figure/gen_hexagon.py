import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import math as m



def gener(c, r, step, al):
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    for i in range(step):
        hex = RegularPolygon((c[0] + 3*r*i*m.cos(m.radians(al)), c[1]+ 3*r*i*m.sin(m.radians(al))), numVertices=6, radius=r, edgecolor='red')
        ax.add_patch(hex)
    plt.autoscale(enable=True)
    plt.show()