// Created by: Jas Khetani
// Concept Implemented: Quantum True Randomness (Single-Qubit Gates)

namespace QuantumCoinFlipper {
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;

    @EntryPoint()
    operation main(): Unit {
        use coin = Qubit(); // Coin formed
        H(coin); // Coin flipped (gives equal probability of landing heads and tails)
        if (ResultAsBool(MResetZ(coin)) == false) { Message("Tails"); } 
        else { Message("Heads"); }
    }

}