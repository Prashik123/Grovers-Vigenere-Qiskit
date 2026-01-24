from qiskit import QuantumCircuit


def phase_oracle(marked_state):
n = len(marked_state)
qc = QuantumCircuit(n)
for i,b in enumerate(marked_state):
if b == '0': qc.x(i)
qc.h(n-1)
qc.mcx(list(range(n-1)), n-1)
qc.h(n-1)
for i,b in enumerate(marked_state):
if b == '0': qc.x(i)
return qc
