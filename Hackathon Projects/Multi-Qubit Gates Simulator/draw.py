# Created by: Jas Khetani
# Concept Implemented: Visualization Simulator
# Tech Stack used: Matplotlib

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import floor
import numpy as np

def size(n):
    if n==1:
        return 1
    elif n==2:
        return 3.5
    else:
        return size(n-1)+(5*(n-2))

def rotated(x, y, angle_deg, center=(0, 0)):
    angle_rad = np.radians(angle_deg)
    cx, cy = center
    x, y = x - cx, y - cy
    x_rotated = x * np.cos(angle_rad) - y * np.sin(angle_rad)
    y_rotated = x * np.sin(angle_rad) + y * np.cos(angle_rad)
    return x_rotated + cx, y_rotated + cy

def visualize(num_of_qubits, states, probabilities):
    # Graph Variables
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('Multi-Qubit Gate Visualization')
    ax.axis('off')
    ax.set_xlim(-1.5, size(num_of_qubits)+0.5)
    ax.set_ylim(-4, 1.5)
    ax.set_aspect('equal')
    
    # Visualization Math Variables
    num_circles = 2**num_of_qubits
    midpoint = num_circles//2
    x, y = 0, 0

    for i in range(num_circles):
        ket = f'|{bin(i)[2:].zfill(num_of_qubits)}⟩'
        cx, cy = x+2.5*(i%midpoint),y-2.5*floor(i/midpoint)
        rx, ry = rotated(cx+1, cy, states[i], (cx, cy))
        ax.add_patch(Circle((cx, cy), 1, fill=False))
        ax.add_patch(Circle((cx, cy), probabilities[i]/100))
        ax.plot([cx, rx], [cy, ry], color='black')
        ax.text(cx-(len(ket)/24), cy-1.3, ket)


if __name__=='__main__':
    '''Test your code below:'''