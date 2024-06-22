// Created by: Jas Khetani
// Concept Implemented: Quantum Teleportation
// Tech Stack used: OpenQASM

OPENQASM 2.0;
include "qelib1.inc";

// Qubits:
qreg alice[1];
qreg control[1];
qreg bob[1];
// Classical Bits:
creg c[1];
creg d[1];

// Alice sets her qubit
u(pi / 3, pi / 6, pi / 9) alice[0];
barrier alice, control, bob; // @phaseDisk

// Entangle control and Bob's qubit
h control[0];
cx control[0], bob[0];
barrier alice[0], control[0], bob[0];

// Send Bob his qubit, and then decodde Alice's qubit
cx alice[0], control[0];
h alice[0];
barrier alice[0], control[0], bob[0];

// Measure and recreate Bob's qubit
measure alice[0] -> c[0];
measure control[0] -> d[0];
cx control[0], bob[0]; // if control qubit is 1, apply X to Bob's qubit
cz alice[0], bob[0]; // if Alice's qubit is 1, apply Z to Bob's qubit