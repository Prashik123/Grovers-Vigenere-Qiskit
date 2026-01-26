from qiskit import QuantumCircuit

def diffuser(n_qubits):
    
    #Implements the Grover diffuser (inversion about the mean).
   
    qc = QuantumCircuit(n_qubits)

    qc.h(range(n_qubits))
    qc.x(range(n_qubits))

    qc.h(n_qubits - 1)
    qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    qc.h(n_qubits - 1)

    qc.x(range(n_qubits))
    qc.h(range(n_qubits))

    return qc
