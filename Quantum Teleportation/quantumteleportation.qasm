// Created by: Jas Khetani
// Concept Implemented: Quantum Teleportation

OPENQASM 2.0;
include "qelib1.inc";

// Quantum Bits:
qreg alice[1];
qreg control[1];
qreg bob[1];
// Classical Bits:
creg c[1];
creg d[1];

// Alice sets her qubit:
u(pi / 3, pi / 6, pi / 9) alice[0];

// Entangle control and Bob's qubit
h control[0];
cx control[0], bob[0];
barrier alice, control, bob; // @phaseDisk
barrier alice[0], control[0], bob[0];

// Send Bob his qubit
cx alice[0], control[0];
h alice[0];
barrier alice[0], control[0], bob[0];

// Measure and recreate
measure alice[0] -> c[0];
measure control[0] -> d[0];