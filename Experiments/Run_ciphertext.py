import os, sys
from src.ic_analysis import estimate_key_length
from src.classical_attack import recover_key
from src.vigenere import decrypt
from src.grover import grover_circuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# ================= USER CONFIG =================
CIPHERTEXT_FILE = 'data/ciphertext.txt'
OUTPUT_DIR = 'results'
SHOTS = 1024
# ===============================================


os.makedirs(OUTPUT_DIR, exist_ok=True)


# Load ciphertext words
with open(CIPHERTEXT_FILE) as f:
words = [w.strip() for w in f.readlines() if w.strip()]


ciphertext = ''.join(words)


# 1. Estimate key length (ciphertext-only)
key_len = estimate_key_length(ciphertext)


# 2. Recover key using English statistics
secret_key = recover_key(ciphertext, key_len)


# 3. Quantum Grover demonstration (1st key character)
correct_state = format(ord(secret_key[0]) - 65, '05b')
qc = grover_circuit(correct_state, iterations=2)


qc.draw('mpl').savefig(os.path.join(OUTPUT_DIR, 'circuit.png'))
backend = AerSimulator()
counts = backend.run(transpile(qc, backend), shots=SHOTS).result().get_counts()


plot_histogram(counts)
plt.savefig(os.path.join(OUTPUT_DIR, 'histogram.png'))
plt.close()


success_prob = counts.get(correct_state, 0) / SHOTS


# 4. Decrypt all ciphertext words
plaintext_words = [decrypt(w, secret_key) for w in words]


# 5. Write plaintext + metadata
output_file = os.path.join(OUTPUT_DIR, 'recovered_plaintext.txt')
with open(output_file, 'w') as f:
f.write('Recovered Plaintext (Ciphertext-Only Vigenère Attack)\n')
f.write('='*60 + '\n')
f.write(f'Recovered Key : {secret_key}\n')
f.write(f'Estimated Key Length: {key_len}\n')
f.write(f'Quantum Accuracy : {success_prob*100:.2f}%\n')
f.write(f'Shots Used : {SHOTS}\n')
f.write('='*60 + '\n\n')
for w in plaintext_words:
f.write(w + '\n')


print('Recovered key:', secret_key)
print('Plaintext written to:', output_file)
