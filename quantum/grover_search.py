from qiskit import QuantumCircuit, Aer, execute
from .diffuser import diffuser

def grover_search(oracle, n_qubits, iterations):
    qc = QuantumCircuit(n_qubits, n_qubits)

    # Initialize uniform superposition
    qc.h(range(n_qubits))

    for _ in range(iterations):
        qc.compose(oracle, inplace=True)
        qc.compose(diffuser(n_qubits), inplace=True)

    qc.measure(range(n_qubits), range(n_qubits))

    backend = Aer.get_backend("qasm_simulator")
    result = execute(qc, backend, shots=1024).result()
    return result.get_counts()
