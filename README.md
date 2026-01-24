# Quantum Ciphertext-Only Cryptanalysis of the Vigenère Cipher  
### Using Grover’s Algorithm (Qiskit 2.3.0)

---

## 1. Overview

This repository implements a **ciphertext-only cryptanalysis** of the classical
**Vigenère cipher** using a **hybrid classical–quantum approach**.

Only the encrypted ciphertext is provided as input:
- No plaintext
- No encryption key
- No side-channel information

The project demonstrates how **statistical cryptanalysis** combined with
**Grover’s quantum search algorithm** enables efficient key recovery and
plaintext reconstruction, while empirically demonstrating **quantum advantage**.

---

## 2. Problem Definition

### Given
- A ciphertext file containing **100 encrypted words**
- Each word is on a new line
- Encryption uses the Vigenère cipher
- The secret key is **unknown**

### Objective
1. Recover the secret key
2. Determine the key length
3. Decrypt all ciphertext words
4. Quantify quantum accuracy using measurement statistics
5. Output a plaintext file with metadata

---

## 3. Vigenère Cipher Mathematics

The Vigenère cipher operates on the alphabet:

\[
A \rightarrow 0, \; B \rightarrow 1, \; \ldots, \; Z \rightarrow 25
\]

### Encryption Formula

\[
C_i = (P_i + K_{i \bmod m}) \bmod 26
\]

Where:
- \( P_i \) = plaintext letter
- \( K_j \) = key letter
- \( m \) = key length
- \( C_i \) = ciphertext letter

### Decryption Formula

\[
P_i = (C_i - K_{i \bmod m} + 26) \bmod 26
\]

Implementation: `src/vigenere.py`

---

## 4. Ciphertext-Only Cryptanalysis Strategy

Because no plaintext is available, the attack relies entirely on **statistical
properties of the English language**.

The attack consists of **three main stages**:

1. Key length estimation
2. Key character recovery
3. Quantum validation using Grover’s algorithm

---

## 5. Key Length Estimation  
### Index of Coincidence (IC)

The **Index of Coincidence** measures the probability that two randomly chosen
letters from a text are identical.

\[
IC = \frac{\sum_{i} f_i (f_i - 1)}{N (N - 1)}
\]

Where:
- \( f_i \) = frequency of letter \( i \)
- \( N \) = total number of letters

### Logic
- Ciphertext is split into `m` streams assuming key length `m`
- IC is computed for each stream
- English-like text yields IC ≈ 0.065
- The key length that maximizes average IC is selected

Implementation: `src/ic_analysis.py`

---

## 6. English Fitness Function  
### χ² (Chi-Square) Statistic

To determine whether decrypted text resembles English, the **χ² statistic** is
used:

\[
\chi^2 = \sum_{i=A}^{Z} \frac{(O_i - E_i)^2}{E_i}
\]

Where:
- \( O_i \) = observed frequency of letter \( i \)
- \( E_i \) = expected frequency of letter \( i \) in English

Lower χ² indicates a closer match to English.

Implementation: `src/english_score.py`

---

## 7. Classical Ciphertext-Only Key Recovery

Once the key length \( m \) is known:
- The ciphertext is split into \( m \) independent Caesar ciphers
- Each key character is recovered by minimizing χ²
- This yields the full Vigenère key

Classical complexity per character:
\[
O(26)
\]

Implementation: `src/classical_attack.py`

---

## 8. Quantum Search Formulation

Each key character search is mapped to a **quantum search problem**:

- Search space size: \( N = 26 \)
- Qubits required: \( \lceil \log_2 26 \rceil = 5 \)

The goal is to amplify the amplitude of the basis state corresponding to the
correct key character.

---

## 9. Grover’s Algorithm

Grover’s algorithm provides a quadratic speedup for unstructured search.

### Optimal Number of Iterations

\[
k \approx \left\lfloor \frac{\pi}{4} \sqrt{N} \right\rfloor
\]

For \( N = 26 \):

\[
k \approx 2
\]

---

## 10. Oracle Construction

The oracle performs a **phase flip** on the marked state:

\[
|x\rangle \rightarrow -|x\rangle
\]

This is implemented using:
- Multi-controlled NOT (MCX) gates
- Ancilla-free phase marking

Implementation:
- `src/oracle.py`
- `src/diffuser.py`

---

## 11. Quantum Circuit Structure

The Grover circuit consists of:

1. Hadamard gates → uniform superposition
2. Oracle → phase marking
3. Diffuser → amplitude amplification
4. Measurement → key extraction

The circuit is saved automatically to:

