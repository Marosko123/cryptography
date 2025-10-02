# ZKGRA - Fundamentals of Cryptography
**Course:** Fundamentals of Cryptography (Základy kryptografie a riadenia aplikácií)  
**Student:** Maros Bednar  
**Institution:** Slovak University of Technology in Bratislava  
**Academic Year:** 2025

## 📚 Repository Structure

This repository contains all laboratory works for the Fundamentals of Cryptography course:

```
ZKGRA/
├── cvicenie1/    # Laboratory Work No. 1 - Stream and Block Coding
├── cvicenie2/    # Laboratory Work No. 2 - (In Progress)
└── README.md     # This file
```

## 📋 Laboratory Works Overview

### Laboratory Work No. 1 - Stream and Block Coding
**Status:** ✅ Completed

Implementation of classical cipher algorithms:
- **Task 1a:** Stream coding (Atbash cipher with reverse alphabet)
- **Task 1b:** Block coding (alphabet partitioning with reversal)

**Key Features:**
- English alphabet encoding (A-Z)
- Surname "BEDNAR" as test message
- Direct and reverse numbering systems
- High-precision timing measurements
- Involution property verification

**Results:**
- Stream Coding: BEDNAR → YVWMZI (~0.67μs)
- Block Coding: BEDNAR → LIJZMV (~0.71μs)

[📖 View Lab 1 Details →](./cvicenie1/)

---

### Laboratory Work No. 2 - Polybius Square & XOR Operations
**Status:** 🚧 In Progress

Implementation of Polybius square encoding and XOR operations:
- **Task 1:** Polybius square (6×6 grid) encoding/decoding
- **Task 2:** XOR bitstring operations
- **Task 3:** Information entropy calculations

[📖 View Lab 2 Details →](./cvicenie2/)

---

## 🚀 Quick Start

### Clone the Repository
```bash
git clone https://github.com/Marosko123/cryptography.git
cd cryptography
```

### Navigate to Specific Lab
```bash
# Laboratory Work 1
cd cvicenie1
python src/cipher.py --surname "BEDNAR" --mode stream

# Laboratory Work 2 (when completed)
cd cvicenie2
python main.py --encode "HELLO"
```

## 📊 Course Information

**Course Code:** ZKGRA  
**Instructor:** Prof. Dr. Khilenko V.V.  
**Contact:** volodymyr.khylenko@stuba.sk  

**Course Objectives:**
- Gain experience writing programs using coding algorithms
- Acquire practical skills working with cryptosystems
- Evaluate characteristics and stability of encryption algorithms
- Use software for solving coding and crypto-protection problems

## 📁 Each Lab Contains

- **`src/`** - Source code implementation
- **`tests/`** - Comprehensive test suite
- **`report/`** - Detailed laboratory report
- **`examples/`** - Sample runs and outputs
- **`README.md`** - Lab-specific documentation
- **`Makefile`** - Automation scripts

## 🔧 General Requirements

- **Language:** Python 3.9+
- **Dependencies:** Standard library only (unless specified)
- **Testing:** pytest for automated testing
- **Documentation:** Complete reports with analysis

## 📝 Submission Guidelines

Each laboratory work includes:
1. Algorithm description and implementation
2. Program listings with proper documentation
3. Test results and verification
4. Timing/performance measurements
5. Analysis and conclusions

**Deadline:** 1 week per laboratory work (unless specified otherwise)

## 🏆 Completed Labs

- [x] Laboratory Work No. 1 - Stream and Block Coding
- [ ] Laboratory Work No. 2 - Polybius Square & XOR
- [ ] Laboratory Work No. 3 - TBD
- [ ] Laboratory Work No. 4 - TBD

## 📧 Contact

**Student Email:** xbednarm1@stuba.sk  
**GitHub:** [@Marosko123](https://github.com/Marosko123)
