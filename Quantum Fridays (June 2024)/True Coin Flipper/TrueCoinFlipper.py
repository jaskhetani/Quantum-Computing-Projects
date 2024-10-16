# Created by: Jas Khetani
# Concept Implemented: Quantum True Randomness (Single-Qubit Gates)
# Tech Stack used: Qiskit

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute

coinQ  = QuantumRegister(1, 'coinQ') # Coin formed
coin = ClassicalRegister(1, 'coin')
qc = QuantumCircuit(coinQ, coin)

qc.h(coinQ[0]) # Coin flipped (gives equal probability of landing heads and tails)
qc.measure(coinQ, coin)
