# Created by: Jas Khetani
# Concept Implemented: Bloch Sphere for Single-Qubit Circuit Visualization

import numpy as np
import matplotlib.pyplot as plt
from gates import *

# Create a new figure for the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the parameters for the sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface of the sphere
ax.plot_surface(x, y, z, color='b', alpha=0.6, edgecolor='w')

# Set the labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sphere')

# Set the aspect ratio to be equal
ax.set_box_aspect([1, 1, 1])

# Show the plot
plt.show()
