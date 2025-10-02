# ZKGRA - Laboratory Work No. 2

**Fundamentals of Cryptography**  
**Student:** Maroš Bednár (xbednarm1@stuba.sk)  
**Instructor:** volodymyr.khylenko@stuba.sk

## Assignment Overview

This laboratory work implements:
1. **Polybius Square (6×6)** - Classical substitution cipher
2. **XOR Operations** - Bitstring manipulation and property testing
3. **Entropy Calculations** - Shannon entropy for equiprobable distributions

## Polybius Square (6×6)

The Polybius square is a 6×6 grid containing letters A-Z and digits 0-9:

|   | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| **1** | A | B | C | D | E | F |
| **2** | G | H | I | J | K | L |
| **3** | M | N | O | P | Q | R |
| **4** | S | T | U | V | W | X |
| **5** | Y | Z | 0 | 1 | 2 | 3 |
| **6** | 4 | 5 | 6 | 7 | 8 | 9 |

Each character is encoded as a two-digit coordinate (row, column).

### Features
- ✅ Supports A-Z letters and 0-9 digits
- ✅ Removes Slovak diacritics (Á→A, Č→C, etc.) using `unicodedata`
- ✅ Preserves spaces in encoded output
- ✅ Returns both space-separated pairs and concatenated format

## Installation

No external dependencies required (Python 3.9+). For testing, optionally install pytest:

```bash
pip install pytest
```

## Usage

### Command Line Interface

The CLI provides several modes of operation:

#### Polybius Encoding
```bash
python main.py --encode "ENCRYPT ME 2 DAY"
```
Output:
```
Input: ENCRYPT ME 2 DAY
Space-separated pairs: 15 32 13 36 51 34 42  31 15  55  14 11 51
Concatenated: 15321336513442 3115 55 141151
```

#### Polybius Decoding
```bash
python main.py --decode "15 32 13 36 51 34 42"
```
Output:
```
Input: 15 32 13 36 51 34 42
Decoded: ENCRYPT
```

#### XOR Operations
```bash
python main.py --xor 1011 0110 0100
```
Output:
```
Bitstrings: 1011 XOR 0110 XOR 0100
Result: 1001

Expression a⊕b⊕c⊕a⊕b = 0100
```

#### Entropy Calculation
```bash
python main.py --entropy 8
```
Output:
```
Entropy H(8) = 3.000000 bits
            = 3 bits (exact power of 2)
```

#### Surname Test
```bash
python main.py --surname "BEDNÁR"
```
Output:
```
Surname: BEDNÁR
Encoded (pairs): 12 15 14 32 11 36
Encoded (concat): 121514321136
Decoded: BEDNAR
Match: ✓
```

### Python API

```python
from src.polybius import encode, decode
from src.xor_utils import xor_chain, evaluate_expression
from src.entropy import entropy_equiprobable

# Polybius encoding
pairs, concat = encode("HELLO")
print(pairs)  # "22 15 26 26 33"

# Polybius decoding
plaintext = decode("22 15 26 26 33")
print(plaintext)  # "HELLO"

# XOR operations
result = xor_chain("1011", "0110", "0100")
print(result)  # "1001"

# XOR expression evaluation
result = evaluate_expression("1011", "0110", "0100")
print(result)  # "0100" (equals c, since a⊕b⊕c⊕a⊕b = c)

# Entropy calculation
h = entropy_equiprobable(128)
print(h)  # 7.0 bits
```

## Testing

Run all tests:

```bash
# With pytest
pytest tests/ -v

# Without pytest (manual test runner)
python tests/test_polybius.py
python tests/test_xor.py
python tests/test_entropy.py
```

### Test Results

All acceptance tests pass:

**Polybius Square:**
- ✅ Encode "ENCRYPT ME 2 DAY" → "15 32 13 36 51 34 42  31 15  55  14 11 51"
- ✅ Encode "BEDNÁR" → "12 15 14 32 11 36"
- ✅ Roundtrip encoding/decoding works correctly

**XOR Operations:**
- ✅ Test Set 1: a=1011, b=0110, c=0100 → a⊕b⊕c⊕a⊕b = 0100
- ✅ Test Set 2: a=0101, b=1110, c=1101 → a⊕b⊕c⊕a⊕b = 1101
- ✅ XOR properties: commutative, associative, identity, self-inverse

**Entropy:**
- ✅ H(8) = 3.0 bits
- ✅ H(128) = 7.0 bits
- ✅ Formula H(n) = log₂(n) verified

## Project Structure

```
cvicenie2/
├── main.py              # CLI interface
├── src/
│   ├── polybius.py      # Polybius square encoding/decoding
│   ├── xor_utils.py     # XOR operations
│   └── entropy.py       # Entropy calculations
├── tests/
│   ├── test_polybius.py # Polybius tests
│   ├── test_xor.py      # XOR tests
│   └── test_entropy.py  # Entropy tests
├── README.md            # This file
└── pyproject.toml       # Python project configuration
```

## Theory

### Polybius Square
Classical cipher invented by the ancient Greek historian Polybius. Each letter is replaced by its grid coordinates, making it a simple substitution cipher. The 6×6 variant extends the traditional 5×5 grid to accommodate digits.

### XOR (Exclusive OR)
Binary operation with important properties:
- **Commutative:** a ⊕ b = b ⊕ a
- **Associative:** (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)
- **Identity:** a ⊕ 0 = a
- **Self-inverse:** a ⊕ a = 0

Used extensively in cryptography (stream ciphers, one-time pad).

### Shannon Entropy
Measures uncertainty in a random variable. For n equiprobable outcomes:

**H = log₂(n)**

Examples:
- Coin flip (2 outcomes): H = 1 bit
- Byte (256 outcomes): H = 8 bits
- This assignment: H(8) = 3 bits, H(128) = 7 bits

## Submission

**Author:** Maroš Bednár (xbednarm1@stuba.sk)  
**Course:** ZKGRA - Fundamentals of Cryptography  
**Laboratory:** Work No. 2

---

*For questions or issues, contact the instructor at volodymyr.khylenko@stuba.sk*
