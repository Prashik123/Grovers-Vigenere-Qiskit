# Quantum Ciphertext-Only Cryptanalysis of the Vigenère Cipher  
Using Grover’s Algorithm (Qiskit 2.3.0)

---

## Problem Statement

This project addresses the problem of **ciphertext-only cryptanalysis** of the
Vigenère cipher.

Given:
- A text file containing **100 Vigenère-encrypted English words**
- Each word appears on a new line
- The encryption key is **completely unknown**
- No plaintext or plaintext–ciphertext pairs are provided

The objective is to:
1. Estimate the key length
2. Recover the secret key using only ciphertext
3. Decrypt the ciphertext
4. Generate a plaintext output file
5. Demonstrate quantum advantage using Grover’s algorithm

---

## What Is Implemented

The repository implements a **hybrid classical–quantum cryptanalysis pipeline**:

1. Read the ciphertext file
2. Estimate the Vigenère key length using statistical analysis
3. Reduce the cipher into independent Caesar ciphers
4. Recover each key character using χ² frequency analysis
5. Accelerate key search using Grover’s algorithm
6. Decrypt the ciphertext using the recovered key
7. Generate a plaintext file with metrics

All steps operate strictly under the **ciphertext-only attack model**.

---

## Cryptanalytic Logic Used (Ciphertext Only)

### 1. Key Length Estimation – Index of Coincidence (IC)

The **Index of Coincidence (IC)** measures the probability that two randomly chosen
letters from a text are identical.

Formula (plain text):

$\mathrm{IC} = \frac{\sum_i f_i (f_i - 1)}{N (N - 1)}$



