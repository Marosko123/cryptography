# Laboratory Report No. 1
## Fundamentals of Cryptography

**Course:** Fundamentals of Cryptography  
**Student:** Maros Bednar  
**Date:** September 29, 2025

## Assignment Implementation

This report presents the implementation and results of Laboratory Work No. 1, which consists of:
- **Task 1a:** Stream coding algorithm 
- **Task 1b:** Block coding algorithm

Both tasks use my surname **"BEDNAR"** as the test information message and implement the algorithms according to the specifications provided.

---

## Task 1a: Stream Coding Algorithm

### Algorithm Description

According to the assignment specifications, the stream coding algorithm performs encoding in three steps:

1. **Step 1:** Form digital representation with direct alphabet numbering (A=1, B=2, ..., Z=26)
2. **Step 2:** Form digital representation with reverse alphabet numbering (A=26, B=25, ..., Z=1)  
3. **Step 3:** Form ciphertext using correlation of alphabet numbering

This creates a mapping where each letter corresponds to its reverse position in the alphabet (A↔Z, B↔Y, etc.).

### Algorithm Implementation

The stream coding follows these steps:
1. Normalize input message (convert to uppercase, keep only letters)
2. Calculate direct numbering for each letter
3. Calculate reverse numbering for each letter  
4. Apply transformation using the correlation between direct and reverse numbering

### Alphabet Mapping Table

```
Direct Position:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Plain Letters:    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
Cipher Letters:   Z  Y  X  W  V  U  T  S  R  Q  P  O  N  M  L  K  J  I  H  G  F  E  D  C  B  A
Reverse Position:26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1
```

### Processing Test Message "BEDNAR"

**Normalized Input:** BEDNAR

**Step 1 - Direct Numbering (A=1, B=2, ..., Z=26):**
- B = 2
- E = 5  
- D = 4
- N = 14
- A = 1
- R = 18

**Step 2 - Reverse Numbering (A=26, B=25, ..., Z=1):**
- B = 25
- E = 22
- D = 23
- N = 13
- A = 26
- R = 9

**Step 3 - Ciphertext Formation using Correlation:**
Each letter maps to the letter at its reverse position:
- B (position 2) → Y (position 25)
- E (position 5) → V (position 22)
- D (position 4) → W (position 23)
- N (position 14) → M (position 13)
- A (position 1) → Z (position 26)
- R (position 18) → I (position 9)

**Final Ciphertext:** YVWMZI

### Program Listing (Stream Coding)

The main algorithm is implemented in the `process_atbash()` method:

```python
def process_atbash(self, surname: str) -> Dict:
    """Process surname using stream coding algorithm."""
    normalized = self.normalize_input(surname)
    ciphertext = self.apply_cipher(normalized, self.atbash_mapping)
    direct_nums = get_direct_numbers(normalized)
    reverse_nums = get_reverse_numbers(normalized)
    
    single_time, avg_time_per_char = self.time_cipher_operation(normalized, self.atbash_mapping)
    
    return {
        'normalized': normalized,
        'ciphertext': ciphertext,
        'direct_numbers': direct_nums,
        'reverse_numbers': reverse_nums,
        'single_time_us': single_time,
        'avg_time_per_char_us': avg_time_per_char
    }
```

### Processor Time Results

| Metric | Value |
|--------|-------|
| Single operation | 0.667 μs |
| Average per character (10,000 iterations) | 0.0364 μs/char |
| Total characters processed | 6 |

---

## Task 1b: Block Coding Algorithm

### Algorithm Description

According to the assignment specifications, the block coding algorithm performs the following steps:

1. **Step 1:** Use student's surname as test information message
2. **Step 2:** Divide alphabet into two parts arbitrarily  
3. **Step 3:** In each part, number letters in reverse order
4. **Step 4:** Perform encoding using correspondence of digital designations

### Implementation Details

**Alphabet Division:** 
- Part 1: A, B, C, D, E, F, G, H, I, J, K, L, M (13 letters)
- Part 2: N, O, P, Q, R, S, T, U, V, W, X, Y, Z (13 letters)

**Reverse Numbering within Each Part:**
- Part 1: A(13)↔M(1), B(12)↔L(2), C(11)↔K(3), etc.
- Part 2: N(13)↔Z(1), O(12)↔Y(2), P(11)↔X(3), etc.

### Part-wise Mapping Tables

**Part 1 (A-M) - Reverse Order Mapping:**
```
Position in Part: 1  2  3  4  5  6  7  8  9 10 11 12 13
Plain Letters:    A  B  C  D  E  F  G  H  I  J  K  L  M
Cipher Letters:   M  L  K  J  I  H  G  F  E  D  C  B  A
Reverse Position:13 12 11 10  9  8  7  6  5  4  3  2  1
```

**Part 2 (N-Z) - Reverse Order Mapping:**
```
Position in Part: 1  2  3  4  5  6  7  8  9 10 11 12 13
Plain Letters:    N  O  P  Q  R  S  T  U  V  W  X  Y  Z
Cipher Letters:   Z  Y  X  W  V  U  T  S  R  Q  P  O  N
Reverse Position:13 12 11 10  9  8  7  6  5  4  3  2  1
```

### Processing Test Message "BEDNAR"
Cipher: Z Y X W R S T U V W X Y N
```

### Processing BEDNAR

**Normalized Input:** BEDNAR

**Direct Numbers (A=1...Z=26):**
- B = 2
- E = 5
- D = 4  
- N = 14
- A = 1
- R = 18

**Ciphertext:** LIBMZS

**Character-by-character transformation:**
- B (Part 1) → L
- E (Part 1) → I  
- D (Part 1) → B
- N (Part 2) → M
- A (Part 1) → Z
- R (Part 2) → S

### Timing Results

| Metric | Value |
|--------|-------|
| Single operation | 2.583 μs |
| Average per character (10,000 iterations) | 0.071667 μs/char |
| Total characters processed | 6 |

---

## Complications to Increase Cryptoresistance

### 1. Keyed Alphabet Permutation
Instead of using the standard A-Z ordering, use a keyword to generate a scrambled alphabet. For example, with keyword "CRYPTO":
```
Standard: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Keyed:    CRYPTOABDEFGHIJKLMNQSUVWXZ
```

### 2. Caesar Cipher Pre/Post Processing
Apply a Caesar shift before or after the main cipher:
- **Pre-Caesar**: Shift input by N positions before applying Atbash/block
- **Post-Caesar**: Shift output by M positions after cipher application
- **Combined**: Use both for double protection

### 3. Polyalphabetic Extension
Use multiple cipher alphabets and cycle through them:
- Generate 3-5 different block splits or Atbash variants
- Cycle through alphabets for each character position
- Example: Position 1,4,7... uses Alphabet 1, Position 2,5,8... uses Alphabet 2

### 4. Transposition Layer
Add columnar transposition after substitution:
- Write ciphertext in rows of fixed width
- Read out by columns in key-determined order
- Combines substitution with transposition for hybrid security

### 5. Null Character Insertion
Insert meaningless characters at random positions:
- Add 10-20% null characters (e.g., X, Q, Z in English)
- Use predetermined pattern known only to recipient
- Significantly increases cryptanalysis difficulty

### 6. Homophonic Substitution
Map frequent letters to multiple cipher symbols:
- E might map to [V, K, P] chosen randomly
- A might map to [Z, F, L] chosen randomly  
- Flattens frequency distribution to resist frequency analysis

### 7. Variable Block Sizes
Instead of fixed A-M|N-Z split, use variable partitioning:
- Partition 1: A-H (8 letters)
- Partition 2: I-Q (9 letters)  
- Partition 3: R-Z (9 letters)
- Key determines partition boundaries and reversal patterns

---

## Comparison: Task 1a vs Task 1b

### Simplicity Analysis

**Atbash (1a):**
- ✅ **Implementation**: Single mapping table, straightforward logic
- ✅ **Understanding**: Intuitive "mirror" concept  
- ✅ **Memory**: Only one 26-character mapping required
- ✅ **Computation**: Single table lookup per character

**Block Cipher (1b):**
- ⚠️ **Implementation**: Requires part management and boundary handling
- ⚠️ **Understanding**: Must track which part each letter belongs to
- ⚠️ **Memory**: Multiple mapping tables or runtime computation
- ⚠️ **Computation**: Part determination + table lookup per character

### Security Analysis

**Atbash (1a):**
- ❌ **Historical**: Well-known cipher, easily recognized
- ❌ **Pattern**: Fixed A↔Z relationship reveals cipher type quickly
- ❌ **Frequency**: Preserves letter frequency distribution exactly
- ❌ **Cryptanalysis**: Vulnerable to frequency analysis and known plaintext

**Block Cipher (1b):**
- ✅ **Obscurity**: Less recognizable pattern than classic Atbash
- ✅ **Flexibility**: Configurable part boundaries increase key space
- ❌ **Frequency**: Still preserves frequency within each part
- ⚠️ **Cryptanalysis**: Slightly more resistant but still monoalphabetic

### Performance Comparison

| Metric | Atbash (1a) | Block (1b) | Difference |
|--------|-------------|------------|------------|
| Single operation | 2.417 μs | 2.583 μs | +6.9% |
| Avg per character | 0.067500 μs | 0.071667 μs | +6.2% |
| Memory usage | Lower | Higher | Block needs part info |

---

## Conclusion

Both cipher implementations successfully demonstrate fundamental cryptographic concepts and possess the involution property (self-inverse). The Atbash cipher offers superior simplicity and slightly better performance, while the block cipher provides marginally better security through configurable alphabet partitioning.

**Key findings:**
1. **Involution verified** for both ciphers across all test cases
2. **Performance overhead** of block cipher is minimal (~6-7%)  
3. **Security improvement** of block cipher is limited due to monoalphabetic nature
4. **Practical application** would require additional layers (polyalphabetic, transposition) for real-world security

Both ciphers serve their educational purpose effectively, demonstrating substitution principles while highlighting the limitations of simple monoalphabetic systems in modern cryptographic contexts.