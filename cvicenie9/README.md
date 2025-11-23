# Cvičenie 9 - Hash Functions and Digital Signatures

## Description
This project implements hash functions and the Schnorr digital signature algorithm as per the laboratory assignment.

## Structure
- `src/`: Source code modules
    - `hash_functions.py`: Implementation of Task 1 and Task 2 hash functions.
    - `schnorr.py`: Implementation of Schnorr digital signature (Task 3).
    - `des_tables.py`: Tables used for Task 1.
- `main.py`: Main entry point to run the demonstrations.

## Tasks
1. **Hash Functions**:
   - $h(n) = n \pmod m$
   - $h(n) = \sum h(n_i) \pmod m$
   - Calculated for specific parity combinations of $n$ and $m$.

2. **Custom Hash**:
   - A custom algorithm for string hashing.

3. **Schnorr Signature**:
   - Implementation of key generation, signing, and verification.
   - Supports arbitrary bit lengths for $p$ and $q$.

## Usage
Run the main script:
```bash
python3 main.py
```
