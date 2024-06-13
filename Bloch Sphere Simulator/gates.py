# Created by: Jas Khetani
# Concept Implemented: Single-Qubit Gates Calculation

import numpy as np

# X Gate: |0〉to |1〉(x-axis rotation)
def X(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, np.pi*(intensity/100), -(np.pi / 2)
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# Y Gate: |0〉to |1〉(y-axis rotation)
def Y(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, np.pi*(intensity/100), 0
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# Z Gate: |+〉to |-〉(z-axis rotation)
def Z(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, 0, np.pi*(intensity/100)
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# H Gate: |0〉to |+〉(xz-axis rotation)
def H(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, # Working on this gate...
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# S Gate: |+〉to |+i〉(z-axis rotation)
def S(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, 0, (np.pi/2)*(intensity/100)
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# antiS Gate: |+〉to |-i〉(z-axis rotation)
def antiS(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, 0, -(np.pi/2)*(intensity/100)
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# T Gate: Half of S Gate (z-axis rotation)
def T(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, 0, (np.pi/4)*(intensity/100)
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# antiT Gate: Half of antiS Gate (z-axis rotation)
def antiT(intensity=100, oldx=0, oldy=0, oldz=0):
    x, y, z, theta, phi = oldx, oldy, oldz, 0, -(np.pi/4)*(intensity/100)
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z

# A Gate: Abstractly controlled by theta and phi angles (custom rotations)
def A(theta=0, phi=0, oldx=0, oldy=0, oldz=0):
    x, y, z = oldx, oldy, oldz
    x += np.sin(theta) * np.cos(phi)
    y += np.sin(theta) * np.sin(phi)
    z += np.cos(theta)
    return x, y, z