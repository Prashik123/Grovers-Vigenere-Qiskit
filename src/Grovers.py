from qiskit import QuantumCircuit
from .oracle import phase_oracle
from .diffuser import diffuser


def grover_circuit(marked_state, iterations):
n = len(marked_state)
qc = QuantumCircuit(n, n)
qc.h(range(n))
oracle = phase_oracle(marked_state)
for _ in range(iterations):
qc.compose(oracle, inplace=True)
qc.compose(diffuser(n), inplace=True)
qc.measure(range(n), range(n))
return qc
