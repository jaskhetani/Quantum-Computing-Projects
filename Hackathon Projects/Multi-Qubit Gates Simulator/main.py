# Created by: Jas Khetani
# To use the simulator

from circuit import QuantumCircuit

qc = QuantumCircuit(2)
qc.x(0)
print(qc)
qc.visualize()