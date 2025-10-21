# ZKGRA - Laboratory Work No. 6

**Course:** Fundamentals of Cryptography  
**Student:** Maroš Bednár (xbednarm1@stuba.sk)  
**Date:** October 21, 2025

## Assignment

This laboratory work covers **simplified DES operations**:
1. **Encoding with IP cob permutation** - Using Feistel mesh transformation
2. **Permutation table correspondence** - Mapping between Intel x86 and original DES tables
3. **S-box transformations** - Computing 6-bit to 4-bit substitutions

**Objective:** Formation of skills in working with encryption algorithms using the Feistel grid.

## Project Structure

```
cvicenie6/
├── main.py              # Main program - solves all exercises
├── src/
│   └── des_tables.py   # DES tables and permutation functions
├── zadanie/            # Assignment documents
└── README.md           # This file
```

## Usage

### Run All Exercises

```bash
python3 main.py
```

This will automatically solve:
- Exercise 1: Encode "USTAŠI" using IP cob permutation
- Exercise 2: Find correspondence between permutation tables
- Exercise 3: Calculate S-box transformations for 4 test inputs

### Use as a Library

```python
from src.des_tables import apply_permutation, s_box_lookup, IP_INTEL_X86, S_BOX_2

# Apply permutation
bits = [0, 1, 1, 0, 1, 0, ...]
permuted = apply_permutation(bits, IP_INTEL_X86)

# S-box lookup
input_6bits = "011010"
output_4bits = s_box_lookup(S_BOX_2, input_6bits)
```

## Solutions

### Exercise 1: Encode USTAŠI

**Task:** Encode the vikorist notification "USTAŠI" using IP cob permutation.

**Setup:**
- Student number: xbednarm1 (last digit = **1**)
- Message: **USTAŠI** 
- Alphabet: A-Z (A=1, B=2, ..., Z=26)
- Note: **Š** (skin letter) is one bit

**Letter mapping:**
- U → 21
- S → 19
- T → 20
- A → 1
- Š → 1 (one bit only)
- I → 9

**Original bit pattern (25 bits):**
```
1000000010000000001110000
```

**After IP cob permutation:**
```
0101000100000000110000000
```

**Subdivision into L and R:**
- L (left 12 bits):  `010100010000`
- R (right 13 bits): `0000110000000`

**IP cob mental table:**
```
16  19   5   1  13
14   4  21  10   8
24  11   3  12  22
17   9  20   7  18
23   2   6  15  25
```

### Exercise 2: Permutation Table Correspondence

**Task:** Fill in correspondence table between Intel x86 and original DES IP tables.

| Intel x86 IP position | Original DES IP position | Final IP⁻¹ position |
|----------------------|-------------------------|-------------------|
| **14** | 49 | 52 |
| **23** | 40 | 58 |
| **61** | 2 | 41 |
| **6** | 57 | 54 |

**Explanation:**
- Intel x86 uses different bit numbering than standard DES
- The correspondence table shows where each bit position maps
- This is important for implementing DES on different architectures

### Exercise 3: S-box Transformations

**Task:** Calculate S-box output for 6-bit inputs using the second DES S-box.

**Second DES S-box:**
```
Row 0: 15  1  8 14  6 11  3  4  9  7  2 13 12  0  5 10
Row 1:  3 13  4  7 15  2  8 14 12  0  1 10  6  9 11  5
Row 2:  0 14  7 11 10  4 13  1  5  8 12  6  9  3  2 15
Row 3: 13  8 10  1  3 15  4  2 11  6  7 12  0  5 14  9
```

**Results:**

#### A. Input: `011010`
- Row bits (outer): 0...0 = **0**
- Column bits (middle): 1101 = **13**
- S-box[0][13] = **0**
- **Output: `0000`** (decimal: 0)

#### B. Input: `001111`
- Row bits (outer): 0...1 = **1**
- Column bits (middle): 0111 = **7**
- S-box[1][7] = **14**
- **Output: `1110`** (decimal: 14)

#### C. Input: `110110`
- Row bits (outer): 1...0 = **2**
- Column bits (middle): 1011 = **11**
- S-box[2][11] = **6**
- **Output: `0110`** (decimal: 6)

#### D. Input: `110011`
- Row bits (outer): 1...1 = **3**
- Column bits (middle): 1001 = **9**
- S-box[3][9] = **6**
- **Output: `0110`** (decimal: 6)

**Summary:**
| Input (6 bits) | Output (4 bits) | Decimal |
|---------------|----------------|---------|
| 011010 | 0000 | 0 |
| 001111 | 1110 | 14 |
| 110110 | 0110 | 6 |
| 110011 | 0110 | 6 |

## Implementation Details

### Permutation Application

Permutations are applied by using the permutation table as indices:
```python
permuted[i] = original[permutation_table[i]]
```

### S-box Lookup

S-boxes perform a 6-bit to 4-bit substitution:
1. **Row** is determined by outer bits (bit 0 and bit 5)
2. **Column** is determined by middle bits (bits 1-4)
3. Look up value in S-box[row][column]
4. Convert to 4-bit binary output

### Feistel Structure

The Feistel mesh transformation:
- Splits input into left (L) and right (R) parts
- Applies permutations and substitutions
- Combines parts through XOR operations

## Tables Used

### IP (Initial Permutation) - Intel x86
64-bit permutation used at the start of DES encryption.

### IP⁻¹ (Final Permutation) - Intel x86
64-bit permutation used at the end of DES encryption (inverse of IP).

### IP cob (Mental Table)
25-element permutation table specific to the USTAŠI encoding task.

### Second S-box
4×16 table performing 6-bit to 4-bit substitution in DES rounds.

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Key Concepts

1. **Permutation:** Rearranging bits according to a fixed table
2. **S-box (Substitution box):** Non-linear transformation providing confusion
3. **Feistel structure:** Dividing data into halves and processing iteratively
4. **DES:** Data Encryption Standard using multiple rounds of permutation and substitution

## Notes

- Bit numbering can vary between implementations (0-indexed vs 1-indexed)
- Intel x86 and standard DES use different bit ordering
- S-boxes provide the main security (non-linearity) in DES
- Real DES uses 16 rounds, this is a simplified version
