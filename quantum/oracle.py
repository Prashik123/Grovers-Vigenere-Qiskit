from qiskit import QuantumCircuit
import math

def build_verification_oracle(validity_map):
  
    #Phase oracle marking all indices whose keys decrypt to valid plaintext.
  

    n_states = len(validity_map)
    n_qubits = math.ceil(math.log2(n_states))

    qc = QuantumCircuit(n_qubits)

    for index, valid in validity_map.items():
        if not valid:
            continue

        bits = format(index, f"0{n_qubits}b")

        for i, b in enumerate(bits):
            if b == '0':
                qc.x(i)

        qc.h(n_qubits-1)
        qc.mcx(list(range(n_qubits-1)), n_qubits-1)
        qc.h(n_qubits-1)

        for i, b in enumerate(bits):
            if b == '0':
                qc.x(i)

    return qc
