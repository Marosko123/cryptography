# ZKGRA - Laboratory Work No. 4

**Course:** Fundamentals of Cryptography  
**Student:** Maroš Bednár (xbednarm1@stuba.sk)  
**Date:** October 21, 2025

## Assignment

This laboratory work covers:
1. **Modular arithmetic operations** - Basic modulo and modular inverse calculations
2. **Residual vectors** - Computing sequences of powers modulo m
3. **Diffie-Hellman key exchange** - Asymmetric encryption demonstration

## Project Structure

```
cvicenie4/
├── main.py              # Main program - runs all exercises
├── src/
│   └── modular_arithmetic.py  # Core functions for modular operations
└── README.md           # This file
```

## Usage

### Run All Exercises

```bash
python3 main.py
```

This will solve all exercises automatically:
- Exercise 1: Modular operations and inverses
- Exercise 2: Residual vectors
- Exercise 3: Diffie-Hellman key exchange analysis

### Use as a Library

```python
from src.modular_arithmetic import mod_inverse, residual_vector, diffie_hellman_exchange

# Calculate modular inverse
inv = mod_inverse(7, 47)  # Returns 27

# Generate residual vector
vec = residual_vector(4, 9)  # Returns [4, 7, 1]

# Diffie-Hellman exchange
pub_a, pub_b, shared_a, shared_b = diffie_hellman_exchange(
    g=2,        # generator
    p=23,       # prime modulus
    secret_a=6, # Alice's secret
    secret_b=3  # Bob's secret
)
```

## Solutions

### Exercise 1: Modular Operations

#### Simple Modulo Operations

| Operation | Result |
|-----------|--------|
| 2 mod 4 | **2** |
| 78 mod 33 | **12** |
| 51 mod 7 | **2** |
| 27 mod 47 | **27** |

#### Modular Inverse Operations

| Operation | Result | Verification |
|-----------|--------|--------------|
| 7⁻¹ mod 47 | **27** | 7 × 27 mod 47 = 1 ✓ |
| 19⁻¹ mod 7 | **3** | 19 × 3 mod 7 = 1 ✓ |
| 4⁻¹ mod 7 | **2** | 4 × 2 mod 7 = 1 ✓ |
| 4⁻¹ mod 15 | **4** | 4 × 4 mod 15 = 1 ✓ |
| 3⁻¹ mod 7 | **5** | 3 × 5 mod 7 = 1 ✓ |
| 4⁻¹ mod 17 | **13** | 4 × 13 mod 17 = 1 ✓ |
| 9⁻¹ mod 17 | **2** | 9 × 2 mod 17 = 1 ✓ |
| 2⁻¹ mod 6 | **Does not exist** | gcd(2, 6) = 2 ≠ 1 |

**Note:** Modular inverse exists only when gcd(a, m) = 1 (a and m are coprime).

### Exercise 2: Vector of Residuals

#### 2.1. Vector of residuals of 4 by modulus 9

Powers of 4 modulo 9:
- 4¹ mod 9 = 4
- 4² mod 9 = 16 mod 9 = 7
- 4³ mod 9 = 64 mod 9 = 1
- 4⁴ mod 9 = 4 (cycle repeats)

**Vector:** [4, 7, 1]

#### 2.2. Vector of residuals of 15 by modulus 7

Powers of 15 modulo 7:
- 15¹ mod 7 = 1
- 15² mod 7 = 1 (cycle repeats immediately)

**Vector:** [1]

Note: 15 ≡ 1 (mod 7), so all powers equal 1.

#### 2.3. Vector of residuals of 32 by modulus 29

Powers of 32 modulo 29:
- 32¹ mod 29 = 3
- 32² mod 29 = 9
- 32³ mod 29 = 27
- ... (continues for 28 elements)

**Vector:** [3, 9, 27, 23, 11, 4, 12, 7, 21, 5, 15, 16, 19, 28, 26, 20, 2, 6, 18, 25, 17, 22, 8, 24, 14, 13, 10, 1]

Note: Since 32 ≡ 3 (mod 29) and gcd(3, 29) = 1, the vector contains 28 elements (φ(29) = 28) before repeating.

### Exercise 3: Asymmetric Encryption

#### 3.1. Common Secret Key Calculation

Using Diffie-Hellman key exchange with:
- Alice's secret key: **a = 6**
- Bob's secret key: **b = 3**

##### a) Function: 2ˣ (mod 4)

**Alice's computation:**
- Sends: A = 2⁶ mod 4 = 64 mod 4 = **0**
- Receives B = 0
- Computes: 0⁶ mod 4 = **0**

**Bob's computation:**
- Sends: B = 2³ mod 4 = 8 mod 4 = **0**
- Receives A = 0
- Computes: 0³ mod 4 = **0**

**Shared secret key: 0**

⚠️ **Problem:** This function is NOT suitable for Diffie-Hellman because:
- The modulus 4 is too small
- 2² ≡ 0 (mod 4), so all higher powers are also 0
- No security - the key is always 0

##### b) Function: 78ˣ (mod 33)

First, simplify: 78 mod 33 = 12

**Alice's computation:**
- Sends: A = 78⁶ mod 33 = 12⁶ mod 33 = **12**
- Receives B = 12
- Computes: 12⁶ mod 33 = **12**

**Bob's computation:**
- Sends: B = 78³ mod 33 = 12³ mod 33 = **12**
- Receives A = 12
- Computes: 12³ mod 33 = **12**

**Shared secret key: 12**

⚠️ **Problem:** 12 is a fixed point (12ⁿ ≡ 12 mod 33 for all n ≥ 1), so this is also not suitable for secure key exchange.

#### 3.2. Can we use 2⁻¹ (mod 6) as a common function?

**Answer: NO**

**Justification:**

1. **Modular inverse doesn't exist:**
   - 2⁻¹ mod 6 requires gcd(2, 6) = 1
   - But gcd(2, 6) = 2 ≠ 1
   - Therefore, 2⁻¹ mod 6 does not exist

2. **Not a suitable function:**
   - Even if it existed, a modular inverse is a fixed value, not a function of x
   - Diffie-Hellman requires a function like gˣ mod p
   - 2⁻¹ mod 6 would just be a constant, not something that varies with the secret key

3. **Requirements for Diffie-Hellman:**
   - Need a prime modulus p (or at least a large prime factor)
   - Need a generator g that produces a large subgroup
   - 6 is not prime and is too small for security

**Conclusion:** This function cannot be used for asymmetric encryption.

## Implementation Details

### Extended Euclidean Algorithm

Used to compute modular inverses. Finds integers x, y such that:
```
a·x + m·y = gcd(a, m)
```

If gcd(a, m) = 1, then x is the modular inverse.

### Residual Vector Generation

Computes powers of n modulo m until the pattern repeats:
```
[n¹ mod m, n² mod m, n³ mod m, ...]
```

Stops when a value repeats (cycle detected).

### Diffie-Hellman Key Exchange

1. Alice computes: A = gᵃ mod p (sends to Bob)
2. Bob computes: B = gᵇ mod p (sends to Alice)
3. Alice computes shared key: Bᵃ mod p
4. Bob computes shared key: Aᵇ mod p
5. Both get the same key: gᵃᵇ mod p

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Notes

- All calculations use Python's built-in `pow(base, exp, mod)` for efficient modular exponentiation
- The Extended Euclidean Algorithm is implemented recursively
- Residual vector generation includes cycle detection to avoid infinite loops
