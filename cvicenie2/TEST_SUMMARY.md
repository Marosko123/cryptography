# ZKGRA Lab Work 2 - Test Summary

**Date:** October 2, 2025  
**Student:** Maroš Bednár (xbednarm1@stuba.sk)  
**Status:** ✅ ALL TESTS PASSED

## Test Results

### 1. Polybius Square - Encode & Decode

#### Test Case 1: "ENCRYPT ME 2 DAY"
```
✓ Encoded (pairs): 15 32 13 36 51 34 42  31 15  55  14 11 51
✓ Encoded (concat): 15321336513442 3115 55 141151
✓ Decoded: ENCRYPT ME 2 DAY
```

#### Test Case 2: "BEDNÁR" (with diacritics)
```
✓ Encoded (pairs): 12 15 14 32 11 36
✓ Encoded (concat): 121514321136
✓ Decoded: BEDNAR (diacritics removed)
```

### 2. XOR Calculations: a ⊕ b ⊕ c ⊕ a ⊕ b

#### Test Set 1
```
Input: a=1011, b=0110, c=0100
Result: 0100
✓ CORRECT
```

#### Test Set 2
```
Input: a=0101, b=1110, c=1101
Result: 1101
✓ CORRECT
```

### 3. Entropy Calculations

```
✓ H(8) = 3.0 bits (eight equiprobable states)
✓ H(128) = 7.0 bits (128 equiprobable states)
```

## Unit Tests

### Polybius Tests
```
✓ test_remove_diacritics
✓ test_normalize_text
✓ test_encode_basic
✓ test_encode_with_spaces
✓ test_encode_acceptance_test
✓ test_encode_surname
✓ test_decode_basic
✓ test_decode_with_spaces
✓ test_decode_acceptance_test
✓ test_roundtrip
✓ test_roundtrip_surname
✓ test_all_characters

12 passed, 0 failed
```

### XOR Tests
```
✓ test_xor_chain_two
✓ test_xor_chain_three
✓ test_xor_chain_properties
✓ test_evaluate_expression_testset1
✓ test_evaluate_expression_testset2
✓ test_evaluate_expression_equals_c
✓ test_xor_chain_errors

7 passed, 0 failed
```

### Entropy Tests
```
✓ test_entropy_power_of_2
✓ test_entropy_required_values
✓ test_entropy_non_power_of_2
✓ test_entropy_properties
✓ test_entropy_comparison
✓ test_entropy_errors
✓ test_entropy_formula

7 passed, 0 failed
```

## CLI Functionality

All CLI commands tested and working:

```bash
# Encode text
python main.py --encode "ENCRYPT ME 2 DAY"

# Decode text
python main.py --decode "15 32 13 36 51 34 42  31 15  55  14 11 51"

# Test surname with diacritics
python main.py --surname "BEDNÁR"

# XOR operations
python main.py --xor 1011 0110 0100

# Entropy calculations
python main.py --entropy 8
python main.py --entropy 128
```

## Implementation Notes

- ✅ All functions use Python standard library only
- ✅ Diacritics handled with `unicodedata` module
- ✅ All acceptance tests pass exactly as specified
- ✅ Type hints and docstrings included
- ✅ Manual test runner works without pytest
- ✅ Clean, readable code structure
