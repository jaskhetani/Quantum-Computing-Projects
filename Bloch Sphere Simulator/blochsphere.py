# Created by: Jas Khetani
# Concept Implemented: Bloch Sphere for Single-Qubit Circuit Visualization
# Tech Stack used: MatPlotLib, Numpy

import numpy as np
import matplotlib.pyplot as plt
from gates import *

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

def bloch_sphere():
    # Initialising all constants to create the Sphere
    u, v = np.linspace(0, 2 * np.pi, 100), np.linspace(0, np.pi, 100)
    x, y, z = np.outer(np.cos(u), np.sin(v)), np.outer(np.sin(u), np.sin(v)), np.outer(np.ones(np.size(u)), np.cos(v))

    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

    ax.plot_surface(x, y, z, color='c', alpha=0.3, rstride=5, cstride=5, edgecolor='w')

    # Declaring all sides of the Bloch Sphere (|0⟩, |1⟩, |+⟩, |-⟩, |+i⟩, |-i⟩)
    ax.text(1.1, 0, 0, r'$|+\rangle$', color='r', fontsize=15)
    ax.text(-1.2, 0, 0, r'$|-\rangle$', color='r', fontsize=15)
    ax.text(0, 1.1, 0, r'$|+i\rangle$', color='g', fontsize=15)
    ax.text(0, -1.2, 0, r'$|-i\rangle$', color='g', fontsize=15)
    ax.text(0, 0, 1.1, r'$|0\rangle$', color='b', fontsize=15)
    ax.text(0, 0, -1.2, r'$|1\rangle$', color='b', fontsize=15)
    print(f"X0 = {x}\nY0 = {y}\nZ0 = {z}")

def run(x, y, z):
    # Making the |ψ⟩ arrow
    ax.quiver(0, 0, 0, x, y, z, color='k', arrow_length_ratio=0.1)
    ax.text(x * 1.1, y * 1.1, z * 1.1, r'$|\psi\rangle$', color='k', fontsize=15)
    
    # Setting up the Cartesian Plane
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere')
    ax.set_box_aspect([1, 1, 1])

    # Displaying the results
    plt.show()
    print(f"X = {x}\nY = {y}\nZ = {z}")

if __name__ == '__main__':
    bloch_sphere()
    x, y, z = X(50)
    run(x, y, z)
