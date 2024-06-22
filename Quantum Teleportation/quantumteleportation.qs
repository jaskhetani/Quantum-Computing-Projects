// Created by: Jas Khetani
// Concept Implemented: Quantum Teleportation
// Tech Stack used: Q#

namespace QuantumFridaysforJune2024 {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;

    @EntryPoint()
    operation QuantumMain(): Unit {
        // Qubits:
        use alice = Qubit(); use control = Qubit(); use bob = Qubit();

        // Complete circuit:
        SetInitialQubit(alice); // Alice sets her qubit
        PrepareBellState(control, bob); // Entangle control and Bob's qubit
        Decode(alice, control); // Send Bob his qubit, and then decode Alice's qubit
        
        // Classical Bits:
        let c = ResultAsBool(M(alice)); let d = ResultAsBool(M(control));

        // Measure and recreate Bob's qubit
        CX(control, bob); // if control qubit is 1, apply X to Bob's qubit
        CZ(alice, bob); // if Alice's qubit is 1, apply Z to Bob's qubit

    }

    operation SetInitialQubit(AliceQ: Qubit) : Unit {
        // Set the below gates to anything you want
        H(AliceQ); X(AliceQ); S(AliceQ);
    }

    operation PrepareBellState(control: Qubit, target: Qubit) : Unit {
        H(control);
        CNOT(control, target);
    }

    operation Decode(message: Qubit, control: Qubit) : Unit {
        CNOT(message, control);
        H(message);
    }

}