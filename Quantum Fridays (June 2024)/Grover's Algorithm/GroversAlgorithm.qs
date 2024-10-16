// Created by: Jas Khetani
// Concept Implemented: Grover's Algorithm
// Tech Stack used: Q#
// Under maintenance, will be available soon

namespace QuantumFridaysforJune2024 {
    open Microsoft.Quantum.Arrays;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Measurement;

    @EntryPoint()
    operation Main() : Result[] {
    let nQubits = 5;
    let iterations = CalculateOptimalIterations(nQubits);
    Message($"Number of iterations: {iterations}");

    // Use Grover's algorithm to find a particular marked state.
    let results = GroverSearch(nQubits, iterations, ReflectAboutMarked);
    return results;
    }

    operation GroverSearch(
        nQubits : Int,
        iterations : Int,
        phaseOracle : Qubit[] => Unit) : Result[] {

        use qubits = Qubit[nQubits];

        PrepareUniform(qubits);

        for _ in 1..iterations {
            phaseOracle(qubits);
            ReflectAboutUniform(qubits);
        }

        // Measure and return the answer.
        return MResetEachZ(qubits);
    }

    function CalculateOptimalIterations(nQubits : Int) : Int {
        if nQubits > 63 {
            fail "This sample supports at most 63 qubits.";
        }
        let nItems = 1 <<< nQubits; // 2^nQubits
        let angle = ArcSin(1. / Sqrt(IntAsDouble(nItems)));
        let iterations = Round(0.25 * PI() / angle - 0.5);
        return iterations;
    }

    operation ReflectAboutMarked(inputQubits : Qubit[]) : Unit {
        Message("Reflecting about marked state...");
        use outputQubit = Qubit();
        within {
            // We initialize the outputQubit to (|0⟩ - |1⟩) / √2, so that
            // toggling it results in a (-1) phase.
            X(outputQubit);
            H(outputQubit);
            // Flip the outputQubit for marked states.
            // Here, we get the state with alternating 0s and 1s by using the X
            // operation on every other qubit.
            for q in inputQubits[...2...] {
                X(q);
            }
        } apply {
            Controlled X(inputQubits, outputQubit);
        }
    }

    operation PrepareUniform(inputQubits : Qubit[]) : Unit is Adj + Ctl {
        for q in inputQubits {
            H(q);
        }
    }

    operation ReflectAboutAllOnes(inputQubits : Qubit[]) : Unit {
        Controlled Z(Most(inputQubits), Tail(inputQubits));
    }

    operation ReflectAboutUniform(inputQubits : Qubit[]) : Unit {
        within {
            // Transform the uniform superposition to all-zero.
            Adjoint PrepareUniform(inputQubits);
            // Transform the all-zero state to all-ones
            for q in inputQubits {
                X(q);
            }
        } apply {
            // Now that we've transformed the uniform superposition to the
            // all-ones state, reflect about the all-ones state, then let the
            // within/apply block transform us back.
            ReflectAboutAllOnes(inputQubits);
        }
    }

}