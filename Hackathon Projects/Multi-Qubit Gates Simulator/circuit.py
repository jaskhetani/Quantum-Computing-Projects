# Created by: Jas Khetani
# Concept Implemented: Multi-Qubit Gates Calculation
# Tech Stack used: Python Class
# Currently only X gate is useful however, diving deep into the logic behind other gates.

from draw import *
from draw import visualize as v

class QuantumCircuit:
    def __init__(self, num_of_qubits:int):
        # Initial States & Probabilities
        self.noq = num_of_qubits
        self.kets = 2**self.noq
        self.states = [0]*self.kets
        self.probabilities = [100] + [0]*(self.kets-1)
        self.gates_applied = []
    
    def __str__(self):
        return f"Quantum Circuit with {self.noq} Qubits:\nKets          | {' '.join([f'|{bin(i)[2:].zfill(self.noq)}⟩' for i in range(self.kets)])}\nStates        |  {'   '.join([str(s).ljust(self.noq, ' ') for s in self.states])}\nProbabilities |  {'   '.join([str(p).ljust(self.noq, ' ') for p in self.probabilities])}\nGates Applied: {' -> '.join(self.gates_applied)}\n"
    
    def validate_qubit_entry(self, qubit):
        if not (0 <= qubit < self.noq):
            print(f'Error: Qubit {qubit} is out of range!')
            return False
        return True

    # Completed!
    def x(self, qubit):
        new_probabilities = [0] * self.kets
        if self.validate_qubit_entry(qubit):
            for state in range(self.kets):
                flipped_state = state ^ (1 << qubit)
                new_probabilities[flipped_state] += self.probabilities[state]

            self.probabilities = new_probabilities
            self.gates_applied.append(f"X({qubit})")
    
    # Work in progress, state change is left
    def h(self, qubit):
        new_probabilities = [0] * self.kets
        if self.validate_qubit_entry(qubit):
            for state in range(self.kets):
                new_probabilities[state & ~(1 << qubit)] += self.probabilities[state] / 2
                new_probabilities[state | (1 << qubit)] += self.probabilities[state] / 2
                if bin(state)[2:].zfill(self.noq)[-1-qubit] == '1':
                    self.states[state | (1 << qubit)] += 90

            self.probabilities = new_probabilities
            self.gates_applied.append(f"H({qubit})")
    
    # Work in progress, testing left and errors expected
    def z(self, qubit):
        for state in range(self.kets):
            bit = (state >> qubit) & 1
            if bit == 1:
                self.states[state] = (self.states[state] + 180) % 360

        self.gates_applied.append(f"Z({qubit})")

    def visualize(self):
        v(self.noq, self.states, self.probabilities)
        plt.show()
