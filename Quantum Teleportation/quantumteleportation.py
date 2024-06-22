# Created by: Jas Khetani
# Concept Implemented: Quantum Teleportation (Qiskit)

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

# Qubits:
alice, control, bob = QuantumRegister(1, 'alice'), QuantumRegister(1, 'control'), QuantumRegister(1, 'bob')
# Classical Bits:
c, d = ClassicalRegister(1, 'c'), ClassicalRegister(1, 'd')
# Setting up the circuit
circuit = QuantumCircuit(alice, control, bob, c, d)

# Alice sets her qubit
circuit.u(pi / 3, pi / 6, pi / 9, alice[0])
circuit.barrier(alice, control, bob) # @phaseDisk

# Entangle control and Bob's qubit
circuit.h(control[0])
circuit.cx(control[0], bob[0])
circuit.barrier(alice[0], control[0], bob[0])

# Send Bob his qubit, and then decode Alice's qubit
circuit.cx(alice[0], control[0])
circuit.h(alice[0])
circuit.barrier(alice[0], control[0], bob[0])

# Measure and recreate Bob's qubit
circuit.measure(alice[0], c[0])
circuit.measure(control[0], d[0])
circuit.cx(control[0], bob[0]) # if control qubit is 1, apply X to Bob's qubit
circuit.cz(alice[0], bob[0]) # if Alice's qubit is 1, apply Z to Bob's qubit