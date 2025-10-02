# Laboratory Work No. 1 - Fundamentals of Cryptography
**Student:** Maros Bednar  
**Course:** Fundamentals of Cryptography  
**Assignment:** Stream and Block Coding Algorithms

## Assignment Overview

This laboratory work implements two coding algorithms as specified in the assignment:

**Task 1a:** Stream coding of information message  
**Task 1b:** Block coding of information message

Both programs use my surname **"BEDNAR"** as the test information message and work with the English alphabet.

## Project Structure

```
cvicenie1/
├── src/
│   ├── cipher.py      - Main program with both algorithms
│   └── mappings.py    - Helper functions for alphabet mappings
├── tests/
│   └── test_cipher.py - Tests to verify correctness
├── report/
│   └── report.md      - Detailed laboratory report
├── examples/
│   └── sample_run.txt - Example program outputs
├── README.md          - This file
└── Makefile          - Commands for running the programs
```

## How to Run

### Prerequisites
- Python 3.9 or higher
- No additional libraries needed (uses only standard Python)

### Running Stream Coding (Task 1a)
```bash
python src/cipher.py --surname "BEDNAR" --mode stream
```

### Running Block Coding (Task 1b)
```bash
python src/cipher.py --surname "BEDNAR" --mode block
```

### Alternative: Using Make Commands
```bash
make run-stream    # Runs stream coding
make run-block     # Runs block coding
make test          # Runs all tests
```

## Algorithm Description

### Task 1a: Stream Coding Algorithm

**Steps according to assignment:**
1. Use student's surname as test message
2. Number letters in reverse order
3. Perform encoding in three steps:
   - Step 1: Form digital representation with direct alphabet numbering
   - Step 2: Form digital representation with reverse alphabet numbering  
   - Step 3: Form ciphertext using correlation of alphabet numbering

**Implementation:**
- Uses English alphabet A-Z
- Direct numbering: A=1, B=2, ..., Z=26
- Reverse numbering: A=26, B=25, ..., Z=1
- Each letter maps to its reverse position (A↔Z, B↔Y, etc.)

### Task 1b: Block Coding Algorithm

**Steps according to assignment:**
1. Use student's surname as test message
2. Divide alphabet into two parts arbitrarily
3. In each part, number letters in reverse order
4. Perform encoding using correspondence of digital designations

**Implementation:**
- Divides alphabet into: Part 1 (A-M) and Part 2 (N-Z)
- Reverses numbering within each part separately
- Part 1: A↔M, B↔L, C↔K, etc.
- Part 2: N↔Z, O↔Y, P↔X, etc.

## Sample Results

### Stream Coding Result for "BEDNAR":
```
Input: BEDNAR
Direct numbers: B=2, E=5, D=4, N=14, A=1, R=18
Reverse numbers: B=25, E=22, D=23, N=13, A=26, R=9
Ciphertext: YVWMZI
Processing time: ~0.75 μs
```

### Block Coding Result for "BEDNAR":
```
Input: BEDNAR
Part 1 (A-M): A↔M, B↔L, C↔K, D↔J, E↔I, F↔H, G↔G
Part 2 (N-Z): N↔Z, O↔Y, P↔X, Q↔W, R↔V, S↔U, T↔T
Ciphertext: LIJZMV
Processing time: ~0.92 μs
```

## Processor Time Measurement

The program measures processing time using Python's `time.perf_counter()` function:
- Single operation timing for individual runs
- Average timing over 10,000 iterations for statistical accuracy
- Results reported in microseconds (μs)

**Typical Performance:**
- Stream coding: ~0.05 μs per character
- Block coding: ~0.05 μs per character (slightly higher due to part determination)

## Files Description

### src/cipher.py
Main program implementing both algorithms. Contains:
- `CipherProcessor` class with both stream and block coding methods
- Command-line interface for easy execution
- Timing measurement functionality
- Input validation and normalization

### src/mappings.py
Helper functions for creating cipher mappings:
- `build_atbash_mapping()` - creates reverse alphabet mapping for stream coding
- `build_block_mapping()` - creates part-based mapping for block coding
- `get_direct_numbers()` and `get_reverse_numbers()` - numbering functions

### tests/test_cipher.py
Comprehensive test suite verifying:
- Correct alphabet mappings
- Proper input normalization
- Algorithm correctness with various inputs
- Involution property (encoding twice returns original)

## Verification

Both algorithms have been verified to be **involutions** - applying the same cipher twice returns the original text:
- BEDNAR → YVWMZI → BEDNAR (stream)
- BEDNAR → LIJZMV → BEDNAR (block)

This property is tested automatically and confirmed in all runs.

## Additional Complications (Optional Task)

To increase cryptoresistance of these simple algorithms, several complications could be introduced:

1. **Multiple alphabet splits** - vary the block boundaries
2. **Key-based alphabet permutation** - scramble alphabet before applying cipher
3. **Cascading ciphers** - apply multiple transformations in sequence
4. **Null character insertion** - add dummy characters at random positions
5. **Position-dependent encoding** - vary encoding based on character position

These complications would significantly increase the difficulty of cryptanalysis while maintaining the basic algorithmic principles.

## Report

Complete detailed analysis including algorithm descriptions, program listings, results, and timing measurements can be found in `report/report.md`.

---

*This implementation fulfills all requirements of Laboratory Work No. 1 for the Fundamentals of Cryptography course.*









