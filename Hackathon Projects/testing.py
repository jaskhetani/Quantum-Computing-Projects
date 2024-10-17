import numpy as np

class Ket:
    def __init__(self, vector: np.ndarray):
        """Initialize the ket (state vector)."""
        if not isinstance(vector, np.ndarray):
            raise ValueError("The state must be a numpy array.")
        self.vector = vector

    def normalize(self):
        """Normalize the ket."""
        norm = np.linalg.norm(self.vector)
        if norm == 0:
            raise ValueError("Cannot normalize a zero vector.")
        self.vector = self.vector / norm

    def tensor_product(self, other):
        """Compute the tensor product |ψ⟩ ⊗ |φ⟩."""
        return Ket(np.kron(self.vector, other.vector))


class QuantumCircuit:
    def __init__(self, num_of_qubits: int):
        """Initialize a quantum circuit with a given number of qubits."""
        self.noq = num_of_qubits  # Number of qubits
        self.kets = 2**self.noq  # Total number of states (2^n)

        # Initialize the state vector to |0⟩^n (all-zero state)
        self.state_vector = np.zeros((self.kets,), dtype=complex)
        self.state_vector[0] = 1  # |00...0⟩ state has amplitude 1

        self.probabilities = [0] * self.kets  # Initialize probabilities
        self.states = [0] * self.kets  # Initialize state angles
        self.gates_applied = []  # Track gates applied

    def __str__(self):
        """Display the current state of the quantum circuit."""
        state_str = ' '.join([f"|{bin(i)[2:].zfill(self.noq)}⟩" for i in range(self.kets)])
        prob_str = ' '.join([str(round(p, 2)).ljust(self.noq) for p in self.probabilities])
        state_angles = ' '.join([str(s).ljust(self.noq) for s in self.states])
        return (f"Quantum Circuit with {self.noq} Qubits:\n"
                f"Kets          | {state_str}\n"
                f"Probabilities | {prob_str}\n"
                f"States        | {state_angles}\n"
                f"Gates Applied: {' -> '.join(self.gates_applied)}\n")

    def update_probabilities(self):
        """Update the probabilities based on the current state vector."""
        self.probabilities = [abs(amplitude)**2 * 100 for amplitude in self.state_vector]

    def update_states(self):
        """Update state angles (degrees) for visualization."""
        self.states = [np.angle(amplitude, deg=True) for amplitude in self.state_vector]

    def apply_x_gate(self, qubit: int):
        """Apply the Pauli-X gate to the given qubit."""
        if qubit >= self.noq:
            raise ValueError(f"Qubit index {qubit} is out of range for {self.noq} qubits.")

        # Apply X gate by flipping the bit at the target qubit (LSB-first)
        new_state_vector = np.zeros_like(self.state_vector, dtype=complex)

        for i in range(self.kets):
            # Flip the bit at the given qubit index (LSB-first)
            flipped_state = i ^ (1 << qubit)  # Adjusted for LSB indexing
            new_state_vector[flipped_state] = self.state_vector[i]

        self.state_vector = new_state_vector  # Update the state vector
        self.update_probabilities()  # Recalculate probabilities
        self.update_states()  # Recalculate angles

        # Record the gate application
        self.gates_applied.append(f"X({qubit})")

    def apply_h_gate(self, qubit: int):
        """Apply the Hadamard (H) gate to the given qubit."""
        if qubit >= self.noq:
            raise ValueError(f"Qubit index {qubit} is out of range for {self.noq} qubits.")

        # Define the Hadamard matrix
        H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

        new_state_vector = np.zeros_like(self.state_vector, dtype=complex)

        # Apply the Hadamard gate to the target qubit
        for i in range(self.kets):
            bit = (i >> qubit) & 1  # Get the bit value at the target qubit
            for j in range(2):
                target_state = i ^ ((bit ^ j) << qubit)
                new_state_vector[target_state] += H[j, bit] * self.state_vector[i]

        self.state_vector = new_state_vector  # Update the state vector
        self.update_probabilities()  # Recalculate probabilities
        self.update_states()  # Recalculate angles

        # Record the gate application
        self.gates_applied.append(f"H({qubit})")

    def apply_z_gate(self, qubit: int):
        """Apply the Pauli-Z gate to the given qubit."""
        if qubit >= self.noq:
            raise ValueError(f"Qubit index {qubit} is out of range for {self.noq} qubits.")

        # Iterate through all kets and apply Z logic to the relevant states.
        for i in range(self.kets):
            bit = (i >> qubit) & 1  # Extract the bit value at the target qubit.
            
            # Flip phase by 180 degrees only for |1⟩ states.
            if bit == 1:
                self.states[i] = (self.states[i] + 180) % 360  # Adjust angle.

        # After adjusting states, ensure probabilities are correct.
        self.update_probabilities()  # Recalculate probabilities.

        # If all angles are 180, reset them to 0 (since phase cancelation occurs).
        if all(angle == 180 for angle in self.states):
            self.states = [0] * self.kets  # Reset all angles to 0.

        # Record the gate application.
        self.gates_applied.append(f"Z({qubit})")


    def initialize(self, state_index: int):
        """Initialize the circuit to a specific state |index⟩."""
        self.state_vector = np.zeros((self.kets,), dtype=complex)
        self.state_vector[state_index] = 1.0
        self.update_probabilities()
        self.update_states()


# Example usage of the QuantumCircuit with X, H, and Z gates
if __name__ == "__main__":
    # Create a 2-qubit quantum circuit
    qc = QuantumCircuit(2)

    print("Initial State:")
    print(qc)

    # Apply X gate to the 0th qubit (LSB-first indexing)
    qc.apply_x_gate(0)
    print("After applying X(0):")
    print(qc)

    # Apply H gate to the 1st qubit (LSB-first indexing)
    qc.apply_h_gate(0)
    print("After applying H(1):")
    print(qc)

    # Apply Z gate to the 0th qubit (LSB-first indexing)
    qc.apply_z_gate(0)
    print("After applying Z(0):")
    print(qc)
